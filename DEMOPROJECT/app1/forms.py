from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    Email = forms.EmailField()
    # Type = forms.CharField()


class Meta:
    model = User
    fields = ['username', 'Email', 'password1', 'password2']
