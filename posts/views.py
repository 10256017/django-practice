from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import  IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import action

from core.permissions import IsStaffOrReadOnly, IsCreatorOrReadOnly

from comments.models import Comment
from comments.serializers import CommentSerializer

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

    def get_queryset(self):
        if self.action == 'comments':
            pk = self.kwargs.get('pk') #取得pk
            return Comment.objects.filter(post_id=pk) #過濾postid的留言

        if self.action == 'my': #只顯示自己的文章
            return Post.objects.filter(creator=self.request.user)

        return super().get_queryset()

    def get_serializer_class(self):
        # if self.action == 'retrieve': #單一要求
        #     return PostCommentSerializer
        #
        # if self.action == 'comments':
        #     return CommentSerializer
        #
        # return super().get_serializer_class() #給原本預設的Serializer

        default = super().get_serializer_class()
        return {
            'retrieve': PostCommentSerializer,
            'comments': CommentSerializer
        }.get(self.action, default)

    # 在文章存入資料庫之前，將登入的使用者一併寫入(避免新增文章者把擁有者亂填)
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    # http: // 127.0.0.1: 8000 / posts / 1 / comments
    @action(['GET'], True)  #detail = True -> 列出單一物件 (url會有PK)
    def comments(self, request, pk):
        return self.list(request)

        # queryset = self.get_queryset()
        # serializer = self.get_serializer(queryset, many=True)
        # return Response(serializer.data)

        # return Response({
        #     'message': f'Comments of post {pk}',
        # })
    
    @action(['GET'], False, permission_classes= [IsAuthenticated]) #permission ->要有登入才能看到自己的文章
    def my(self, request):
        return self.list(request)
