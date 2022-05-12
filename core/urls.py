
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('', include('products.urls')),
    path('', include('boxes.urls')),
    path('', include('packages.urls')),
]
