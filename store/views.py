from django.http import JsonResponse
from django.shortcuts import render
from .models import *
import json

def index(request):
    products = Product.objects.all()
    categories = Category.objects.all().order_by('name')
    return render(request, 'index.html',context={'products':products, 'categories':categories})

# def index(request):
#     products = Product.objects.all()
#     categories = Category.objects.all().order_by('name')
#     return render(request, 'index.html',context={'products':products, 'categories':categories})

# def search(request):
#     if request.method=='POST':
#         key = str(request.POST['search'])
#         products = Product.objects.filter(Q(name__contains=key) | Q(category__name__contains=key))
#     return render(request,'search.html',{'products':set(products)})

def product_by(request):
    data = json.loads(request.body)
    print(data['sort'])
    sort = data['sort']
    if sort=='reyting':
        products = Product.objects.all().order_by('-reyting')

    elif sort=='onsale':
        products = Product.objects.filter(quantity__isnull=False)

    pd = [{"id": p.id, "name": p.name, 'image': p.imageURL, 'price': p.price, 'discount': p.with_discount,"category": p.category.name,"reyting": p.reyting} for p in products]

    return JsonResponse({"products":pd})
#
# def product_info(request,id):
#     product = Product.objects.get(id=id)
#     product_like = Product.objects.filter(category__product=product)
#     return render(request, 'product-extended.html', {'product': product,'product_like':product_like})

def category(request,id):
    products_discount = Product.objects.filter(category_id=id,discount__isnull=False)
    products = Product.objects.filter(category_id=id,discount__isnull=True)
    categories = Category.objects.all().order_by('name')
    return render(request, 'category-market.html',{'products':products, 'categories':categories, 'products_discount':products_discount,})


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

