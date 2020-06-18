"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views
# from .views import *

# notice    >    urls.py
app_name='notice'
urlpatterns = [
    path('noticeList/', views.list, name="list"),
    # name은 중복 불가
    path('noticeList/<int:page>', views.list, name='listPage'),
    path('noticeWrite/', views.write, name="write"),
    path('noticeSelect/<int:num>', views.select, name="select"),
    path('noticeUpdate/<int:num>', views.update, name="update"),
    path('noticeDelete/<int:num>', views.delete, name="delete")
]
