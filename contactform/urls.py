

from django.urls import path, re_path

from .import views


urlpatterns = [
    
    path('contact/submit', views.addcontact, name='addcontact'),
    path('panel/contactlist', views.contactlist, name='contactlist'),



]