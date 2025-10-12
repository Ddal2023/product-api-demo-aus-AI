from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField("product description",  default="no descriptions")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']