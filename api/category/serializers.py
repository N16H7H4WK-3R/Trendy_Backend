from .models import Category
from rest_framework import serializers


class CategorySerialzer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = { "name", "description" }
        fields = '__all__'
