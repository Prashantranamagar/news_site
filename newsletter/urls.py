from django.urls import path
from .import views



urlpatterns = [
    path('newsletter/', views.newsletter, name='newsletter'),
    path('panel/email', views.email, name='email'),
    path('panel/phone', views.phone, name='phone'),


    path('panel/delemailphone/<int:pk>/<int:num>', views.delemailphone, name='delemailphone'),



]