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


class FlatMaterialSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    code = serializers.IntegerField()
    cost = serializers.DecimalField(max_digits=10, decimal_places=2)
    category_title = serializers.CharField(source='category.title')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'title': instance.title,
            'code': instance.code,
            'cost': instance.cost,
            'category_title': instance.category.title
        }





class CategoryWithMaterialSerializer(serializers.ModelSerializer):
    materials = MaterialSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Category
        # fields = ['category_title', 'material_name','material_cost']
        fields = ['id', 'title', 'materials']

