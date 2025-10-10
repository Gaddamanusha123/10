from rest_framework import viewsets, permissions, decorators, response
from .models import Group, GroupPost
from .serializers import GroupSerializer, GroupPostSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        group = serializer.save(owner=self.request.user)
        group.members.add(self.request.user)


class GroupPostViewSet(viewsets.ModelViewSet):
    queryset = GroupPost.objects.select_related('group', 'author')
    serializer_class = GroupPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
