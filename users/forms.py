from django.db import models
from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password
from users.models import Profile


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите имя юзера'
    }))

    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите email'
    }))

    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите пароль'
    }))
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Подтвердите пароль'
    }))

    birth_date = forms.DateTimeField(label='Дата рождения', widget=forms.DateTimeInput(attrs={
        'class': 'form-control',
        'placeholder': 'Дата рождения'
    }))

    phone = forms.IntegerField(label='Номер телефона', widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Номер телефона'
    }))

    class Meta:
        model = Profile
        fields = ('phone', )