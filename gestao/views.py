from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home/home.html')
    #if request.user.is_authenticated:
    #    return render(request, 'home/home.html')
    #else:
    #    return redirect("/accounts/login/")