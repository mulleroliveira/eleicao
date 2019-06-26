from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')
        else:
            return render(request, 'registration/register.html', {"form":form})
    else:
        form = UserCreationForm()
        return render(request, 'registration/register.html', {"form":form})

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home/home.html')
    else:
        return redirect("/accounts/login/")