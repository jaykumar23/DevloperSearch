from django import views
from django.urls import path
from . import views
urlpatterns = [

    path('login/',views.loginUser, name='login'),
    path('register/',views.registerUser, name='register'),
    path('logout/',views.logoutUser, name='logout'),
    path('', views.profiles, name="profiles"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    
]