from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from .models import *


def index(request):
    products = Product.objects.all()
    categories = Category.objects.all().order_by('name')
    return render(request, 'index.html', context={'products': products, 'categories': categories})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def furniture(request):
    category = Category.objects.all()
    product = Product.objects.all().order_by('name')
    return render(request, 'furniture.html', context={'category': category, 'product': product})

def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all().order_by('name')
    return render(request, 'shop.html', context={'products': products, 'categories': categories})

def testing(request):
    return render(request, 'testing.html')

def base(request):
    return render(request, 'base.html')

def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            print(user)
            if user:
                login(request, user)
                return redirect('index')
    return render(request, 'auth/login.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            print(user)
            if user:
                login(request, user)
                return redirect('index')
            print('no user')
    return render(request, 'auth/register.html', {})

# 1234!@qwert

def log_out(request):
    logout(request)
    return redirect('login')
