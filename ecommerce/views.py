from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ecommerce_index_view(request):
    '''This function render index page of ecommerce views'''
    return HttpResponse('Welcome to 6410742347 Chayapat Samapak views?!')

def item_view(request, item_id):
    context_data = {
    "item_id": item_id
    }
    return render(request, 'index.html',context = context_data)

def ecommerce_homepage_view(request):
    return render(request, 'home.html')

def ecommerce_category_view(request):
    return render(request, 'category.html')

def ecommerce_product_view(request):
    return render(request, 'product.html')

def ecommerce_checkout_view(request):
    return render(request, 'checkout.html')

def ecommerce_contact_view(request):
    return render(request, 'contact.html')
