from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image', 'description']

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username']
