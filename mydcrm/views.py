from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record
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
    
    records = Record.objects.all()
    context = {
        'records':records
    }
    return render(request, 'home.html', context) 
    return render(request, 'home.html', {})



def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "you have successfully registered")
            return redirect('home')
    else:
        form = SignUpForm()         
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('home')

def view_record(request, pk):
    if request.user.is_authenticated:
        obj = Record.objects.get(id=pk)
        return render(request, 'record.html',{'record': obj})
    else:
        messages.success(request, "You nust be logged in to view the page")
        return(redirect('home'))
def delete_record(request, pk):
    if request.user.is_authenticated:
        obj = Record.objects.get(id=pk)
        obj.delete()
    return redirect('home')
