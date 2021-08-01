from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Register(models.Model):
    Email=models.EmailField()
    Password=models.CharField(max_length=100)
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    def __str__(self) :
        return f'{self.FirstName}'






