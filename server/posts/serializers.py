from rest_framework import serializers
from .models import Post, Comment, Hashtag, Story


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ['id', 'name']


class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'author', 'author_username', 'text', 'created_at']
        read_only_fields = ['id', 'author_username', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    comments = CommentSerializer(many=True, read_only=True)
    hashtags = HashtagSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = [
            'id', 'author', 'author_username', 'text', 'image', 'video',
            'link_url', 'visibility', 'created_at', 'updated_at',
            'like_count', 'comment_count', 'save_count', 'hashtags',
        ]
        read_only_fields = ['id', 'author_username', 'created_at', 'updated_at', 'like_count', 'comment_count', 'save_count']

    def create(self, validated_data):
        hashtags_data = validated_data.pop('hashtags', [])
        post = Post.objects.create(**validated_data)
        for tag in hashtags_data:
            tag_obj, _ = Hashtag.objects.get_or_create(name=tag['name'].lower())
            post.hashtags.add(tag_obj)
        return post


class StorySerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Story
        fields = ['id', 'author', 'author_username', 'image', 'video', 'caption', 'created_at', 'expires_at', 'is_highlight']
        read_only_fields = ['id', 'author_username', 'created_at']
