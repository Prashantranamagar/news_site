from django.shortcuts import render, get_object_or_404, redirect
from main.models import Main
from news.models import News
from category.models import Category
from subcategory.models import Subcategory
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from trending.models import Trending
import random
from random import randint
from django.contrib.auth.models import User, Group, Permission
from .models import Manager
from django.contrib.contenttypes.models import ContentType


# Create your views here.


def managerlist(request): # Shows new registered users
	perm = 0
	for i in request.user.groups.all():
		if i.name =="masteruser" : perm = 1

	if perm == 0:
		error = "Acess Denied"
		return render(request, 'back/error.html', {'error': error})



	manager= Manager.objects.all()

	
	return render(request,'back/managerlist.html', {'manager':manager})
  



def delmanager(request, pk): # delete registered users

	perm = 0
	for i in request.user.groups.all():
		if i.name =="masteruser" : perm = 1

	if perm == 0:
		error = "Acess Denied"
		return render(request, 'back/error.html', {'error': error})



	manager = Manager.objects.get(pk=pk)
	b = User.objects.filter(username=manager.utxt)
	b.delete()

	manager.delete()
	return redirect('managerlist')



def managergroup(request): #Shows all the groups


	perm = 0
	for i in request.user.groups.all():
		if i.name =="masteruser" : perm = 1

	if perm == 0:
		error = "Acess Denied"
		return render(request, 'back/error.html', {'error': error})

	group = Group.objects.all().exclude(name="masteruser")


	group=Group.objects.all()

	return render(request, 'back/managergroup.html', {'group':group})



def addmanagergroup(request): #add group


	perm = 0
	for i in request.user.groups.all():
		if i.name =="masteruser" : perm = 1

	if perm == 0:
		error = "Acess Denied"
		return render(request, 'back/error.html', {'error': error})



	if request.method == 'POST':
		name= request.POST.get('name')

		if name != "" :
			
			if len(Group.objects.filter(name=name)) == 0:


				group = Group(name=name)
				group.save()


	return redirect(managergroup)



def delgroupmanager(request, name): #delete group


	perm = 0
	for i in request.user.groups.all():
		if i.name =="masteruser" : perm = 1

	if perm == 0:
		error = "Acess Denied"
		return render(request, 'back/error.html', {'error': error})

	group= Group.objects.filter(name=name)
	group.delete()




	return redirect('managergroup')







def usergroup(request, pk): # edit group and permissions of a user


	perm = 0
	for i in request.user.groups.all():
		if i.name =="masteruser" : perm = 1

	if perm == 0:
		error = "Acess Denied"
		return render(request, 'back/error.html', {'error': error})


	manager = Manager.objects.get(pk=pk)
	user = User.objects.get(username=manager.utxt)

	ugroup = []

	for i in user.groups.all():
		ugroup.append(i.name)


	group = Group.objects.all()



	return render(request, 'back/usergroup.html', {'ugroup':ugroup, 'group':group, 'pk':pk})




def addusergroup(request, pk): # add group to a user

	perm = 0
	for i in request.user.groups.all():
		if i.name =="masteruser" : perm = 1

	if perm == 0:
		error = "Acess Denied"
		return render(request, 'back/error.html', {'error': error})



	if request.method == 'POST' :

		gname = request.POST.get('gname')

		group = Group.objects.get(name=gname)
		manager = Manager.objects.get(pk=pk)
		user = User.objects.get(username=manager.utxt)
		user.groups.add(group)



		return redirect('users_groups' , pk=pk)





def delusergroup(request, pk,name): # del group of a user


	perm = 0
	for i in request.user.groups.all():
		if i.name =="masteruser" : perm = 1

	if perm == 0:
		error = "Acess Denied"
		return render(request, 'back/error.html', {'error': error})


	group = Group.objects.get(name=name)
	manager =Manager.objects.get(pk=pk)

	user = User.objects.get(username=manager.utxt)
	user.groups.remove(group)

	



	return redirect('usergroup', pk=pk)


