from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(blank=True, max_length=300)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.DecimalField(max_digits=6, decimal_places=2)
    sku = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
