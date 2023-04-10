from django import forms
from .models import Product, Order
from django.contrib.auth.models import Group
from django.forms import ModelForm


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "name", "price", "description", "discount", "preview"

    images = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
    )


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "user", "delivery_address", "promocode", "products"


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = "name",
