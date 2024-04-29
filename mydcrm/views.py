from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecord
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


def add_record(request):
    form = AddRecord(request.POST or None)
    if request.user.is_authenticated:
        if request.method =='POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Great job! You have added new record...")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in...")


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecord(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Great job, the form is updated...")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in...")


        



#this is so much worl for nothing 
            # first_name=form.cleaned_data['first_name']
            # last_name=form.cleaned_data['last_name']
            # phone=form.cleaned_data['phone']
            # email=form.cleaned_data['email']
            # city=form.cleaned_data['city']
            # address=form.cleaned_data['address']
            # zipcode=form.cleaned_data['zipcode']
            # state=form.cleaned_data['state']
            # user_record = Record(first_name=first_name,last_name=last_name,phone=phone,email=email,city=city,address=address,zipcode=zipcode,state=state)
            # user_record.save()
