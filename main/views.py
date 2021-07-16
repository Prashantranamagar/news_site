from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from news.models import News
from category.models import Category
from subcategory.models import Subcategory
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from trending.models import Trending
import random
from random import randint
from django.contrib.auth.models import User
from manager.models import Manager
from ipware import get_client_ip
from ip2geotools.databases.noncommercial  import DbIpCity
from django.contrib.gis.geoip2 import GeoIP2
import random
import string



# Create your views here.


def home(request):

	site = Main.objects.get()	
	news = News.objects.filter(act=1).order_by('-pk')
	category = Category.objects.all()
	subcategory = Subcategory.objects.all()
	lastnews = News.objects.filter(act=1).order_by('-pk')[:3]
	trending =Trending.objects.all()[:3]
	popnews2 = News.objects.filter(act=1).order_by('-show')[:3]
	trendingrandom =Trending.objects.all()[random.randint(0, len(trending) -1)]   #show trending randomly 
	lastnews2 = News.objects.filter(act=1).order_by('-pk')[:4]




	
	return render(request,'front/home.html', {'site' : site, 'news' : news, 'category':category, 'subcategory':subcategory, 'lastnews':lastnews,'lastnews2':lastnews2, 'popnews2':popnews2 , 'trending':trending, 'trendingrandom':trendingrandom})
  

def about(request):

	site = Main.objects.get()
	news = News.objects.filter(act=1).order_by('-pk')
	category = Category.objects.all()
	subcategory = Subcategory.objects.all()
	lastnews = News.objects.filter(act=1).order_by('-pk')[:3]
	popnews = News.objects.filter(act=1).order_by('-pk')[:3]
	trending =Trending.objects.all()[:3]
	popnews2 = News.objects.filter(act=1).order_by('-show')[:3]





	return render(request,'front/about.html', {'site' : site, 'news' : news, 'category':category, 'subcategory':subcategory, 'lastnews':lastnews, 'popnews':popnews, 'popnews2':popnews2 , 'trending':trending} )



def panel(request):


	if not request.user.is_authenticated:
		return redirect('log_in')

	# rand = random.randint(0,1000000)  # Generates random number from 0 to 10000.

	# randi = ""
	# for i in range(10): #loop 0,10
	# 	randi= randi + random.choice(string.ascii_letters) # generate random character
	
	# test = ['!', '#', '@', '$', '%']
	# ran=  random.choice(test)   # randomly choose one character from test

	test = ['!', '#', '@', '$', '%']
	rand = ""
	for i in range(4):
		rand= rand + random.choice(string.ascii_letters)
		rand +=random.choice(test)
		rand +=str(random.randint(0,9))

	count = News.objects.count() # count = len(News.objects.all)
	random_news = News.objects.all()[random.randint(0,count-1)]

	return render(request,'back/home.html', {'rand':rand , 'random_news':random_news})	



def log_in(request):

	if request.method == 'POST':
		uname =request.POST.get('username')
		upass = request.POST.get('password')

		if uname != "" and upass != "" :
			user = authenticate(username=uname, password=upass)

			if user != None :

				login(request, user)
				return redirect('panel')


	return render(request,'back/login.html')



def log_out(request):

	logout(request)

	return redirect(log_in)


def sitesettings(request):

	if request.method == 'POST':
		sitename =request.POST.get('sitename') 
		sitetell =request.POST.get('sitetell') 
		fb=request.POST.get('fb') 
		tw =request.POST.get('tw') 
		link =request.POST.get('link') 
		about =request.POST.get('about') 

		if fb=="": fb='#'
		if tw=="": tw='#'
		if link=="": link='#'

		if sitetell =="" or sitename =="" or about =="" :
			error = "All Field Required"
			return render(request, 'back/error.html', {'error':error})

		try:

			myfile = request.FILES['myfile']
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)
			url = fs.url(filename)


			b = Main.objects.get(pk=2)
			b.name= sitename
			b.fb= fb
			b.tw= tw
			b.link= link
			b.tel= sitetell
			b.picurl=url
			b.picname=filename
			b.save()

		except:
			b = Main.objects.get(pk=2)
			b.name= sitename
			b.fb= fb
			b.tw= tw
			b.link= link
			b.tel= sitetell
			
			b.save()





	site = Main.objects.get(pk=2)


	return render(request, "back/sitesettings.html", {'site':site})


