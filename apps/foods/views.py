from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from apps.foods.filters import FoodStatusFilter
from apps.foods.models import Food, Category
from apps.foods.serializers import FoodDetailSerializer, FoodListSerializer, CategoryListSerializer


class FoodViewSet(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodDetailSerializer
    filter_backends = [FoodStatusFilter]

    def get_serializer_class(self):
        if self.action == 'list':
            return FoodListSerializer
        return self.serializer_class


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class FoodListByCategory(ListAPIView):
    serializer_class = FoodDetailSerializer

    def get_queryset(self):
        category_id = self.kwargs['id']
        return Food.objects.filter(category__id=category_id)
