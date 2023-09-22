# Edit web/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
import json
from .forms import ContactForm
from .models import Blog
from .models import Gallery
from .models import Category
from .models import Product
from django.shortcuts import render, redirect
from web.models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart



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
    products = Product.objects.all()

    if category_id:
        products = products.filter(category_id=category_id)

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
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully updated",
            }
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "Form validation error",
            }
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
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
    context = {"is_checkout": True}
    return render(request, "web/checkout.html", context)








def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("web/index.html")



def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart")



def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")



def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart")



def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart")



def cart_detail(request):
    return render(request, 'web/cart_detail.html')