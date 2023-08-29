from rest_framework.viewsets import ModelViewSet

from apps.posts.filters import PostStatusFilter
from apps.posts.models import Post
from apps.posts.serializers import PostDetailSerializer, PostListSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    filter_backends = [PostStatusFilter]

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        return self.serializer_class
