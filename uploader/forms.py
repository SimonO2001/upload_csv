# shop/forms.py

from django.forms import FileField, Form, ModelForm
from .models import Product
from django import forms


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["Lokation", "KundeID", "MACadd", "Model", "SerieNr", "Navn", "Image", "GatewayIP", "Noter", "Journalsystem", "Analyzers", "SIMnr"]


class UploadForm(Form):
    products_file = FileField()



class SearchForm(forms.Form):
    query = forms.CharField(label='Search for Location or MAC', required=False)


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["Lokation", "KundeID", "MACadd", "Model", "SerieNr", "Navn", "Image", "GatewayIP", "Noter", "Journalsystem", "Analyzers", "SIMnr"]

    

