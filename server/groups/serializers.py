from rest_framework import serializers
from .models import Group, Membership, GroupPost


class GroupSerializer(serializers.ModelSerializer):
    members_count = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ['id', 'name', 'description', 'is_public', 'owner', 'members_count', 'created_at']
        read_only_fields = ['id', 'members_count', 'created_at']

    def get_members_count(self, obj):
        return obj.members.count()


class GroupPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupPost
        fields = ['id', 'group', 'author', 'text', 'created_at']
        read_only_fields = ['id', 'created_at']
