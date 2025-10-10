from rest_framework import viewsets, permissions
from .models import Campaign, Ad
from .serializers import CampaignSerializer, AdSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.select_related('campaign')
    serializer_class = AdSerializer
    permission_classes = [permissions.IsAuthenticated]
