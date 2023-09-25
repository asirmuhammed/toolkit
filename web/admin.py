from django.contrib import admin
from .models import Contact
from .models import Blog
from .models import Gallery
from .models import Category
from .models import Product
from .models import Checkout

# Register your models here.
admin.site.register(Contact)
admin.site.register(Blog)
admin.site.register(Gallery)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Checkout)