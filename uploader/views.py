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
                    KundeNavn=row['KundeNavn'],
                    TunIP=row['TunIP'],
                    MACadd=row['MACadd'],
                    Model=row['Model'],
                    SerieNr=row['SerieNr'],
                    CreatedDate=row['CreatedDate'],
                    GatewayIP=row['GatewayIP'],
                    Noter=row['Noter'],
                    Journalsystem=row['Journalsystem'],
                    Analyzers=row['Analyzers'],
                    SIMnr=row['SIMnr'],
                    Image=row['Image'],
                    StorageBoxUser=row['StorageBoxUser'],
                    WarrantyFrom=row['WarrantyFrom'],
                    company=company,
                    AbonStart=row['AbonStart']
                )
                product.save()

            return redirect('display_data')

        return render(request, self.template_name, {'form': form})

from django.shortcuts import render, get_object_or_404
from .models import Product, Company  # Adjust these imports to match your models
from .forms import SearchForm  # Adjust this import to match your form
from django.db.models import Q


from django.shortcuts import render, get_object_or_404
from .models import Product, Company
from .forms import SearchForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from .models import Product, Company  # Justér dette til dine faktiske import-stier
from django.db.models import Q
from django.http import JsonResponse
from django.template.loader import render_to_string



from django.shortcuts import render, get_object_or_404
from .models import Product, Company
from .forms import SearchForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string

from django.shortcuts import render, get_object_or_404
from .models import Product, Company
from .forms import SearchForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string

@login_required(login_url='/login/')
def display_data(request):
    default_columns = ['KundeNavn', 'TunIP', 'MACadd', 'Model', 'SerieNr', 'GatewayIP', 'Noter', 'Journalsystem', 'Analyzers', 'Image', 'StorageBoxUser', 'WarrantyFrom', 'CreatedDate', "AbonStart"]
    
    if 'submitted' in request.GET or request.headers.get('x-requested-with') == 'XMLHttpRequest':
        selected_columns = request.GET.getlist('columns')
    else:
        selected_columns = default_columns
    
    company_id = request.GET.get('company_id')
    if company_id in COMPANY_COLUMNS:
        selected_columns = COMPANY_COLUMNS[company_id]  # Get company-specific columns
    else:
        selected_columns = default_columns  # Fallback to default columns
    
    sortable_columns = ['KundeNavn', 'CreatedDate', 'AbonStart']
    products = Product.objects.all()
    companies = Company.objects.all()
    products_count = products.count()
    
    query = request.GET.get('query', '')
    if query:
        products = products.filter(
            Q(KundeNavn__icontains=query) | 
            Q(TunIP__icontains=query) |
            Q(MACadd__icontains=query) |
            Q(Model__icontains=query) |
            Q(SerieNr__icontains=query) |
            Q(GatewayIP__icontains=query) |
            Q(Noter__icontains=query) |
            Q(Journalsystem__icontains=query) |
            Q(Analyzers__icontains=query) |
            Q(SIMnr__icontains=query) |
            Q(Image__icontains=query) |
            Q(StorageBoxUser__icontains=query) |
            Q(WarrantyFrom__icontains=query) |
            Q(company__name__icontains=query) |
            Q(CreatedDate__icontains=query) |
            Q(AbonStart__icontains=query)
        )
    
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('products_table.html', {
            'products': products,
            'selected_columns': selected_columns,
            'sortable_columns': sortable_columns,
        }, request=request)
        return JsonResponse({'html': html})
    
    search_form = SearchForm(initial={'query': query})
    return render(request, 'display_data.html', {
        'products': products,
        'search_form': search_form,
        'selected_columns': selected_columns,
        'sortable_columns': sortable_columns,
        'companies': companies,
        'default_columns': default_columns,
        'products_count': products_count,
    })



from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Product
from django.shortcuts import get_object_or_404
from django.db.models import Q

from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Product, Company
from django.db.models import Q

from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Product
from django.db.models import Q

