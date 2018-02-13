"""FollowMe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include,re_path


import FollowMeApp
from FollowMeApp.views import (login_view, register_view, logout_view, index)
from geoApp.views import (map,getPosition) 
urlpatterns = [
    path('admin/', admin.site.urls),
	re_path(r'FollowMeApp/', include('FollowMeApp.urls')),
    re_path(r'geoApp/', include('geoApp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path(r'/login/', login_view, name= 'login'),
    re_path(r'/logout/' , logout_view, name='logout_view'),
    


]
