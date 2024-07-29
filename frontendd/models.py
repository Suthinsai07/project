from django.db import models

# Create your models here.
class userdb(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    confirmpassword = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to="photoss", null=True, blank=True)

class userregisterdb(models.Model):

    username = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    confirmpassword = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True,blank=True)
    bloodgroup = models.CharField(max_length=100,null=True,blank=True)
    disease = models.CharField(max_length=100, null=True, blank=True)
    address= models.CharField(max_length=100, null=True,blank=True)
    contact = models.IntegerField(null=True,blank=True)
    photo= models.ImageField(upload_to="picss",null=True,blank=True)



class donorregisterdb(models.Model):

    username = models.EmailField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    confirmpassword = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True,blank=True)
    bloodgroup = models.CharField(max_length=100,null=True,blank=True)

    address= models.CharField(max_length=100, null=True,blank=True)
    contact = models.IntegerField(null=True,blank=True)
    photo= models.ImageField(upload_to="picsss",null=True,blank=True)

class makerequestdb(models.Model):


    patientname = models.CharField(max_length=100, null=True, blank=True)
    patientage = models.IntegerField(null=True, blank=True)
    reason= models.CharField(max_length=100, null=True, blank=True)
    bloodgroup = models.CharField(max_length=100, null=True, blank=True)
    unit = models.IntegerField(null=True, blank=True)


class donateblooddb(models.Model):
    donorname = models.CharField(max_length=100, null=True, blank=True)
    donorage = models.IntegerField(null=True, blank=True)
    disease = models.CharField(max_length=100, null=True, blank=True)
    bloodgroup = models.CharField(max_length=100, null=True, blank=True)
    unit = models.IntegerField(null=True, blank=True)







