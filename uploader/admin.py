

# Register your models here.

from django.contrib import admin
from .models import Product, Company

admin.site.register(Product)
admin.site.register(Company)