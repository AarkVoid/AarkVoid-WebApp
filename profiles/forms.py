from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django.core.validators import ValidationError

from resources.utils import getProfile
from .models import User_OTP

# Register Form
class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password ( Length must be more than 10 characters )'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
        # data from the form is fetched using super function
        cleaned_data = super().clean()

        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        # Check Password Length
        if len(password1) <= 8:
            raise ValidationError({'password2': 'Password length must be more than 8 characters'})

        # Check if Passwords are matching or not        
        if password1 != password2:
            raise ValidationError({'password2': 'Password Does Not Match.'})

        if User.objects.filter(username=cleaned_data.get('username').lower()).exists():
            raise ValidationError({'username': 'User with this username already exists.'})

        if User.objects.filter(email=cleaned_data.get('email').lower()).exists():
            raise ValidationError({'email': 'User with this email already exists.'})

        return cleaned_data

    # Form Save Method
    def save(self):
        data = self.cleaned_data
        instance = super(UserCreationForm, self).save(commit=False)
        instance.set_password(self.cleaned_data["password1"])
        instance.username = data.get('username').lower()
        instance.is_active = False
        instance.save()
        return instance

# Login Form
class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        # data from the form is fetched using super function
        cleaned_data = super().clean()

        # Check is user is exists or not
        if not User.objects.filter(username=cleaned_data.get('username').lower()).exists():
            raise ValidationError('User with this username does not exists.')

        return cleaned_data