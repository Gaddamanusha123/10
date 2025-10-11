from rest_framework import serializers
from .models import Plan, UserSubscription


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'name', 'price', 'duration_days', 'perks']
        read_only_fields = ['id']


class UserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubscription
        fields = ['id', 'user', 'plan', 'started_at', 'expires_at', 'is_active']
        read_only_fields = ['id', 'started_at']
