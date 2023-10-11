from django.forms import FileField, Form, ModelForm
from .models import Product
from django import forms


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["Lokation", "KundeID", "MACadd", "Model", "SerieNr", "Navn", "Image", "GatewayIP", "Noter", "Journalsystem", "Analyzers", "SIMnr"]


from django.forms import FileField, Form
from django import forms
from .models import Company

from django.forms import FileField, Form, ModelChoiceField
from .models import Company

class UploadForm(Form):
    company = ModelChoiceField(queryset=Company.objects.all())
    products_file = FileField()





class SearchForm(forms.Form):
    query = forms.CharField(label='Search for Location or MAC', required=False)


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["Lokation", "KundeID", "MACadd", "Model", "SerieNr", "Navn", "Image", "GatewayIP", "Noter", "Journalsystem", "Analyzers", "SIMnr", "company"]

    
from django import forms
from .models import Product, Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name']



