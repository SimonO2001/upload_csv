from django.db import models
from django.utils import timezone

class Company(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    KundeNavn = models.CharField(max_length=255, null=True, blank=True)
    TunIP = models.CharField(max_length=255, null=True, blank=True)
    MACadd = models.CharField(max_length=255, null=True, blank=True)
    Model = models.CharField(max_length=255, null=True, blank=True)
    SerieNr = models.CharField(max_length=255, null=True, blank=True)
    GatewayIP = models.CharField(max_length=255, null=True, blank=True)
    Noter = models.CharField(max_length=255, null=True, blank=True)
    Journalsystem = models.CharField(max_length=255, null=True, blank=True)
    Analyzers = models.CharField(max_length=255, null=True, blank=True)
    SIMnr = models.CharField(max_length=255, null=True, blank=True)
    Image = models.CharField(max_length=255, null=True, blank=True)
    StorageBoxUser = models.CharField(max_length=255, null=True, blank=True)
    WarrantyFrom = models.DateTimeField (default=timezone.now, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, db_constraint=True, null=True, blank=True)
    CreatedDate = models.DateTimeField(default=timezone.now, null=True, blank=True)
    AbonStart = models.DateTimeField (default=timezone.now, null=True, blank=True)

    def __str__(self):
        return f"{self.KundeNavn} {self.TunIP} {self.MACadd} {self.Model} {self.SerieNr} {self.Image} {self.StorageBoxUser} {self.WarrantyFrom} {self.GatewayIP} {self.Noter} {self.Journalsystem} {self.Analyzers} {self.SIMnr} {self.CreatedDate} {self.AbonStart}"
    
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('USER', 'User'),
    )
    user_type = models.CharField(choices=USER_TYPE_CHOICES, max_length=10)

