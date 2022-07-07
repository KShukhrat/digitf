from django.shortcuts import render

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

