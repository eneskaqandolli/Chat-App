from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

from .models import Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
       widget=forms.EmailInput(attrs={
            'class': 'border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Enter your email'
        })
    )
    
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Enter your username'
        })
    )
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Enter your password'
        })
    )
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Confirm your password'
        })
    )
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["username", "image"]