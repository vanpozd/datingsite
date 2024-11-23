from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from authentication.views import UserView

router = routers.DefaultRouter()
router.register('user', UserView)

urlpatterns = [
    path('auth/', include('authentication.urls')),
    path('', include('recommendations.urls')),
	path('profile/', include('profiles.urls')),
    path('admin/', admin.site.urls),
]
