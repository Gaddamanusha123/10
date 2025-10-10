from rest_framework import viewsets, permissions
from .models import Plan, UserSubscription
from .serializers import PlanSerializer, UserSubscriptionSerializer


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = UserSubscription.objects.select_related('plan')
    serializer_class = UserSubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]
