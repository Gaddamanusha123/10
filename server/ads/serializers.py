from rest_framework import serializers
from .models import Campaign, Ad


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ['id', 'owner', 'name', 'budget', 'is_active', 'created_at']
        read_only_fields = ['id', 'created_at']


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'campaign', 'media', 'target_url', 'impressions', 'clicks', 'created_at']
        read_only_fields = ['id', 'impressions', 'clicks', 'created_at']
