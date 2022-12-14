from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    first_name = forms.CharField(label = 'Etunimi')
    last_name = forms.CharField(label = 'Sukunimi')
    email = forms.EmailField(label = 'Sähköposti')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
