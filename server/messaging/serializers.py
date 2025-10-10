from rest_framework import serializers
from .models import Conversation, Message


class MessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.ReadOnlyField(source='sender.username')

    class Meta:
        model = Message
        fields = ['id', 'conversation', 'sender', 'sender_username', 'text', 'attachment', 'created_at', 'is_read']
        read_only_fields = ['id', 'sender_username', 'created_at']


class ConversationSerializer(serializers.ModelSerializer):
    participants_usernames = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username',
        source='participants'
    )
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['id', 'name', 'participants', 'participants_usernames', 'is_group', 'created_at', 'last_message']
        read_only_fields = ['id', 'participants_usernames', 'created_at', 'last_message']

    def get_last_message(self, obj):
        last = obj.messages.order_by('-created_at').first()
        return MessageSerializer(last).data if last else None
