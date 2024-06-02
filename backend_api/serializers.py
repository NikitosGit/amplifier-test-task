from django.db.models import Sum
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
    total_cost = serializers.SerializerMethodField('get_total_cost')
    children = serializers.SerializerMethodField()
    materials = MaterialSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Category
        fields = ['id', 'title', 'parent_id', 'total_cost', 'children', 'materials']
    def get_total_cost(self, obj):
        all_materials = obj.materials.all()
        for subcategory in obj.get_descendants():
            all_materials = all_materials | subcategory.materials.all()

        total_cost = all_materials.aggregate(total_cost=Sum('cost'))['total_cost'] or 0
        return total_cost
    def get_children(self, obj):
        return CategoryWithMaterialSerializer(obj.children.all(), many=True).data
