from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt

from .models import *

def home(request):
    if "login" not in request.session:
        request.session['login'] = 'logout'
    return render(request, "homepage.html")

def reg_process(request):
    if request.method == 'POST':
        errors = User.objects.register_validate(request.POST)

        if len(errors):
            for key, value in errors.items():
                messages.error(request, value, extra_tags = 'register')
            return redirect('/login')
        else: 
            request.session['login'] = 'login'
            p = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            user = User.objects.create(first_name = request.POST['first_name'],
            last_name = request.POST['last_name'], email = request.POST['email'],
            password = p)
            
            messages.success(request, "You have successfully registered!", extra_tags = 'register')

            request.session['id'] = user.id
            return redirect('/login/success')

def log_process(request):
    if request.method == 'POST':
        errors = User.objects.login_validate(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value, extra_tags = 'login')
            return redirect('/login')
        else:
            request.session['login'] = 'login'
            user = User.objects.filter(email = request.POST['email'])[0]
            request.session['id'] = user.id

            messages.success(request, "You are logged in!", extra_tags = 'login')

            return redirect('/login/success')

def success(request):
    if request.session['login'] == 'logout':
        return redirect('/login')
    else: 
        user = User.objects.get(id = request.session['id'])
        info = {
            "u": user
        }
        return render(request, "success.html", info)

def logout(request):
    request.session['login'] = 'logout'
    return redirect('/login')