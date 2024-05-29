from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Material
from .serializers import MaterialSerializer

class MaterialView(ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class MaterialDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
