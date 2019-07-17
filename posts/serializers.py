from rest_framework import serializers

from comments.serializers import CommentSerializer

from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['creator','create_at']

class PostCommentSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True) #要跟關聯的名稱一樣

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['creator','create_at']
