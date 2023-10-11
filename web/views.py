# Edit web/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
import json
from .forms import ContactForm
from .forms import CheckoutForm
from .models import Blog
from .models import Gallery
from .models import Category
from .models import Product
from cart.cart import Cart
from django.shortcuts import render, redirect
from web.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.db.models import Q
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import send_mail

from django.core.mail import send_mail
import requests
import urllib.parse



def index(request):
    context = {"is_index": True,
               'blog':Blog.objects.all(),
               'category':Category.objects.all(),
               'product':Product.objects.all()}
    return render(request, "web/index.html", context)


def about(request):
    context = {"is_about": True}
    return render(request, "web/about.html", context)

# def product(request):
#     context = {"is_product": True,
#                'product':Product.objects.all(),}
#     return render(request, "web/product.html", context)

def product(request):
    category_id = request.GET.get('category')
    search_query = request.GET.get('search')

    products = Product.objects.all()

    if category_id:
        products = products.filter(category_id=category_id)

    if search_query:
        # Perform a case-insensitive search across product names and descriptions
        products = products.filter(
            Q(product_name__icontains=search_query) | 
            Q(product_description__icontains=search_query)
        )

    categories = Category.objects.all()
    context = {
        "is_product": True,
        'products': products,
        'categories': categories,
    }
    return render(request, "web/product.html", context)


def blog(request):
    context = {"is_blog": True,
               'blog':Blog.objects.all(),}
    return render(request, "web/blog.html", context)

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        messages.success(request,"succsessfully saved")
        return redirect('/contact')
    else:
        context = {
            "is_contact": True,
            "form": form,
        }
    return render(request, "web/contact.html", context)


def blog_detail(request, id):
    blog = Blog.objects.get(id=id)
    context = {'blog': blog}
    return render(request, 'web/blog-detail.html', context)



def gallery(request):
    context = {"is_gallery": True,
               'gallery':Gallery.objects.all(),}
    return render(request, "web/gallery.html", context)


def categories(request,id):
    category = get_object_or_404(Category, id=id)
    
    # Retrieve products that belong to the selected category
    products = Product.objects.filter(category=category)
    
    context = {
        'category': category,
        'products': products,
    }
    
    return render(request,'web/categories.html',context)

def product_detail(request, id):
    product =Product.objects.get(id=id)
    context = {'product': product}
    return render(request, 'web/product-detail.html', context)


def cart(request):
    context = {"is_cart": True}
    return render(request, "web/cart.html", context)

def checkout(request):
    cart = Cart(request)
    total_price = cart.get_total_price()
    form = CheckoutForm(request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            # Save the form data to the Checkout model
            checkout_instance = form.save()

            # Send an email with the form data
            subject = 'Checkout Information'
            message = f'First Name: {checkout_instance.firstname}\n' \
                      f'Last Name: {checkout_instance.lastname}\n' \
                      f'Address: {checkout_instance.address}\n' \
                      f'subaddress: {checkout_instance.subaddress}\n' \
                      f'postcode: {checkout_instance.postcode}\n' \
                      f'country: {checkout_instance.country}\n' \
                      f'state: {checkout_instance.state}\n' \
                      f'town: {checkout_instance.town}\n' \
                      
                    
                    
                      # Add more fields as needed

            from_email = 'asirm0658@gmail.com'  # Sender's email
            recipient_list = ['asirm0658@gmail.com']  # Recipient's email

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            
            whatsapp_api_url = 'https://api.whatsapp.com/send'
            phone_number = '919656949008'
            encoded_message = urllib.parse.quote(message)
            whatsapp_url = f'{whatsapp_api_url}?phone={phone_number}&text={encoded_message}'

            messages.success(request, "Successfully saved")
            return redirect(whatsapp_url)
        else:
            messages.error(request, "Form is not valid")

    context = {
        "is_checkout": True,
        "form": form,
        'total': total_price
    }
    return render(request, "web/checkout.html", context)




# def cart_add(request, id):
#     cart = Cart(request)
#     product = Product.objects.get(id=id)
#     cart.add(product=product)
#     return redirect("/")

def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("/")


def cart_add_qty(request, id,qty):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product,quantity=qty)
    return redirect("/")

def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("web:cart")



def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("web:cart")



def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("web:cart")



def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("web:cart")



def cart_detail(request):
    return render(request, 'web/cart_detail.html')









