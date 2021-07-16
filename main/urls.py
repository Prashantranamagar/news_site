from django.conf.urls import include

from django.urls import path

from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('panel/', views.panel, name='panel'),
    path('login/', views.log_in, name='log_in'),
    path('logout/', views.log_out, name='log_out'),
    path('panel/sitesettings', views.sitesettings, name='sitesettings'),
    path('panel/aboutsettings', views.aboutsettings, name='aboutsettings'),
    path('panel/changepass', views.changepass, name='changepass'),
    path('register', views.myregister, name='myregister'),







]