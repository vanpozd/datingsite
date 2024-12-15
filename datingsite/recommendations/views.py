from django.shortcuts import render,redirect

# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework import status

# from .serializers import UserSerializer
# from .models import CustomUser
from django.contrib import messages
from authentication.models import CustomUser
# from . import forms

def recom(request):
	user = request.user
	if request.user.is_authenticated:
		users = CustomUser.objects.exclude(id=request.user.id).filter(age__gte=user.age-2, age__lte=user.age+2)
		return render(request, 'recommendations.html', {'recom_users': users})
	else:
		return redirect('login')