from django.db import models
from products.models import Product
from boxes.models import Box


class Package(models.Model):

    box = models.ForeignKey(
        to=Box,
        on_delete=models.CASCADE,
        blank=True,
        null=False,
    )

    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
    )
