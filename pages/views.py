from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, "base.html")

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')
   
def sale(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    
    return render(
        request,
        'pages/sale.html',
        context
    )

def repairs(request):
    return render(request, 'pages/repairs.html')

