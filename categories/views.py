from rest_framework.viewsets import ModelViewSet

from core.permissions import IsStaffOrReadOnly

from .models import Category
from .serializers import CategorySerializer

# view增刪改查
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsStaffOrReadOnly] #權限
