from django.db import models

# Create your models here.
class Mart(models.Model):
    mart_name = models.CharField(max_length=255)