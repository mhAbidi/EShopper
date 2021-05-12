from django import forms
from adminpanel.models import *


class Product_Form(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'sku', 'short_description', 'long_description', 'price',
            'special_price', 'quantity', 'meta_title', 'meta_description', 'meta_keywords'

        ]


class User_Form(forms.ModelForm):
    class Meta:
        model = Users
        fields = [
            'firstname', 'lastname', 'email', 'password'
        ]
        widgets = {
            "password": forms.PasswordInput(),
        }

