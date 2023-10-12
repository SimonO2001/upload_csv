from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Company
from .forms import UploadForm, ProductForm, SearchForm, AddProductForm, CompanyForm
from django.db.models import Q
from django.views.generic.base import View
from csv import DictReader
from io import TextIOWrapper
import csv

class UploadView(View):
    template_name = 'upload.html'

    def get(self, request, *args, **kwargs):
        form = UploadForm()
        companies = Company.objects.all()
        return render(request, self.template_name, {'form': form, 'companies': companies})

    def post(self, request, *args, **kwargs):
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            company_id = request.POST.get('company')

            company = get_object_or_404(Company, pk=company_id)

            products_file = request.FILES.get("products_file")
            csv_data = TextIOWrapper(products_file, encoding="utf-8", newline="")
            reader = csv.DictReader(csv_data)

            for row in reader:
                product = Product(
                    Lokation=row['Lokation'],
                    KundeID=row['KundeID'],
                    MACadd=row['MACadd'],
                    Model=row['Model'],
                    SerieNr=row['SerieNr'],
                    Navn=row['Navn'],
                    GatewayIP=row['GatewayIP'],
                    Noter=row['Noter'],
                    Journalsystem=row['Journalsystem'],
                    Analyzers=row['Analyzers'],
                    SIMnr=row['SIMnr'],
                    Image=row['Image'],
                    company=company
                )
                product.save()

            return redirect('display_data')

        return render(request, self.template_name, {'form': form})

def display_data(request):
    company_id = request.GET.get('company_id')
    query = request.GET.get('query', '')

    if company_id:
        products = Product.objects.filter(company_id=company_id)
        company = get_object_or_404(Company, pk=company_id)
    else:
        products = Product.objects.all()
        company = None

    if query:
        products = products.filter(Q(Lokation__icontains=query) | Q(MACadd__icontains=query))

    companies = Company.objects.all()
    search_form = SearchForm(initial={'query': query})  # Initialize the form with the search query

    return render(request, 'display_data.html', {'products': products, 'search_form': search_form, 'companies': companies, 'company_id': company_id, 'company': company})






def edit_product(request, company_id, product_id):
    company = get_object_or_404(Company, pk=company_id)
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('display_data')
    else:
        form = ProductForm(instance=product)

    return render(request, 'edit_product.html', {'form': form})

def delete_product(request, company_id, product_id):
    product = get_object_or_404(Product, pk=product_id)
    company = get_object_or_404(Company, pk=company_id)

    if request.method == 'POST':
        product.delete()       
        return redirect('display_data')  # Redirect to display_data without specifying company_id

    return render(request, 'delete_product.html', {'product': product, 'company': company})


def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            company_id = request.POST.get('company')  # Get the selected company ID from the form
            company = get_object_or_404(Company, pk=company_id)  # Retrieve the company object
            product = form.save(commit=False)
            product.company = company  # Assign the product to the selected company
            product.save()
            return redirect('display_data')
    else:
        form = AddProductForm()

    companies = Company.objects.all()
    return render(request, 'add_product.html', {'form': form, 'companies': companies})

def copy_and_edit_data(request, company_id, product_id):
    original_product = get_object_or_404(Product, pk=product_id)

    # Create a new instance of the Product model for the copied product
    copied_product = Product(
        Lokation=original_product.Lokation + '-copy',
        KundeID=original_product.KundeID,
        MACadd=original_product.MACadd,
        Model=original_product.Model,
        SerieNr=original_product.SerieNr,
        Navn=original_product.Navn,
        GatewayIP=original_product.GatewayIP,
        Noter=original_product.Noter,
        Journalsystem=original_product.Journalsystem,
        Analyzers=original_product.Analyzers,
        SIMnr=original_product.SIMnr,
        Image=original_product.Image,
        company=original_product.company  # Assign the same company to the copied product
    )

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=copied_product)
        if form.is_valid():
            form.save()
            return redirect('display_data')
    else:
        form = ProductForm(instance=copied_product)

    return render(request, 'copy_and_edit.html', {'form': form, 'company': copied_product.company})


def select_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save()
            return redirect('display_data', company_id=company.id)
    else:
        form = CompanyForm()
    companies = Company.objects.all()
    return render(request, 'select_company.html', {'form': form, 'companies': companies})
