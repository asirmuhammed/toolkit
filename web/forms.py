# web/forms.py
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Contact
from .models import Checkout
from django.forms import widgets


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ("timestamp",)
        widgets = {
            "name": widgets.TextInput(attrs={"class": "required form-control", "placeholder": "Your Name"}),
            "email": widgets.EmailInput(attrs={"class": "required form-control","placeholder": "Your Email Address",}),
            "phone": widgets.TextInput(attrs={"class": "required form-control", "placeholder": "Your Phone"}),
            "subject": widgets.TextInput(attrs={"class": "required form-control", "placeholder": "Your subject"}),
            "message": widgets.Textarea(attrs={"class": "required form-control","placeholder": "Type Your Message",}),
        }
        
        
        
        
class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        exclude = ("timestamp",)
        widgets = {
            "firstname": widgets.TextInput(attrs={"class": "required form-control", "placeholder": "Your first Name"}),
            "lastname": widgets.TextInput(attrs={"class": "required form-control", "placeholder": "Your Last Name"}),
            "address": widgets.TextInput(attrs={"class": "required form-control","placeholder": "Your Address",}),
            "subaddress": widgets.TextInput(attrs={"class": "required form-control", "placeholder": "Apartment, suite, unit etc. (optional)"}),
            "postcode": widgets.TextInput(attrs={"class": "required form-control", "placeholder": "Your Postcode"}),
            "country": widgets.TextInput(attrs={"class": "required form-control","placeholder": "Type Your country",}),
            "state": widgets.TextInput(attrs={"class": "required form-control","placeholder": "Type Your State",}),
            "town": widgets.TextInput(attrs={"class": "required form-control","placeholder": "Type Your town",}),
            
        }

