from django.db import models

class Order(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2)

class Product(models.Model):
    name = models.CharField(max_length=100)

class User(models.Model):
    username = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)