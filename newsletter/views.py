from django.shortcuts import render, redirect
from .models import Newsletter


def newsletter(request):

    if request.method == 'POST' :

        txt = request.POST.get('txt')
        
        res = txt.find('@')

        if int(res) != -1 :
            b = Newsletter(txt=txt,status=1)
            b.save()
        else:
            
            try:

                int(txt)
                b = Newsletter(txt=txt,status=2)
                b.save()
            
            except:

                return redirect('home')

        
    return redirect('home')





def email(request):
	email=Newsletter.objects.filter(status=1)
	return render(request, 'back/email.html', {'email':email})



def delemailphone(request, pk, num):
	b=Newsletter.objects.get(pk=pk)
	b.delete()

	if int(num)== 1:
		return redirect('email')

	return redirect('phone')



def phone(request):

	phone=Newsletter.objects.filter(status=2)
	return render(request, 'back/phone.html', {'phone':phone})

