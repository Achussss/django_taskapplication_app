from django import forms

from tasks.models import Tasks
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TaskForm(forms.ModelForm):

    class Meta:
        model=Tasks
        fields=["task_name","user"]

class RegistrationForm(UserCreationForm):

    class Meta:
        model=User
        fields=["email","username","password1","password2"]      



class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()          