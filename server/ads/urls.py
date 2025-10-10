from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CampaignViewSet, AdViewSet

router = DefaultRouter()
router.register(r'campaigns', CampaignViewSet, basename='campaign')
router.register(r'ads', AdViewSet, basename='ad')

urlpatterns = [
    path('', include(router.urls)),
]
