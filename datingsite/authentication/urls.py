from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register1/', views.user_register1, name='register1'),
    path('register2/', views.user_register2, name='register2'),
    path('register3/', views.user_register3, name='register3'),
]
