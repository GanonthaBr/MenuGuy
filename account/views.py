from django import forms

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

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
    def get(self,request):
        return render(request, 'login.html')
    
    def post(self,request):
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(request, phone=phone,password=password)
        if user:
            login(request,user)
            request.session.set_expiry(7776000)
            return redirect('home')
        return render(request, 'login.html')

class LogoutView(View):
    pass

