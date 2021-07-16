

from django.urls import path, re_path

from .import views


urlpatterns = [
    path('news/<str:word>', views.newsdetail, name='newsdetail'),
    path('panel/addnews', views.addnews, name='addnews'),
    path('panel/newslist', views.newslist, name='newslist'),
    path('panel/del<int:pk>', views.newsdelete, name='newsdelete'),
    path('panel/edit<int:pk>', views.newsedit, name='newsedit'),
    path('panel/publish<int:pk>', views.newspublish, name='newspublish'),
    path('panel/unpublish<int:pk>', views.newsunpublish, name='newsunpublish'),
    path('panel/allnews<str:word>', views.all_news, name='all_news'),




]