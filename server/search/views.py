from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from posts.models import Post

User = get_user_model()


@api_view(['GET'])
@permission_classes([AllowAny])
def search(request):
    q = request.query_params.get('q', '').strip()
    users = User.objects.filter(username__icontains=q)[:10]
    posts = Post.objects.filter(text__icontains=q)[:10]
    return Response({
        'users': [{'id': u.id, 'username': u.username} for u in users],
        'posts': [{'id': p.id, 'text': p.text[:100]} for p in posts],
    })
