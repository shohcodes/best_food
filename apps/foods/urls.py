from rest_framework.routers import DefaultRouter

from apps.foods.views import FoodViewSet, CategoryViewSet

router = DefaultRouter()
router.register('foods', FoodViewSet, 'foods')
router.register('categories', CategoryViewSet, 'categories')

urlpatterns = router.urls
