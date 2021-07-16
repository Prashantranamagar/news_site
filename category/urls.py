from django.conf.urls import include

from django.urls import path

from .import views


urlpatterns = [
 
    path('panel/categorylist', views.categorylist, name='categorylist'),
    path('panel/addcategory', views.addcategory, name='addcategory'),
    path('panel/delcategory/<int:pk>', views.delcategory, name='delcategory'),



]