def managerperms(request): # shows all permission


	perm = 0
	for i in request.user.groups.all():
		if i.name =="masteruser" : perm = 1

	if perm == 0:
		error = "Acess Denied"
		return render(request, 'back/error.html', {'error': error})

	perms = Permission.objects.all()


	group=Group.objects.all()

	return render(request, 'back/managerperms.html', {'perms':perms})




def delmanagerperms(request, name): # del permissions


	perm = 0
	for i in request.user.groups.all():
		if i.name =="masteruser" : perm = 1

	if perm == 0:
		error = "Acess Denied"
		return render(request, 'back/error.html', {'error': error})

	perms = Permission.objects.filter(name=name)

	perms.delete()


	return redirect('managerperms')



def addmanagerperms(request): # add permissions


	perm = 0
	for i in request.user.groups.all():
		if i.name =="masteruser" : perm = 1

	if perm == 0:
		error = "Acess Denied"
		return render(request, 'back/error.html', {'error': error})

	if request.method == 'POST':
		name = request.POST.get('name')
		cname = request.POST.get('cname')

		if len(Permission.objects.filter(codename=cname)) == 0:


			content_type = ContentType.objects.get(app_label='main', model='main')
			permission = Permission.objects.create(codename=cname, name=name, content_type=content_type)


		else:
			error = "This codename used before."
			return render(request, 'back/error.html', {'error': error})



	return redirect('managerperms')




def userperm(request, pk): #shows permission of  a user


	perm = 0
	for i in request.user.groups.all():
		if i.name =="masteruser" : perm = 1

	if perm == 0:
		error = "Acess Denied"
		return render(request, 'back/error.html', {'error': error})


	manager = Manager.objects.get(pk=pk)

	user = User.objects.get(username=manager.utxt)

	permission = Permission.objects.filter(user=user)
	uperms = []

	for i in permission:
		uperms.append(i.name)



	perms = Permission.objects.all()



	return render(request, 'back/userperm.html', {'uperms':uperms, 'perms':perms, 'pk':pk})




def deluserperm(request, pk, name): #del permission of user


	perm = 0
	for i in request.user.groups.all():
		if i.name =="masteruser" : perm = 1

	if perm == 0:
		error = "Acess Denied"
		return render(request, 'back/error.html', {'error': error})


	manager = Manager.objects.get(pk=pk)

	user = User.objects.get(username=manager.utxt)

	permission = Permission.objects.get(name=name)
	user.user_permissions.remove(permission)



	return redirect('userperm', pk=pk)


def adduserperm(request, pk): # add permission to user


	perm = 0
	for i in request.user.groups.all():
		if i.name =="masteruser" : perm = 1

	if perm == 0:
		error = "Acess Denied"
		return render(request, 'back/error.html', {'error': error})



	if request.method =='POST' :
		pname = request.POST.get('pname')



		manager = Manager.objects.get(pk=pk)

		user = User.objects.get(username=manager.utxt)

		permission = Permission.objects.get(name=pname)
		user.user_permissions.add(permission)



	return redirect('userperm', pk=pk)



def groupperm(request, name): #shows permission of  a group.


	perm = 0
	for i in request.user.groups.all():
		if i.name =="masteruser" : perm = 1

	if perm == 0:
		error = "Acess Denied"
		return render(request, 'back/error.html', {'error': error})

	group = Group.objects.get(name=name)

	perms = group.permissions.all()

	allperms = Permission.objects.all()

	return render(request, 'back/groupperm.html', {'perms':perms, 'name':name, 'allperms':allperms})






def delgroupperm(request, gname, name): #delete permission of  a group.


	perm = 0
	for i in request.user.groups.all():
		if i.name =="masteruser" : perm = 1

	if perm == 0:
		error = "Acess Denied"
		return render(request, 'back/error.html', {'error': error})

	group = Group.objects.get(name=gname)
	perm = Permission.objects.get(name=name)

	group.permissions.remove(perm)

	return redirect('groupperm', name=gname)




def addgroupperm(request,name):		#add permission to  a group.
    


    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})


    if request.method == 'POST' :

        pname = request.POST.get('pname')

        group = Group.objects.get(name=name)
        perm = Permission.objects.get(name=pname)

        group.permissions.add(perm)

    return redirect('groupperm', name=name)