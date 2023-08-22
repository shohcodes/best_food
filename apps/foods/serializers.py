from rest_framework import serializers

from apps.foods.models import Category, Food


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class FoodListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['name', 'price', 'category', 'is_active']


class FoodDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'
