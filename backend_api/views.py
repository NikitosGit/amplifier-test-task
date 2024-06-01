from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Material, Category
from .serializers import MaterialSerializer, CategorySerializer, CategoryWithMaterialSerializer


class MaterialView(ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class MaterialDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class CategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryWithMaterialsView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryWithMaterialSerializer


class CategoryWithMaterialsFlatView(APIView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        materials = Material.objects.all()

        category_serializer = CategorySerializer(categories, many=True)
        material_serializer = MaterialSerializer(materials, many=True)

        combined_data = category_serializer.data + material_serializer.data

        return Response(combined_data, status=status.HTTP_200_OK)
