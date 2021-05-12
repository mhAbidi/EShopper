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
            'firstname', 'lastname', 'email',
            'password', 'status', 'is_staff'

        ]


class products(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    sku = forms.CharField(label='SKU', max_length=45)
    short_description = forms.CharField(label='Short Description', max_length=100)
    long_description = forms.CharField(label='Long Desription', widget=forms.Textarea(attrs={"rows": 5, "cols": 20}))
    price = forms.FloatField(label='Price')
    special_price = forms.FloatField(label='Special Price')
    quantity = forms.IntegerField(label='Quantity')
    meta_title = forms.CharField(label='Meta Title', max_length=45)
    meta_description = forms.CharField(label='meta_description', widget=forms.Textarea(attrs={"rows": 5, "cols": 20}))
    meta_keywords = forms.CharField(label='meta_keywords', widget=forms.Textarea(attrs={"rows": 5, "cols": 20}))


class users(forms.Form):
    firstname = forms.CharField(label='First Name', max_length=45)
    lastname = forms.CharField(label='Last Name', max_length=45)
    email = forms.CharField(label='Email', max_length=45)
    password = forms.CharField(label='Password', max_length=45)
    password2 = forms.CharField(label='Re-Enter', max_length=45)


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name ::', max_length=100)