def fetch_products(request):
    query = request.GET.get('query', '')
    company_id = request.GET.get('company_id')
    selected_columns = request.GET.getlist('columns', [])  # Adjusted to use getlist to fetch columns

    products = Product.objects.all()

    # Filter by company ID if provided
    if company_id and company_id.isdigit():
        products = products.filter(company_id=company_id)

    # Apply query filters if a query is provided
    if query:
        products = products.filter(
            Q(KundeNavn__icontains=query) |
            Q(TunIP__icontains=query) |
            Q(MACadd__icontains=query) |
            Q(Model__icontains=query) |
            Q(SerieNr__icontains=query) |
            Q(GatewayIP__icontains=query) |
            Q(Noter__icontains=query) |
            Q(Journalsystem__icontains=query) |
            Q(Analyzers__icontains=query) |
            Q(SIMnr__icontains=query) |
            Q(Image__icontains=query) |
            Q(StorageBoxUser__icontains=query) |
            Q(WarrantyFrom__icontains=query) |
            Q(company__name__icontains=query) |
            Q(CreatedDate__icontains=query) |
            Q(AbonStart__icontains=query)
        )
    
    company_id = request.GET.get('company_id')
    if company_id and str(company_id) in COMPANY_COLUMNS:
        selected_columns = COMPANY_COLUMNS[str(company_id)]
    else:
        selected_columns = ['KundeNavn', 'TunIP', 'MACadd', 'Model', 'SerieNr', 'GatewayIP', 'Noter', 'Journalsystem', 'Analyzers', 'Image', 'StorageBoxUser', 'WarrantyFrom', 'CreatedDate', "AbonStart"]

    # Make sure to pass 'selected_columns' to your template for rendering
    
    products_count = products.count()  # Get the count of products

    # Render the products table HTML
    html = render_to_string('products_table.html', {
        'products': products,
        'selected_columns': selected_columns,
    }, request=request)

    return JsonResponse({'html': html, 'products_count': products_count})





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
    # Make sure 'companies' is correctly passed to your template context
    return render(request, 'add_product.html', {'form': form, 'companies': companies})





@login_required(login_url='/login/') 
def copy_and_edit_data(request, company_id, product_id):
    original_product = get_object_or_404(Product, pk=product_id)

    # Check if KundeNavn is None and handle it accordingly
    kundeNavn_copy = (original_product.KundeNavn + '-copy') if original_product.KundeNavn else 'Unknown-copy'

    # Create a new instance of the Product model for the copied product
    copied_product = Product(
        KundeNavn=kundeNavn_copy,
        TunIP=original_product.TunIP,
        MACadd=original_product.MACadd,
        Model=original_product.Model,
        SerieNr=original_product.SerieNr,
        GatewayIP=original_product.GatewayIP,
        Noter=original_product.Noter,
        Journalsystem=original_product.Journalsystem,
        Analyzers=original_product.Analyzers,
        SIMnr=original_product.SIMnr,
        Image=original_product.Image,
        StorageBoxUser=original_product.StorageBoxUser,
        WarrantyFrom=original_product.WarrantyFrom,
        company=original_product.company,
        CreatedDate=original_product.CreatedDate,
        AbonStart=original_product.AbonStart 
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


# import logging

# logger = logging.getLogger(__name__)
# def update_columns(request):
#     # Assuming you're sending the columns as a comma-separated string
#     selected_columns = request.GET.get('columns', '')
#     selected_columns_list = selected_columns.split(',') if selected_columns else []

#     # Your logic to fetch products based on selected columns
#     # Assuming you have a function or logic to filter products based on these columns
#     products = fetch_products_based_on_columns(selected_columns_list)
#     logger.info(f"update_columns view hit with URL: {request.get_full_path()}")
#     # Render your table or data partial with the filtered products
#     html = render_to_string('products_table.html', {'products': products, 'selected_columns': selected_columns_list}, request=request)
#     return JsonResponse({'html': html})


COMPANY_COLUMNS = {
    '7': ['KundeNavn', 'TunIP', 'MACadd', 'Model', 'SerieNr', 'GatewayIP', 'Noter', 'Journalsystem', 'Analyzers', 'SIMnr', 'Image', 'WarrantyFrom', 'StorageBoxUser', 'CreatedDate', 'AbonStart',],  
    '6': ['KundeNavn', 'TunIP', 'MACadd', 'SerieNr', 'GatewayIP', 'Noter', 'WarrantyFrom', 'Analyzers', 'StorageBoxUser',],  # Signdesk
    '5': ['KundeNavn', 'TunIP', 'MACadd', 'SerieNr', 'GatewayIP', 'Noter', 'WarrantyFrom', 'Analyzers', 'StorageBoxUser',],  # Lifetest
    '4': ['KundeNavn', 'TunIP', 'MACadd', 'SerieNr', 'GatewayIP', 'Noter', 'WarrantyFrom', 'CreatedDate', 'Image', 'CreatedDate',],    # Immediad
    # Add more as needed for each company
}


from django.http import JsonResponse
from django.template.loader import render_to_string

# Assuming COMPANY_COLUMNS is defined at the top of your views.py

from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import AddProductForm

# Assuming COMPANY_COLUMNS is defined at the top of your views.py

def fetch_company_fields(request):
    company_id = request.GET.get('company_id')
    # Fetch relevant field names for the company
    relevant_fields = COMPANY_COLUMNS.get(company_id, [])
    
    # Initialize the form
    form = AddProductForm()
    
    # Dynamically adjust form to only include fields relevant to the selected company
    form.fields = {field: form.fields[field] for field in relevant_fields if field in form.fields}
    
    # Render the form with the adjusted fields to HTML
    form_fields_html = render_to_string('company_fields.html', {'form': form}, request=request)
    
    return JsonResponse({'html': form_fields_html})
