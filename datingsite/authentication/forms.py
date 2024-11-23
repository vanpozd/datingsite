from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import CustomUser

class UserCredentialsForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    username = forms.CharField(label='Email', max_length=100)

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password1')
        confirm_password = self.cleaned_data.get('password2')

        if password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return confirm_password

    def save(self, commit=True):
        user = super(UserCredentialsForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.email = self.cleaned_data['username']
        if commit:
            user.save()
        return user

class UserNameForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', max_length=30)
    last_name = forms.CharField(label='Last Name', max_length=30)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name')

    def save(self, user, commit=True):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

class UserPhotoForm(forms.ModelForm):
    photo1 = forms.ImageField(label='Photo1')
    photo2 = forms.ImageField(label='Photo2')
    photo3 = forms.ImageField(label='Photo3')

    class Meta:
        model = CustomUser
        fields = ('photo1', 'photo2', 'photo3')

    def save(self, commit=True):
        user = super(UserPhotoForm, self).save(commit=False)
        # Добавьте любую дополнительную логику здесь
        if commit:
            user.save()
        return user


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        fields = ['username', 'password']
