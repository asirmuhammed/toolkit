from django.db import models
from versatileimagefield.fields import VersatileImageField,PPOIField
from tinymce.models import HTMLField

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=120)
    # timestamp = models.DateTimeField(db_index=True,auto_now_add=True)
    email = models.EmailField(blank=True,null=True)
    phone = models.CharField(max_length=120,blank=True,null=True)
    subject = models.CharField(max_length=120,blank=True,null=True)
    message = models.TextField()

    def __str__(self):
        return str(self.name)
    
    
class Blog(models.Model):
    author=models.CharField(max_length=20,)
    title=models.CharField(max_length=225,)
    # date = models.DateField(auto_now=True)
    date = models.DateField()
    image =models.ImageField()
    # ppoi = PPOIField('Image PPOI')
    content= HTMLField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    
class Gallery (models.Model):
    picture=models.ImageField()
    
    
class Category(models.Model):
    category_image=models.ImageField()
    category_title=models.CharField(max_length=30)
    category_product_no=models.CharField(max_length=30)
    
    
    def __str__(self):
        return self.category_title
    


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name=models.CharField(max_length=40)
    product_image=models.ImageField()
    product_price=models.CharField(max_length=30)
    product_del_price=models.CharField(max_length=30)
    product_description=models.TextField()
    
    def __str__(self):
        return self.product_name
    
    
    
    
class Checkout(models.Model):
    firstname=models.CharField(max_length=40)
    lastname=models.CharField(max_length=40)
    address=models.CharField(max_length=250)
    subaddress=models.CharField(max_length=250,blank=True, null=True)
    postcode=models.CharField(max_length=40)
    country=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    town=models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.firstname
    

    
    
    
    
