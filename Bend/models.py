from django.db import models

# Create your models here.
class logdb(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    password=models.CharField(max_length=20,null=True,blank=True)
class empdb(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    adrs=models.CharField(max_length=20,null=True,blank=True)
    mob = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to="profile", null=True, blank=True)
class catdb(models.Model):
    cname = models.CharField(max_length=20, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to="profile", null=True, blank=True)
class prodb(models.Model):
    category =models.CharField(max_length=20,null=True,blank=True)
    name = models.CharField(max_length=20,null=True,blank=True)
    price=models.IntegerField(null=True, blank=True)
    image=models.ImageField(upload_to="profile", null=True, blank=True)




