from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id','username', 'first_name', 'last_name', 'created_at', 'updated_at']
    list_filter = ['reported']

    class Meta:
        model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)