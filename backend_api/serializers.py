from rest_framework import serializers
from .models import Material, Category


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryWithMaterialSerializer(serializers.ModelSerializer):
    materials = MaterialSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Category
        # fields = ['category_title', 'material_name','material_cost']
        fields = ['id', 'title', 'materials']

