from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Company
from .forms import UploadForm, ProductForm, SearchForm, AddProductForm, CompanyForm
from django.db.models import Q
from django.views.generic.base import View
from csv import DictReader
from io import TextIOWrapper
import csv
from django.contrib.auth.decorators import login_required


from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required(login_url='/login/'), name='dispatch')
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

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Company  # Adjust these imports to match your models
from .forms import SearchForm  # Adjust this import to match your form
from django.db.models import Q

@login_required(login_url='/login/')
def display_data(request):
    # Define your default columns - adjust these to match your actual column names
    default_columns = ['Lokation', 'KundeID', 'MACadd', 'Model', 'SerieNr', 'Navn', 'GatewayIP', 'Noter', 'Journalsystem', 'Analyzers', 'SIMnr', 'Image', 'company']
    
    selected_columns = request.GET.getlist('columns') if 'submitted' in request.GET else default_columns

    companies = Company.objects.all()
    # Your search functionality - adjust as necessary
    query = request.GET.get('query', '')
    if query:
        products = Product.objects.filter(Q(Lokation__icontains=query) | Q(MACadd__icontains=query) | Q(KundeID__icontains=query))
    else:
        products = Product.objects.all()

    # If you have a company filter or similar, adjust this part accordingly
    company_id = request.GET.get('company_id')
    if company_id:
        products = products.filter(company__id=company_id)
        company = get_object_or_404(Company, pk=company_id)
    else:
        company = None

    # Instantiate your search form
    search_form = SearchForm(initial={'query': query})

    
    # Render your template, passing the necessary context
    return render(request, 'display_data.html', {
        'products': products,
        'search_form': search_form,
        'selected_columns': selected_columns,
        'company': company, 
        'companies': companies, # If you're using a company filter
        # Add any other context variables you need
    })

# Add any other views you have here


"""@login_required(login_url='/login/') 
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
        products = products.filter(Q(Lokation__icontains=query) | Q(MACadd__icontains=query) | Q(KundeID__icontains=query))

    companies = Company.objects.all()
    search_form = SearchForm(initial={'query': query})  # Initialize the form with the search query

    return render(request, 'display_data.html', {'products': products, 'search_form': search_form, 'companies': companies, 'company_id': company_id, 'company': company})
"""
@login_required(login_url='/login/') 
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


from .decorators import user_type_required  # Assuming the decorator is in a file called decorators.py

@user_type_required('ADMIN')
def delete_product(request, company_id, product_id):
    product = get_object_or_404(Product, pk=product_id)
    company = get_object_or_404(Company, pk=company_id)

    if request.method == 'POST':
        product.delete()       
        return redirect('display_data') 

    return render(request, 'delete_product.html', {'product': product, 'company': company})

@login_required(login_url='/login/') 
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

@login_required(login_url='/login/') 
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

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('display_data')
        else:
            return HttpResponse("Invalid login credentials")
    else:
        return render(request, 'login.html')

from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    return redirect('user_login')
