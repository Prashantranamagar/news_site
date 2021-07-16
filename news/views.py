from django.shortcuts import render, get_object_or_404, redirect

from .models import News
from django.core.files.storage import FileSystemStorage
import datetime
from subcategory.models import Subcategory
from category.models import Category
from main.models import Main
from trending.models import Trending
from comments.models import Comments
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from random import randint
# Create your views here.


def newsdetail(request, word):

	site = Main.objects.get()	
	news = News.objects.all().order_by('-pk')
	category = Category.objects.all()
	subcategory = Subcategory.objects.all()
	lastnews = News.objects.all().order_by('-pk')[:3]

	shownews = News.objects.filter(name=word)
	popnews = News.objects.all().order_by('-show')
	popnews2 = News.objects.all().order_by('-show')[:4]
	trending = Trending.objects.all()[:3]



	try:
		mynews = News.objects.get(name=word)
		mynews.show = mynews.show + 1
		mynews.save()

	except:
		print ('Cant add views')

	code = News.objects.get(name=word).pk
	comment = Comments.objects.filter(news_id=code, status=1).order_by('-pk')[:3]
	
	return render(request,'front/newsdetail.html', {'site' : site, 'news' : news, 'category':category, 'subcategory':subcategory, 'lastnews':lastnews, 'shownews':shownews, 'popnews':popnews, 'popnews2':popnews2, 'trending':trending, 'code':code, 'comment':comment})



def addnews(request):


	now = datetime.datetime.now()
	year = now.year
	month = now.month
	day = now.day

	if len(str(day)) == 1:
		day = '0' + str(day)
	if len(str(month)) == 1:
		month = '0' + str(month)

	today = str(year) + '/' + str(month) + '/' +str(day)
	time = str(now.hour) + ':' + str(now.minute)


	category =Subcategory.objects.all()

	if request.method =='POST':
		newstitle= request.POST.get('newstitle')
		newscategory= request.POST.get('newscategory')
		newsshorttxt= request.POST.get('newsshorttxt')
		newsbodytxt= request.POST.get('newsbodytxt')
		newsid= request.POST.get('newscategory')


		if newstitle == "" or newsshorttxt == "" or newsbodytxt=="" or newscategory=="" :
			error = "All Field Required"
			return render(request, 'back/error.html', {'error':error})

		try:

			myfile = request.FILES['myfile']
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)
			url = fs.url(filename)


			if str(myfile.content_type).startswith("image"):

				if myfile.size < 5000000:

					newsname = Subcategory.objects.get(pk=newsid).name
					ocatid = Subcategory.objects.get(pk=newsid).catid

					b = News(name=newstitle, shorttxt=newsshorttxt, bodytxt= newsbodytxt, date=today, picurl=url, picname=filename, writer=request.user, catname=newsname, catid=newsid, show=0, time=time, ocatid=ocatid)
					b.save()

					count = len(News.objects.filter(ocatid=ocatid))

					b = Category.objects.get(pk=ocatid)
					b.count = count
					b.save()

					return redirect('newslist')

				else:

					fs = FileSystemStorage()
					fs.delete(b.filename)
					error = "Your file is bigger than 5mb."
					return render(request, 'back/error.html', {'error':error})


			else:

				fs = FileSystemStorage()
				fs.delete(b.filename)

				error = "Your file is not supported"
				return render(request, 'back/error.html', {'error':error})


		except:
			error = "Plese input your image."
			return render(request, 'back/error.html', {'error':error})


	return render(request,'back/addnews.html', {'category':category})	


def newslist(request):
	perm=0
	for i in request.user.groups.all():
		if i.name == "masteruser" : perm=1

	if perm == 0:
		news = News.objects.filter(writer=request.user)

	elif perm == 1:
		newss = News.objects.all()
		paginator = Paginator(newss,5)
		page = request.GET.get('page')

		try:
			news=paginator.page(page)

		except EmptyPage :
			news= paginator.page(paginator.num_pages)

		except PageNotAnInteger:
			news = paginator.page(1)


	return render(request,'back/newslist.html', {'news':news})	


