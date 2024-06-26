from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["KundeNavn", "TunIP", "MACadd", "Model", "SerieNr", "Image", 
                  "StorageBoxUser", "WarrantyFrom", "GatewayIP", "Noter", 
                  "Journalsystem", "Analyzers", "SIMnr", "company", "CreatedDate", "AbonStart"]
        widgets = {
            'WarrantyFrom': forms.DateInput(attrs={'type': 'text', 'placeholder': 'dd/mm/yyyy'}, format='%d/%m/%Y'),
            'CreatedDate': forms.DateInput(attrs={'type': 'text', 'placeholder': 'dd/mm/yyyy'}, format='%d/%m/%Y'),
            'AbonStart': forms.DateInput(attrs={'type': 'text', 'placeholder': 'dd/mm/yyyy'}, format='%d/%m/%Y'),
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        date_format = '%d/%m/%Y'
        self.fields['WarrantyFrom'].input_formats = (date_format,)
        self.fields['CreatedDate'].input_formats = (date_format,)
        self.fields['AbonStart'].input_formats = (date_format,)



from django.forms import FileField, Form, ModelChoiceField
from .models import Company

class UploadForm(Form):
    company = ModelChoiceField(queryset=Company.objects.all())
    products_file = FileField()


class SearchForm(forms.Form):
    query = forms.CharField(label='Search for Location or MAC', required=False)


from django import forms
from .models import Product, Company

class AddProductForm(forms.ModelForm):
    company = forms.ModelChoiceField(queryset=Company.objects.all(), required=True)

    class Meta:
        model = Product
        fields = ["KundeNavn", "TunIP", "MACadd", "Model", "SerieNr", "Image", "StorageBoxUser", "WarrantyFrom", "GatewayIP", "Noter", "Journalsystem", "Analyzers", "SIMnr", "company", "CreatedDate", "AbonStart"]
        widgets = {
            'WarrantyFrom': forms.DateInput(attrs={'type': 'text', 'placeholder': 'dd/mm/yyyy'}, format='%d/%m/%Y'),
            'CreatedDate': forms.DateInput(attrs={'type': 'text', 'placeholder': 'dd/mm/yyyy'}, format='%d/%m/%Y'),
            'AbonStart': forms.DateInput(attrs={'type': 'text', 'placeholder': 'dd/mm/yyyy'}, format='%d/%m/%Y'),
        }

    def __init__(self, *args, **kwargs):
        super(AddProductForm, self).__init__(*args, **kwargs)
        date_format = '%d/%m/%Y'
        self.fields['WarrantyFrom'].input_formats = [date_format]
        self.fields['CreatedDate'].input_formats = [date_format]
        self.fields['AbonStart'].input_formats = [date_format]



    
from django import forms
from .models import Product, Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name']