def aboutsettings(request):


	if request.method == 'POST':
		about =request.POST.get('about') 
		


		if about =="" :
			error = "All Field Required"
			return render(request, 'back/error.html', {'error':error})

	
		b = Main.objects.get(pk=2)
		b.abouttxt= about
			
		b.save()





	site = Main.objects.get(pk=2)



	return render(request, 'back/aboutsettings.html', {'site':site})




def contact(request):

	site = Main.objects.get()	
	popnews = News.objects.all().order_by('-pk')[:3]
	trending = Trending.objects.all()[:3]
	popnews2 = News.objects.all().order_by('-show')[:3]




	
	return render(request,'front/contact.html', {'site' : site, 'popnews' : popnews, 'trending':trending, 'popnews2':popnews2 })





def changepass(request):



	if request.method == 'POST':
		newpass =request.POST.get('newpass') 
		oldpass =request.POST.get('oldpass') 

		if newpass=="" or oldpass=="":
			error = 'All Field Required.'
			return render (request, 'back/error.html', {'error':error})
		user = authenticate(username=request.user, password=oldpass)
		if user!= None:

			if len(newpass) < 8:
				error = 'Your password required at least 8 character.'
				return render (request, 'back/error.html', {'error':error})

			count1 = 0
			count2 = 0
			count3 = 0
			count4 = 0
			for i in newpass:
				if i > "0" and i<"9":
					count1 += 1
				if i > "A" and i<"2":
					count2 += 1
				if i > "a" and i<"2":
					count3 += 1
				if i > "!" and i<"(":
					count4 += 1

			if count1 == 1 and count2 == 1 and count3 == 1 and count4 == 1 :
				user = User.objects.get(username=request.user)
				user.set_password(newpass)
				user.save()
				return redirect('mylogout')

		else:
			error = "Your password is not correct"
			return render (request, 'back/error.html', {'error':error})





		

	return render(request, 'back/changepass.html')





def myregister(request):

	if request.method == 'POST':
		name=request.POST.get('name')

		uname=request.POST.get('uname')
		email=request.POST.get('email')
		password1=request.POST.get('password1')
		password2=request.POST.get('password2')


		if name =="":
			messgage= "input your name."
			return render(request, 'back/msgbox.html', {'messgage':messgage})


		if password1 != password2 :
			 messgage = "Your password didn't match."
			 return render(request, 'front/msgbox.html', {'messgage':messgage})

		count1 = 0
		count2 = 0
		count3 = 0
		count4 = 0
		for i in password1:
			if i > "0" and i<"9":
				count1 += 1
			if i > "A" and i<"2":
				count2 += 1
			if i > "a" and i<"2":
				count3 += 1
			if i > "!" and i<"(":
				count4 += 1

		if count1 == 0 and count2 == 0 and count3 == 0 and count4 == 0 :

			message = "Your password is not strong."
			return render(request, 'front/msgbox.html', {'message':message})

		if len(password1) < 8: 
			message = "Your password must be 8 character."
			return render(request, 'front/msgbox.html', {'message':message})

		if len(User.objects.filter(username=uname)) == 0 and len (User.objects.filter(email=email)) == 0 :

			ip, is_routable = get_client_ip(request)

			
			if ip is None:

				ip = "0.0.0.0"

			

			try :
				response = DbIpCity.get(ip,api_key='free')
				country = response.country + "|" + response.city

			except:
				country = "Unknown"



			user = User.objects.create_user(username=uname, email=email, password=password1)

			b = Manager(name=name, utxt=uname, email=email, ip=ip, country=country)
			b.save()
			


	return render(request, 'back/login.html')



