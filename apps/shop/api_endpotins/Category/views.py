from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from .serializers import CategorySerializer
from apps.shop.models import Category


class CategoryListApi(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = None


class CategoryCreateApi(CreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)


class CategoryDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)
    http_method_names = ['get', 'patch', 'patch']

    
__all__ = [
    'CategoryListApi',
    'CategoryCreateApi',
    'CategoryDetails'
]
