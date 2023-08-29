from rest_framework.routers import DefaultRouter

from apps.foods.views import FoodViewSet

router = DefaultRouter()
router.register('foods', FoodViewSet, 'foods')

urlpatterns = router.urls
