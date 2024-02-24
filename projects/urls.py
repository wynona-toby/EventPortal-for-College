from django.urls import path
from . import views
urlpatterns=[
  path('main/', views.main, name="main"),
  path('navbar/', views.navbar, name="navbar"),
  path('dashboard/', views.dashboard, name="dashboard"),
  path('loginpage/', views.loginpage, name="login"),
  path('register/', views.registerpage, name="register") ,
]
