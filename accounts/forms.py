from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from django.forms import ModelForm
from .models import Person

from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

    class Meta:
        model=User
        fields=['username','email','password1','password2']



class PersonForm(ModelForm):
        class Meta:
            model=Person
            fields='__all__'
               