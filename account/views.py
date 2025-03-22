from django import forms

from django.shortcuts import render, redirect
from django.contrib.auth import login

from django.views.generic import ListView, View
from .forms import UserForm

# Create your views here.

class SignupView(View):
    def get(self,request):
        form = UserForm()
        return render(request, 'signup.html', {'form': form})
    
    def post(self,request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
        return render(request, 'signup.html', {'form': form})

class LoginView(View):
    pass

class LogoutView(View):
    pass

