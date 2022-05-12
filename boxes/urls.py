from django.urls import path, include
from rest_framework.routers import DefaultRouter

from boxes import viewsets

router = DefaultRouter()
router.register(r'boxes', viewsets.BoxViewSet, basename="boxes")

urlpatterns = [
    path('', include(router.urls)),
]
