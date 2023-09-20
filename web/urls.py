# Create web/urls.py and paste the following
from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("about",views.about,name="about"),
    path("product",views.product,name="product"),
    path("blog",views.blog,name="blog"),
    path("contact",views.contact,name="contact"),
    path('blog/<int:id>/', views.blog_detail, name='blog_detail'),
    path('gallery',views.gallery,name="gallery"),
    path("categories/<int:id>", views.categories, name="categories"),
    # path('product-detail/<int:id>',views.product_detail,name="product-detail"),
    path('product-detail',views.product_detail,name="product-detail")
    
    
]