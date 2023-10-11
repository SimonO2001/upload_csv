from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    Lokation = models.CharField(max_length=255)
    KundeID = models.CharField(max_length=255)
    MACadd = models.CharField(max_length=255)
    Model = models.CharField(max_length=255)
    SerieNr = models.CharField(max_length=255)
    Navn = models.CharField(max_length=255)
    GatewayIP = models.CharField(max_length=255)
    Noter = models.CharField(max_length=255)
    Journalsystem = models.CharField(max_length=255)
    Analyzers = models.CharField(max_length=255)
    SIMnr = models.CharField(max_length=255)
    Image = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, db_constraint=True, null=True, blank=True)

    def __str__(self):
        return f"{self.Lokation} {self.KundeID} {self.MACadd} {self.Model} {self.SerieNr} {self.Navn} {self.Image} {self.GatewayIP} {self.Noter} {self.Journalsystem} {self.Analyzers} {self.SIMnr} {self.company}"
    
    def __unicode__(self):
        return self.company
