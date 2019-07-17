from rest_framework import serializers

from comments.serializers import CommentSerializer

from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = '__all__'
        exclude = ['creator'] #除了creator欄位其他欄位都要
        read_only_fields = ['create_at']

class PostCommentSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True) #要跟關聯的名稱一樣
    # 匿名留言
    class Meta:
        model = Post
        exclude = ['creator']
        read_only_fields = ['create_at']
