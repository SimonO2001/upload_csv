# shop/views.py

from django.shortcuts import render
from django.views.generic.base import View
from csv import DictReader
from io import TextIOWrapper
from django.shortcuts import render, redirect  # Import redirect
from .models import Product

from .forms import UploadForm, ProductForm

from django.shortcuts import render
from .models import Product

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
    


def display_data(request):
    products = Product.objects.all()
    return render(request, 'display_data.html', {'products': products})
