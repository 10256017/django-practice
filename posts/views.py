from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import  IsAuthenticatedOrReadOnly

from core.permissions import IsStaffOrReadOnly, IsCreatorOrReadOnly

from .models import Post
from .serializers import PostSerializer

# view增刪改查
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsCreatorOrReadOnly,
    ]
