from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from news.models import News
from category.models import Category


def categorylist(request):
	category = Category.objects.all()

	return render(request, 'back/categorylist.html', {'category':category})


def addcategory(request):


	if request.method =='POST':
		category= request.POST.get('category')

		if category == "" :
			error = "All Field Required"
			return render(request, 'back/error.html', {'error':error})


		if len(Category.objects.filter(name=category)) !=0 :
			error = "This name used already"
			return render(request, 'back/error.html', {'error':error})


		b = Category(name=category)
		b.save()
		return redirect('categorylist')
				


	return render(request,'back/addcategory.html')	




def delcategory(request, pk):

	b=Category.objects.filter(pk=pk)
	b.delete()

	return redirect('categorylist')



