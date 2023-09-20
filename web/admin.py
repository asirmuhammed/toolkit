from django.contrib import admin
from .models import Contact
from .models import Blog
from .models import Gallery
from .models import Category
from .models import Product

# Register your models here.
admin.site.register(Contact)
admin.site.register(Blog)
admin.site.register(Gallery)
admin.site.register(Category)
admin.site.register(Product)