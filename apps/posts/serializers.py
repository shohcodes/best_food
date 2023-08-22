from rest_framework.serializers import ModelSerializer

from apps.posts.models import Post


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['created_at', 'updated_at']


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
