from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    if request.method == "POST":
        userName = request.POST['userName']
        pswd = request.POST['pswd']
        user = authenticate(request, username= userName, password = pswd)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged In")
            return redirect('home')
        else:
            messages.success(request, 'Could not log in please try again...')
            return redirect('home')
         
    return render(request, 'home.html', {})


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    return redirect('home')
