from django.shortcuts import render, redirect
from . forms import ExtendsUserCreationForm, UserProfileForm
from django.http import HttpResponse
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        form = ExtendsUserCreationForm(request.POST)
        form2 = UserProfileForm(request.POST)
        if form.is_valid() and form2.is_valid():
            user = form.save()
            profile = form2.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('/accounts/login/')
        else:
            return render(request, 'registration/register.html', {"form":form, "form2":form2})
    else:
        form = ExtendsUserCreationForm()
        form2 = UserProfileForm()
        return render(request, 'registration/register.html', {"form":form, "form2":form2})

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home/home.html')
    else:
        return redirect("/accounts/login/")