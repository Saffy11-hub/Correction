from django.db import models
from django.forms import ModelForm
# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=300)
    second_name = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + '' + self.second_name
    