from django.urls import path
from . import views

urlpatterns = [
    path('', views.userprofile, name='profile'),
    path('edit/', views.editprofile, name='editprofile'),
    path('delete_image/<int:image_id>', views.delete_image, name='delete_image'),
    path('upload_image/', views.upload_image, name='upload_image'),
]
