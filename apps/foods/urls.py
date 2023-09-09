from rest_framework.routers import DefaultRouter
from django.urls import path
from apps.foods.views import FoodViewSet, CategoryViewSet, FoodListByCategory

router = DefaultRouter()
router.register('foods', FoodViewSet, 'foods')
router.register('categories', CategoryViewSet, 'categories')

urlpatterns = [
    path('categories/<int:id>/foods/', FoodListByCategory.as_view(), name='food-list-by-category')
] + router.urls
