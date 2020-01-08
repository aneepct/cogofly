from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('social_api_callback', views.social_api_callback, name='social_api_callback'),
    path('login_view', views.login_view, name='login_view'),
    path('register_view', views.register_view, name='register_view'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout_view, name="logout"),
    path('home', views.home, name="home"),
    path('city_search', views.city_search, name="city_search"),
]
