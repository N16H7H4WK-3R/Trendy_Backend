from rest_framework import viewsets
from .serializers import CategorySerialzer
from .models import Category


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerialzer
