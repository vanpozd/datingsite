from django.shortcuts import render,redirect

# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework import status

# from .serializers import UserSerializer
# from .models import CustomUser
from django.contrib import messages
# from . import forms

def recom(request):
	if request.user.is_authenticated:
		return render(request, 'recommendations.html')
	else:
		return redirect('login')