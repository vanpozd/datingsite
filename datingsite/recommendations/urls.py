from django.urls import path
from . import views

urlpatterns = [
    path('', views.recom, name='recommendations'),
    path('handle_action/', views.handle_action, name='handle_action'),
]
