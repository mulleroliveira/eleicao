from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from localflavor.br.forms import BRCPFField

class login(UserCreationForm):
    cpf = BRCPFField(required=True, max_length=11)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ("username", "cpf", "email", "password1", "password2")