from .models import Category
from rest_framework import serializers

class CategorySerialzer(serializers.Serializer):
    class Meta:
        model = Category
        field = {
            "name", "description"
        }