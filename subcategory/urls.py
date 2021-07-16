from django.conf.urls import include

from django.urls import path

from .import views


urlpatterns = [
 
    path('panel/subcategorylist', views.subcategorylist, name='subcategorylist'),
    path('panel/addsubcategory', views.addsubcategory, name='addsubcategory'),





]