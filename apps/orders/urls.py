from rest_framework.routers import DefaultRouter

from apps.orders.views import OrderViewSet, BasketViewSet

router = DefaultRouter()
router.register('orders', OrderViewSet, 'orders')
router.register('basket', BasketViewSet, 'basket')

urlpatterns = router.urls
