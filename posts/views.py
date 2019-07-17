from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import  IsAuthenticatedOrReadOnly

from core.permissions import IsStaffOrReadOnly, IsCreatorOrReadOnly

from .models import Post
from .serializers import PostSerializer, PostCommentSerializer

# view增刪改查
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsCreatorOrReadOnly,
    ]

    def get_serializer_class(self):
        if self.action == 'retrieve': #單一要求
            return PostCommentSerializer

        return super().get_serializer_class() #給原本預設的Serializer

    # 在文章存入資料庫之前，將登入的使用者一併寫入(避免新增文章者把擁有者亂填)
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
