# shop/models.py

from django.db import models

class Product(models.Model):
    Lokation = models.CharField(max_length=1000, null=True,blank=True)
    KundeID = models.CharField(max_length=1000, null=True,blank=True)
    MACadd = models.CharField(max_length=1000, null=True,blank=True)
    Model = models.CharField(max_length=1000, null=True,blank=True)
    SerieNr = models.CharField(max_length=1000, null=True,blank=True)
    Navn = models.CharField(max_length=1000, null=True,blank=True)
    Image = models.CharField(max_length=1000, null=True,blank=True)
    GatewayIP = models.CharField(max_length=1000, null=True,blank=True)
    Noter = models.CharField(max_length=1000, null=True,blank=True)
    Journalsystem = models.CharField(max_length=1000, null=True,blank=True)
    Analyzers = models.CharField(max_length=1000, null=True,blank=True)
    SIMnr = models.CharField(max_length=1000, null=True,blank=True)
    

    def __str__(self):
        return f"{self.Lokation} {self.KundeID} {self.MACadd} {self.Model} {self.SerieNr} {self.Navn} {self.Image} {self.GatewayIP} {self.Noter} {self.Journalsystem} {self.Analyzers} {self.SIMnr}"

        