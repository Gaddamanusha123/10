from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PlanViewSet, UserSubscriptionViewSet

router = DefaultRouter()
router.register(r'plans', PlanViewSet, basename='plan')
router.register(r'user-subscriptions', UserSubscriptionViewSet, basename='user-subscription')

urlpatterns = [
    path('', include(router.urls)),
]
