from django.db import models

# Create your models here.

class Data(models.Model):
    operation_type = models.CharField(max_length=200)
    x = models.IntegerField(max_length=50)
    y = models.IntegerField(max_length=50)
    