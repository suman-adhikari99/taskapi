from typing import Text
from django import forms
from django.db import models
from django.db.models import fields
from .models import Register
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
        Email = forms.EmailField(widget=forms.TextInput(attrs = { 'type':'email'} ))
        Password = forms.CharField(widget=forms.TextInput(attrs = { 'type':'password'} ))
        FirstName = forms.EmailField(widget=forms.TextInput(attrs = { 'type':'text' }))
        LastName = forms.EmailField(widget=forms.TextInput(attrs = { 'type':'text'} ))

        class Meta:
            model=Register
            fields=("Email", "Password","FirstName", "LastName")
        

