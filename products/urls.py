from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products import viewsets

router = DefaultRouter()
router.register(r'products', viewsets.ProductViewSet, basename="products")

urlpatterns = [
    path('', include(router.urls)),
]
