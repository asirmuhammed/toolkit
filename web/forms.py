# web/forms.py
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Contact
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

