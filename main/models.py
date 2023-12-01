from django.db import models

# Create your models here.

class Contact(models.Model):
    nom = models.CharField(max_length=50,blank=True, null=True)
    prenom = models.CharField(max_length=50 ,blank=True, null=True)
    tel = models.CharField(max_length=50,blank=True, null=True)
    tel2 = models.CharField(max_length=50,blank=True, null=True)
    email = models.CharField(max_length=50,blank=True, null=True)