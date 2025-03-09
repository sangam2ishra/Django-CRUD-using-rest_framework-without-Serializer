from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    category=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    brand=models.CharField(max_length=100)
    quantity=models.PositiveIntegerField()

    def __str__(self):
        return self.name
