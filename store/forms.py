from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.forms import User
from django.db import models

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","email", "password1", "password2")

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=22)
    password = forms.CharField(widget=forms.PasswordInput())