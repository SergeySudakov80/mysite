from django import forms
from .models import Product, Order
from django.forms import ModelForm
from django.contrib.auth.models import Group

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = 'name',


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = 'name', 'price', 'description', 'discount'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = 'delivery_adress', 'promocode', 'user', 'products'
