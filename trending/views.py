from django.shortcuts import render, redirect
from .models import Trending


# Create your views here.

def addtrending(request):

	if request.method == 'POST':
		trending = request.POST.get('trending')


		if trending == '':
			error = 'All field required.'
			return render(request, 'back/error.html', {'error':error})

		b=Trending(trending=trending)
		b.save()

	trending=Trending.objects.all()

	return render(request, 'back/addtrending.html', {'trending':trending})


def deltrending(request, pk):

	b=Trending.objects.filter(pk=pk)
	b.delete()

	return redirect('addtrending')



def edittrending(request, pk):
	mytxt= Trending.objects.get(pk=pk).trending

	if request.method == 'POST':
		txt = request.POST.get('trending')

		if txt == '' :
			error= "all field required"
			return render (request, 'back/error.html', {'error':error})

		b= Trending.objects.get(pk=pk)
		b.trending = txt
		b.save()

		return redirect('addtrending')

	trending=Trending.objects.all()


	return render (request, 'back/edittrending.html', { 'pk':pk, 'mytxt':mytxt, 'trending':trending})
	