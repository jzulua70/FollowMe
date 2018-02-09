from django.urls import path

from . import views
import FollowMeApp


urlpatterns = [
    path('map', views.map, name='map'),
    path('getPosition', views.getPosition, name='getPosition'),
    path('getData',  views.getData, name='getData'),
    path('index2', views.index2, name='index2'),


]