from django.urls import path
from . import views

urlpatterns = [
    path('', views.recom, name='recommendations'),
]
