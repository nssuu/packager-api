from django.urls import path, include
from rest_framework.routers import DefaultRouter

from packages import viewsets

router = DefaultRouter()
router.register(r'packages', viewsets.PackageViewSet, basename="packages")

urlpatterns = [
    path('', include(router.urls)),
]