def newsdelete(request, pk):

	try:
		b=News.objects.get(pk=pk)

		fs = FileSystemStorage()
		fs.delete(b.picname)

		ocatid= News.objects.get(pk=pk).ocatid

		b.delete()

		count =len(News.objects.filter(ocatid=ocatid))

		m = Category.objects.get(pk=ocatid)
		m.count = count
		m.save()


	except:
		error = "Something went wrong"
		return render(request, 'back/error.html', {'error':error})

	return redirect('newslist')
	



def newsedit(request, pk):

	if len(News.objects.filter(pk=pk)) == 0:
		error ='News not found.'
		return render(request, 'back/error.html', {'error':error})

	news =News.objects.get(pk=pk)
	category = Subcategory.objects.all()

	if request.method =='POST':
		newstitle= request.POST.get('newstitle')
		newscategory= request.POST.get('newscategory')
		newsshorttxt= request.POST.get('newsshorttxt')
		newsbodytxt= request.POST.get('newsbodytxt')
		newsid= request.POST.get('newscategory')


		if newstitle == "" or newsshorttxt == "" or newsbodytxt=="" or newscategory=="" :
			error = "All Field Required"
			return render(request, 'back/error.html', {'error':error})

		try:

			myfile = request.FILES['myfile']
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)
			url = fs.url(filename)


			if str(myfile.content_type).startswith("image"):

				if myfile.size < 5000000:

					newsname = Subcategory.objects.get(pk=newsid).name
					
					b= News.objects.get(pk=pk)

					fss=FileSystemStorage()
					fss.delete(b.picname)

					b.name=newstitle
					b.shorttxt = newsshorttxt
					b.bodytxt=newsbodytxt
					b.picname=filename
					b.picurl=url
					b.catname=newsname
					b.catid=newsid
					b.act=0

					b.save()

					return redirect('newslist')

				else:

					fs = FileSystemStorage()
					fs.delete(b.filename)
					error = "Your file is bigger than 5mb."
					return render(request, 'back/error.html', {'error':error})


			else:

				fs = FileSystemStorage()
				fs.delete(b.filename)

				error = "Your file is not supported"
				return render(request, 'back/error.html', {'error':error})


		except: 

			newsname = Subcategory.objects.get(pk=newsid).name
					
			b= News.objects.get(pk=pk)

			

			b.name=newstitle
			b.shorttxt = newsshorttxt
			b.bodytxt=newsbodytxt
			b.catname=newsname
			b.catid=newsid

			b.save()

			return redirect('newslist')


	return render(request,'back/newsedit.html', {'pk':pk, 'news':news, 'category':category })	
	




def newspublish(request, pk):

	news = News.objects.get(pk=pk)
	news.act = 1
	news.save()

	return redirect('newslist')

def newsunpublish(request, pk):

	news = News.objects.get(pk=pk)
	news.act = 0
	news.save()

	return redirect('newslist')


def all_news(request, word):

	catid =Category.objects.get(name=word).pk
	news = News.objects.filter(ocatid=catid)

	site = Main.objects.get()	
	category = Category.objects.all()
	subcategory = Subcategory.objects.all()
	lastnews = News.objects.filter(act=1).order_by('-pk')[:3]
	trending =Trending.objects.all()[:3]
	popnews2 = News.objects.filter(act=1).order_by('-show')[:3]
	trendingrandom =Trending.objects.all()[randint(0, len(trending) -1)]   #show trending randomly 
	lastnews2 = News.objects.filter(act=1).order_by('-pk')[:4]




	
	return render(request,'front/all_news.html', { 'site' : site, 'news' : news, 'category':category, 'subcategory':subcategory, 'lastnews':lastnews,'lastnews2':lastnews2, 'popnews2':popnews2 , 'trending':trending})

