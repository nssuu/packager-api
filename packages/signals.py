from xml.dom import ValidationErr
from django.db.models.signals import pre_save
from django.dispatch import receiver
from rest_framework import exceptions
from packages.models import Package
from boxes.models import Box


@receiver(pre_save, sender=Package)
def handle_pre_save_package(sender, instance, **kwargs):
    product_volume = instance.product.calculate_volume()
    box = Box.objects.filter(
        volume__gte=product_volume,
    ).order_by(
        'volume',
    ).first()
    if box is None:
        raise exceptions.ValidationError(
            detail={
                'product_id': [
                    'No box available.',
                ],
            },
        )
    instance.box = box
