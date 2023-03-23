from django.db import models

# Create your models here.
class customer (models.Model):
    firstname = models.CharField(max_length= 50)
    lastname = models.EmailField(max_length= 50)
    email = models.EmailField(max_length= 30)
    country = models.CharField(max_length= 30)
    password = models.CharField(max_length= 70)
    address = models.CharField(max_length=100)

    