"""Site1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import path, re_path
from MySite import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.auth, name='auth'),
    path('register/', views.register, name='register'),
    path('register/create', views.usercreate, name='createpatient'),
    path('adm/create/', views.usercreate, name='createuser'),
    path('adm/delete/<int:id>', views.userdelete, name='deleteuser'),
    path('adm/appdelete/<int:id>', views.appdelete, name='deleteappointment'),
    path('logfail', views.login3, name='logerror'),
    path('adm/', views.adm, name='adminpage'),
    path('id<int:id>/', views.user, name='userpage'),
    path('apptest', views.apptest, name='apptest'),
    path('admtest', views.admtest, name='admtest'),
    path('contacts', views.about, name='contacts'),
    path('about', views.abouts, name='about'),
    path('logout', views.logout, name='logout'),
    path('id<int:id>/makeappoint', views.makeappoint, name='makeappoint'),

]

urlpatterns += staticfiles_urlpatterns()