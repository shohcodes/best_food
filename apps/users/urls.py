from rest_framework.routers import DefaultRouter

from apps.users.views import UserViewSet, TelegramUserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('tg-users', TelegramUserViewSet, basename='tg-users')

urlpatterns = router.urls
