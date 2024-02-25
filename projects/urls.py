from django.urls import path
from . import views
urlpatterns=[
  path('main/', views.main, name="main"),
  path('navbar/', views.navbar, name="navbar"),
  path('dashboard/', views.dashboard, name="dashboard"),
  path('loginpage/', views.loginpage, name="login"),
  path('register/', views.registerpage, name="register") ,
  path('logout/', views.logoutpage, name='logout'),
  path('add_event/', views.add_event, name='add_event'),
  path('admin_dash/', views.admin_dash, name='admin_dash'),
  path('show_events/', views.show_events, name='show_events'),
  path('approved_events/', views.approved_events, name='approved_events'),
  path('student_dash/', views.student_dash, name='student_dash'),
  path('approve/', views.approve, name='approve'),
]