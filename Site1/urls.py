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
    path('', views.auth, name='home'),
    path('register/', views.register),
    path('register/create', views.create),
    path('adm/create/', views.create),
    path('adm/delete/<int:id>', views.delete),
    path('adm/appdelete/<int:id>', views.appdelete),
    path('logfail', views.login3),
    path('adm/', views.adm),
    path('id<int:id>/', views.user),
    path('id<int:id>/id<int:id2>/', views.user),
    path('contacts', views.about),
    path('about', views.abouts),
    path('id<int:id>/logout', views.logout),
    path('adm/logout', views.admlogout),
    path('id<int:id>/appointments/logout', views.logout),
    path('id<int:id>/makeappoint', views.makeappoint),

]

urlpatterns += staticfiles_urlpatterns()