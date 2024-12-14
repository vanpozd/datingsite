from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from authentication.views import UserView
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('user', UserView)

urlpatterns = [
    path('auth/', include('authentication.urls')),
    path('', include('recommendations.urls')),
	path('profile/', include('profiles.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
