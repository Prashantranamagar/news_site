from django.conf.urls import include

from django.urls import path

from .import views


urlpatterns = [
    path('panel/managerlist', views.managerlist, name='managerlist'),
    path('panel/managerlist/delete<int:pk>', views.delmanager, name='delmanager'),
    path('panel/managergroup', views.managergroup, name='managergroup'),
    path('panel/managerperms', views.managerperms, name='managerperms'),

    path('panel/managergroup/add', views.addmanagergroup, name='addmanagergroup'),
    path('panel/managergroup/delete<str:name>', views.delgroupmanager, name='delgroupmanager'),
    path('panel/usergroup/show<int:pk>', views.usergroup, name='usergroup'),
    path('panel/addusergroup/<int:pk>', views.addusergroup, name='addusergroup'),
    path('panel/delusergroup/<int:pk>/<str:name>', views.delusergroup, name='delusergroup'),


    path('panel/delgroupmanager/<int:pk><str:name>', views.delgroupmanager, name='delgroupmanager'),
    path('panel/delmanagerperms/<str:name>', views.delmanagerperms, name='delmanagerperms'),
    path('panel/addmanagerperms', views.addmanagerperms, name='addmanagerperms'),

    path('panel/userperm/show<int:pk>', views.userperm, name='userperm'),
    path('panel/deluserperm/<int:pk><str:name>', views.deluserperm, name='deluserperm'),
    path('panel/adduserperm/<int:pk>', views.adduserperm, name='adduserperm'),


    path('panel/groupperm/<str:name>', views.groupperm, name='groupperm'),
    path('panel/delgroupperm/<str:gname><str:name>', views.delgroupperm, name='delgroupperm'),
    path('panel/addgroupperm/<str:name>', views.addgroupperm, name='addgroupperm'),











 

]