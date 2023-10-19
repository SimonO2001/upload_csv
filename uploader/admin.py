

# Register your models here.

from django.contrib import admin
from .models import Product, Company, CustomUser
from django.contrib.auth.admin import UserAdmin  # Correct import path



admin.site.register(Product)
admin.site.register(Company)
admin.site.register(CustomUser)
