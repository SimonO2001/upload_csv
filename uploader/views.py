# shop/views.py

from django.shortcuts import render
from django.views.generic.base import View
from csv import DictReader
from io import TextIOWrapper
from django.shortcuts import render, redirect  # Import redirect
from .models import Product
from .forms import UploadForm, ProductForm
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SearchForm


class UploadView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "upload.html", {"form": UploadForm()})
    
    def post(self, request, *args, **kwargs):
        products_file = request.FILES["products_file"]
        rows = TextIOWrapper(products_file, encoding="utf-8", newline="")
        row_count = 0
        form_errors = []
        for row in DictReader(rows):
            row_count += 1
            form = ProductForm(row)
            if not form.is_valid():
                form_errors = form.errors
                break
            form.save()
        return render(
            request,
            "upload.html",
            {
                "form": UploadForm(),
                "form_errors": form_errors,
                "row_count": row_count,
            }
        )




from django.shortcuts import render
from .models import Product
from .forms import SearchForm

def display_data(request):
    products = Product.objects.all()
    search_form = SearchForm(request.GET)  # Get the search form data

    query = request.GET.get('query', '')  # Get the query from request GET parameters

    if query:
        products = products.filter(Lokation__icontains=query)  # Adjust the field as needed for your search

    return render(request, 'display_data.html', {'products': products, 'search_form': search_form})






def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('display_data')  # Redirect to the data display page
    else:
        form = ProductForm(instance=product)

    return render(request, 'edit_product.html', {'form': form})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('display_data')  # Redirect to the data display page after deletion

    return render(request, 'delete_product.html', {'product': product})

from django.shortcuts import render, redirect
from .forms import AddProductForm

def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_data')  # Redirect to the data display page after adding

    else:
        form = AddProductForm()

    return render(request, 'add_product.html', {'form': form})
