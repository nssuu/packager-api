from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Package
from .serializers import PackageSerializer


class PackageList(APIView):
    def get(self, request, format=None):
        packages = Package.objects.all()[0:10]
        serializer = PackageSerializer(packages, many=True)
        return Response(serializer.data)


class PackagePost(APIView):
    def post(self, request, format=None):
        package_data = request.data

        new_package = Package.objects.create()

        new_package.products.set(package_data['products'])

        serializer = PackageSerializer(new_package)
        return Response(serializer.data)
