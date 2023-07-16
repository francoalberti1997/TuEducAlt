from django import forms
from .models import Estudiantes
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(forms.ModelForm):
    class Meta:
        model = Estudiantes
        fields = "__all__"
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"