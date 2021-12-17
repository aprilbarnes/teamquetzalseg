from django.shortcuts import render
from .forms import SignUpForm
from .forms import LogInForm

def home (request):
    return render(request,'home.html')

def log_in(request):
    form = LogInForm()
    return render(request,'log_in.html',{'form':form})

def sign_up(request):
    form = SignUpForm()
    return render(request,'sign_up.html',{'form':form})
