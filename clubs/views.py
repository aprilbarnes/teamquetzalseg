from django.shortcuts import render
from .forms import SignUpForm

def home (request):
    return render(request,'home.html')

def log_in(request):
    return render(request,'log_in.html')

def sign_up(request):
    form = SignUpForm()
    return render(request,'sign_up.html',{'form':form})
