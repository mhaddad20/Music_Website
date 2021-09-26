from django.shortcuts import render, redirect

# Create your views here.
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def new_product(request):
    return render(request, 'new_product.html')

def accessories(request):
    return render(request, 'accessories.html')

def merchandise(request):
    return render(request, 'merchandise.html')

def vouchers(request):
    return render(request, 'vouchers.html')

def repairs(request):
    return render(request, 'repairs.html')