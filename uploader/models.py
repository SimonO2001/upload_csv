from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    Lokation = models.CharField(max_length=255, null=True, blank=True)
    KundeID = models.CharField(max_length=255, null=True, blank=True)
    MACadd = models.CharField(max_length=255, null=True, blank=True)
    Model = models.CharField(max_length=255, null=True, blank=True)
    SerieNr = models.CharField(max_length=255, null=True, blank=True)
    Navn = models.CharField(max_length=255, null=True, blank=True)
    GatewayIP = models.CharField(max_length=255, null=True, blank=True)
    Noter = models.CharField(max_length=255, null=True, blank=True)
    Journalsystem = models.CharField(max_length=255, null=True, blank=True)
    Analyzers = models.CharField(max_length=255, null=True, blank=True)
    SIMnr = models.CharField(max_length=255, null=True, blank=True)
    Image = models.CharField(max_length=255, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, db_constraint=True, null=True, blank=True)

    def __str__(self):
        return f"{self.Lokation} {self.KundeID} {self.MACadd} {self.Model} {self.SerieNr} {self.Navn} {self.Image} {self.GatewayIP} {self.Noter} {self.Journalsystem} {self.Analyzers} {self.SIMnr}"
    
    """def __unicode__(self):
        return self.company"""
    
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('USER', 'User'),
    )
    user_type = models.CharField(choices=USER_TYPE_CHOICES, max_length=10)

