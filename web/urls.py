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
    path('product-detail/<int:id>',views.product_detail,name="product-detail"),
    path('cart',views.cart,name="cart"),
    path('checkout',views.checkout,name="checkout"),
   
   
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/add/<int:id>/<int:qty>/', views.cart_add_qty, name='cart_add_qty'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/<int:id>/',views.cart_detail,name='cart_detail'),

    
    
    
    
    
]