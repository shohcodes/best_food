from rest_framework.routers import DefaultRouter

from apps.orders.views import OrderViewSet

router = DefaultRouter()
router.register('orders', OrderViewSet, 'orders')

urlpatterns = router.urls
