from rest_framework.viewsets import ModelViewSet

from apps.foods.filters import FoodStatusFilter
from apps.foods.models import Food
from apps.foods.serializers import FoodDetailSerializer, FoodListSerializer


class FoodViewSet(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodDetailSerializer
    filter_backends = [FoodStatusFilter]

    def get_serializer_class(self):
        if self.action == 'list':
            return FoodListSerializer
        return self.serializer_class
