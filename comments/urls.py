from django.conf.urls import include

from django.urls import path
from comments import views




urlpatterns = [
    path('addcomment/<int:pk>', views.addcomment, name='addcomment'),
    path('comments_del/<int:pk>', views.comments_del, name='comments_del'),
    path('comments_list', views.comments_list, name='comments_list'),
    path('comments_confirme/<int:pk>', views.comments_confirme, name='comments_confirme'),

 

]