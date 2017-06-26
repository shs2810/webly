from django.db import models
from django import forms

class LoginForm(forms.Form):
    year = forms.DateField()
    month = forms.DateField()
    sex = forms.CharField()

