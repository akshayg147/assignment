from rest_framework import routers

from .views import AuthViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('api/auth', AuthViewSet, basename='auth')
router.register('/api/auth/login', AuthViewSet, basename='login')
router.register('/api/auth/register', AuthViewSet, basename='register')
router.register('/api/auth/logout', AuthViewSet, basename='logout')
router.register('/api/auth/password_change', AuthViewSet, basename='password_change')
urlpatterns = router.urls