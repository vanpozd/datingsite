from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.forms import ValidationError

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer
from .models import CustomUser
from django.contrib import messages
from . import forms


class UserView(viewsets.ViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        queryset = CustomUser.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            user = CustomUser.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except CustomUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def create(self, request):
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            newuser = form.save()
            return Response({'status': 'user created'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': 'user not created'}, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        try:
            user = CustomUser.objects.get(pk=pk)
            serializer = self.serializer_class(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def update(self, request, pk=None):
        try:
            user = CustomUser.objects.get(pk=pk)
            serializer = self.serializer_class(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def destroy(self, request, pk=None):
        try:
            user = CustomUser.objects.get(pk=pk)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CustomUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


def user_login(request):
    if request.method == "POST":
        form = forms.UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back {username}!')
                return redirect('recommendations')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        if request.user.is_authenticated:
            return redirect('recommendations')
        else:
            form = forms.UserLoginForm()
    return render(request, 'login.html', {'form': form})
        
def user_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out')
    return redirect('login')

def user_register1(request):
    if request.method == "POST":
        form = forms.UserCredentialsForm(request.POST)
        if form.is_valid():
            try:
                form.form_validation()
            except ValidationError as e:
                messages.error(request, str(e)[2:-2])
                return render(request, 'register1.html', {'form': form})
            newuser = form.save()
            login(request, newuser)
            request.session['user_id'] = newuser.id
            return redirect('register2')
        else:
            messages.error(request, 'Invalid input')
    else:
        if request.user.is_authenticated:
            return redirect('recommendations')
        else:
            form = forms.UserCredentialsForm()
    return render(request, 'register1.html', {'form': form})

def user_register2(request):
    user_id = request.session.get('user_id')
    if not user_id:
        messages.error(request, 'Please complete the previous step')
        return redirect('register1')
    user = CustomUser.objects.get(id=user_id)
    if request.method == "POST":
        form = forms.UserNameForm(request.POST, instance=user)
        if form.is_valid():
            form.save(user = user)
            return redirect('register3')
        else:
            messages.error(request, 'Invalid input')
    else:
        form = forms.UserNameForm(instance=user)
    return render(request, 'register2.html', {'form': form})

def user_register3(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('register1')
    user = CustomUser.objects.get(id=user_id)
    if request.method == "POST":
        form = forms.UserPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(user = user)
            messages.success(request, 'Registration complete!')
            return redirect('recommendations')
        else:
            print(form.errors)
            messages.error(request, 'Invalid input')
    else:
        form = forms.UserPhotoForm(instance=user)
    return render(request, 'register3.html', {'form': form})