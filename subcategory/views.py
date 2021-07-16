from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from news.models import News
from subcategory.models import Subcategory
from category.models import Category


def subcategorylist(request):
	subcategory = Subcategory.objects.all()

	return render(request, 'back/subcategorylist.html', {'subcategory':subcategory})


def addsubcategory(request):
	category = Category.objects.all()

	if request.method =='POST':
		subcategory= request.POST.get('subcategory')
		catid = request.POST.get('category')

		if subcategory == "" :
			error = "All Field Required"
			return render(request, 'back/error.html', {'error':error})


		catname = Category.objects.get(pk=catid).name

		b = Subcategory(name=subcategory, catname=catname   , catid=catid)
		b.save()
		return redirect('subcategorylist')
				


	return render(request,'back/addsubcategory.html', {'category':category})	



