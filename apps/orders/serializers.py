from rest_framework import serializers

from apps.orders.models import Order, OrderFood


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ['foods', 'created_at', 'updated_at']


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderFoodListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderFood
        exclude = ['created_at', 'updated_at']


class OrderFoodDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderFood
        fields = '__all__'
