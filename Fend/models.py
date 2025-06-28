from django.db import models

# Create your models here.
class logdb(models.Model):
    username=models.CharField(max_length=20, null=True, blank=True)
    password=models.CharField(max_length=20, null=True, blank=True)
class regdb(models.Model):
    username = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=20, null=True, blank=True)
    password2= models.CharField(max_length=20, null=True, blank=True)
class contactdb(models.Model):
    name= models.CharField(max_length=20, null=True, blank=True)
    email= models.CharField(max_length=20, null=True, blank=True)
    msg= models.CharField(max_length=20, null=True, blank=True)
class cartdb(models.Model):
    image=models.ImageField( null=True, blank=True)
    name= models.CharField(max_length=20, null=True, blank=True)
    quantity=models.IntegerField(null=True, blank=True)
    totalprice=models.IntegerField(null=True, blank=True)
    size=models.CharField(max_length=20,null=True,blank=True)

