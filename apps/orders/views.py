from rest_framework.viewsets import ModelViewSet

from apps.orders.filters import OrderStatusFilter
from apps.orders.models import Order, Basket
from apps.orders.serializers import OrderDetailSerializer, OrderListSerializer, BasketSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer
    filter_backends = [OrderStatusFilter]

    def get_serializer_class(self):
        if self.action == 'list':
            return OrderListSerializer
        return self.serializer_class


class BasketViewSet(ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
