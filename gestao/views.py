from django.shortcuts import render, redirect
from . forms import ExtendsUserCreationForm, UserProfileForm
from . models import UserProfile
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required


def register(request):
    if request.method == "POST":
        form = ExtendsUserCreationForm(request.POST)
        form2 = UserProfileForm(request.POST)
        if form.is_valid() and form2.is_valid():
            user = form.save()
            profile = form2.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, "A sua conta foi criada com sucesso.")
            return redirect('/accounts/login/')
        else:
            return render(request, 'registration/register.html', {"form":form, "form2":form2})
    else:
        form = ExtendsUserCreationForm()
        form2 = UserProfileForm()
        return render(request, 'registration/register.html', {"form":form, "form2":form2})

#@login_required
#@gestao.add_book('')
@login_required
def home(request):
    return render(request, 'home/home.html')

@login_required
def perfil(request):
    id = request.user.id
    usuario = User.objects.all().get(id=id)
    usuariocpf = UserProfile.objects.all()
    return render(request, 'usuario/perfil.html', {"usuario":usuario, "usuariocpf":usuariocpf})