from rest_framework.viewsets import ModelViewSet

from .models import Comment
from .serializers import CommentSerializer

# view增刪改查
class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
