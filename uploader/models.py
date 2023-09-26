# shop/models.py

from django.db import models

class Product(models.Model):
    Lokation = models.CharField(max_length=1000, null=True,blank=True)
    KundeID = models.CharField(max_length=1000, null=True,blank=True, db_column='KundeID')
    MACadd = models.CharField(max_length=1000, null=True,blank=True, db_column='MAC')
    Model = models.CharField(max_length=1000, null=True,blank=True)
    SerieNr = models.CharField(max_length=1000, null=True,blank=True, db_column='S_N')
    Navn = models.CharField(max_length=1000, null=True,blank=True)
    Image = models.CharField(max_length=1000, null=True,blank=True)
    GatewayIP = models.CharField(max_length=1000, null=True,blank=True, db_column='GW_IP')
    Noter = models.CharField(max_length=1000, null=True,blank=True)
    Journalsystem = models.CharField(max_length=1000, null=True,blank=True)
    Analyzers = models.CharField(max_length=1000, null=True,blank=True)
    SIMnr = models.CharField(max_length=1000, null=True,blank=True, db_column='SIM')
    

    def __str__(self):
        return f"{self.Lokation} {self.KundeID} {self.MACadd} {self.Model} {self.SerieNr} {self.Navn} {self.Image} {self.GatewayIP} {self.Noter} {self.Journalsystem} {self.Analyzers} {self.SIMnr}"