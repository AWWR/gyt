"""SmartTransportation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from . import views, useDB
from . import login

urlpatterns = [
    path('home/', views.mainpage),
    path('page1/', views.p1),
    path('page2/', views.p2),
    path('useDB/', useDB.testdb),
    path('login/', views.login),
    path('login2/', views.login2),
    path('manager/', views.manager),
path('add/', views.add),
path('delete/', views.delete),
path('edit/', views.edit),
path('search/', views.search),

    path('testecharts/', views.web_show, name="web_show"),

]
