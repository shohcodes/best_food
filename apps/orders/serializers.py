from rest_framework import serializers

from apps.orders.models import Order, OrderFood, Basket


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


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'

    def create(self, validated_data):
        telegram_user = validated_data['telegram_user']
        food = validated_data['food']
        amount = validated_data['amount']

        existing_basket = Basket.objects.filter(telegram_user=telegram_user, food=food).first()

        if existing_basket:
            existing_basket.amount += amount
            existing_basket.save()
            return existing_basket
        else:
            return Basket.objects.create(**validated_data)

        
