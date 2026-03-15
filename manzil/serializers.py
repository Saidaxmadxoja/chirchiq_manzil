from rest_framework import serializers
from .models import Category, Manzil


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ManzilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manzil
        fields = '__all__'