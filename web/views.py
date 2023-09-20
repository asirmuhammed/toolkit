# Edit web/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
from .forms import ContactForm
from .models import Blog
from .models import Gallery
from .models import Category

def index(request):
    context = {"is_index": True,
               'blog':Blog.objects.all(),
               'category':Category.objects.all()}
    return render(request, "web/index.html", context)


def about(request):
    context = {"is_about": True}
    return render(request, "web/about.html", context)

def product(request):
    context = {"is_product": True}
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