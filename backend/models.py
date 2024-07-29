from django.db import models

# Create your models here.

class Donordb(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Photo = models.ImageField(upload_to="pics",null=True,blank=True)
    Bloodgroup = models.CharField(max_length=100,null=True,blank=True)
    Address = models.CharField(max_length=100, null=True,blank=True)
    Contact = models.TextField(null=True,blank=True)


class approvereqdb(models.Model):
    donorname = models.CharField(max_length=100, null=True, blank=True)
    donorage = models.IntegerField(null=True, blank=True)
    disease = models.CharField(max_length=100, null=True, blank=True)
    bloodgroup = models.CharField(max_length=100, null=True, blank=True)
    unit = models.IntegerField(null=True, blank=True)
