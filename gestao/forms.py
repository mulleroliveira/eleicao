from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from localflavor.br.forms import BRCPFField

class ExtendsUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","email","first_name","last_name","password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    cpf = BRCPFField(required=True, max_length=11)
    class Meta:
        model = UserProfile
        fields = ("cpf",)