"""djangoDevelop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('path/', demo1),
    re_path(r'^repath\d+/$', demo1),
    url(r'^url\d+/$', demo1),

    path('pathA<str:data>/', demo2),
    re_path(r'^repathA(\d+)/$', demo2),
    re_path(r'^repathC(?P<data>\d+)/$', demo2),
    url(r'^urlA(\d+)/$', demo2),
    url(r'^urlC(?P<data>\d+)/$', demo2),

    path('pathB<str:x>/', demo3, kwargs={"y": 10}),
    re_path(r'^repathD(\d+)/$', demo3, kwargs={"y": 10}),
    re_path(r'^repathB(?P<x>\d+)/$', demo3, kwargs={"y": 10}),
    url(r'^urlB(?P<x>\d+)/$', demo3, kwargs={"y": 10}),
    url(r'^urlD(\d+)/$', demo3, kwargs={"y": 10}),

    path('pathM/', demo3, kwargs={"x": 23, "y": 10}),
    re_path(r'^repathM/$', demo3, kwargs={"x": 23, "y": 10}),
    url(r'^urlM/$', demo3, kwargs={"x": 23, "y": 10}),
]
