from django.db import models
from products.models import Product


class Box(models.Model):
    name = models.CharField(max_length=100)
    volume = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Box"
        verbose_name_plural = "Boxes"
        ordering = ("id",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/boxes/'
