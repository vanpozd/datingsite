from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import CustomUser
import re

class UserCredentialsForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    username = forms.CharField(label='Username', max_length=100)

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')

    def form_validation(self):
        password = self.cleaned_data.get('password1')
        confirm_password = self.cleaned_data.get('password2')
        username = self.cleaned_data.get('username')

        if password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        if not re.match(r'^(?=.*[A-Z])(?=.*\d)[A-Za-z\d@#$%^&+=]{8,}$', password):
            raise forms.ValidationError("Password must contain at least 8 characters")
        if not re.match(r'^[a-zA-Z0-9_.+-]{4,}', username):
            raise forms.ValidationError("Invalid username")
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("User with this username already exists")

    def save(self, commit=True):
        user = super(UserCredentialsForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.username = self.cleaned_data['username'] 
        user.is_active = True
        if commit:
            user.save()
        return user

class UserNameForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', max_length=30)
    last_name = forms.CharField(label='Last Name', max_length=30, required=False)
    age = forms.IntegerField(label='Age')
    sex = forms.ChoiceField(label='Sex', choices=[('male', 'Male'), ('female', 'Female')])
    description = forms.CharField(label='Description', required=False)
    hobby = forms.CharField(label='Hobby', max_length=100, required=False)
    main_goal = forms.ChoiceField(label='Main Goal', choices=[('dating', 'Dating'), ('friendship', 'Friendship')])
    inst = forms.CharField(label='Instagram', max_length=100, required=False)
    telegram = forms.CharField(label='Telegram', max_length=100, required=False)
    x_network = forms.CharField(label='X Network', max_length=100, required=False)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'age')

    def save(self, user, commit=True):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.description = self.cleaned_data['description']
        user.age = self.cleaned_data['age']
        user.sex = self.cleaned_data['sex']
        user.hobby = self.cleaned_data['hobby']
        user.main_goal = self.cleaned_data['main_goal']
        user.inst = self.cleaned_data['inst']
        user.telegram = self.cleaned_data['telegram']
        user.x_network = self.cleaned_data['x_network']
        user.liked_list = None
        
        if self.cleaned_data['age'] == None:
            raise forms.ValidationError("Age is required")
        user.save()
        return user

class UserPhotoForm(forms.ModelForm):
    photo1 = forms.ImageField(label='photo1')
    photo2 = forms.ImageField(label='photo2', required=False)
    photo3 = forms.ImageField(label='photo3', required=False)
    photo4 = forms.ImageField(label='photo4', required=False)
    photo5 = forms.ImageField(label='photo5', required=False)
    photo6 = forms.ImageField(label='photo6', required=False)

    class Meta:
        model = CustomUser
        fields = ('photo1', 'photo2', 'photo3', 'photo4', 'photo5', 'photo6')

    def save(self, user, commit=True):
        user.photo1 = self.cleaned_data['photo1']
        user.photo2 = self.cleaned_data['photo2']
        user.photo3 = self.cleaned_data['photo3']
        user.photo4 = self.cleaned_data['photo4']
        user.photo5 = self.cleaned_data['photo5']
        user.photo6 = self.cleaned_data['photo6']
        if commit:
            user.save()
        return user


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        fields = ['username', 'password']
