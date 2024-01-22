from rest_framework.routers import DefaultRouter

from apps.users.views import UserViewSet


router = DefaultRouter()
router.register('user', UserViewSet, basename='api_users')

urlpatterns = router.urls