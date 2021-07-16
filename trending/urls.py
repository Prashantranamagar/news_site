

from django.urls import path

from .import views


urlpatterns = [
 
    path('panel/addtrending', views.addtrending, name='addtrending'),
    path('panel/addtrending/delete<int:pk>', views.deltrending, name='deltrending'),

    path('panel/addtrending/edit<int:pk>', views.edittrending, name='edittrending'),




]