from django.db.models import fields
from django.forms import ModelForm
from .models import Order
from django.contrib.auth.models import User
from django import forms


class orderform(ModelForm):

    class Meta:
        model = Order
        fields=['file', 'fileurl', 'pages', 'notes', 'price' ]       
        

class usersignupform(ModelForm):
    class Meta:
        model=User
        fields=['email', 'username', 'password', 'first_name', 'last_name']
        widgets={'password': forms.PasswordInput()}
        





        
