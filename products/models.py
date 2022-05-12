from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    width = models.DecimalField(max_digits=10, decimal_places=2)
    height = models.DecimalField(max_digits=10, decimal_places=2)
    length = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Product"
        ordering = ("id",)

    def __str__(self):
        return self.name

    def calculate_volume(self):
        return self.width * self.height * self.length

    def get_absolute_url(self):
        return f'/products/'
