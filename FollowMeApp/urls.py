from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('login_view' , views.login_view, name='login_view'),
    path('logout' , views.logout_view, name='logout_view'),
    path('register' , views.register_view, name='registers_view'),
    path('mainPage', views.mainPage, name='mainPage'),

]