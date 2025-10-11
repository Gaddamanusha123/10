from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import GroupViewSet, GroupPostViewSet

router = DefaultRouter()
router.register(r'', GroupViewSet, basename='group')
router.register(r'posts', GroupPostViewSet, basename='group-post')

urlpatterns = [
    path('', include(router.urls)),
]
