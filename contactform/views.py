from django.shortcuts import render

from .models import Contactform

def addcontact(request):

	if request.method == 'POST':
		email= request.POST.get('email')
		name= request.POST.get('name')
		msg= request.POST.get('msg')

		if email=="" or name=="" or msg== "":
			message="All Field Required."
			return render (request, 'front/msgbox.html', {'message':message})

		b=Contactform(email=email, name=name, msg=msg)
		b.save()

		message="Your message recived."

		return render(request, 'front/msgbox.html', {'message':message})






def contactlist(request):

	



	contactlist= Contactform.objects.all()

	return render(request, 'back/contactlist.html', {'contactlist':contactlist})