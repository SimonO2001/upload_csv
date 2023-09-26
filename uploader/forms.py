# shop/forms.py

from django.forms import FileField, Form, ModelForm
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["Lokation", "KundeID", "MACadd", "Model", "SerieNr", "Navn", "Image", "GatewayIP", "Noter", "Journalsystem", "Analyzers", "SIMnr"]


class UploadForm(Form):
    products_file = FileField()