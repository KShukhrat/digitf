from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout

from .models import Product


def index(request):
    return render(request,'index.html')

def search(request):
    if request.method=='POST':
        key = str(request.POST['search'])
        products = Product.objects.filter(Q(name__contains=key) | Q(category__name__contains=key))
    return render(request,'search.html',{'products':set(products)})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def furniture(request):
    return render(request, 'furniture.html')

def shop(request):
    return render(request, 'shop.html')

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
