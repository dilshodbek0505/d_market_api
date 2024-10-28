from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .serializers import ProductSerializer

from apps.shop.models import Product


class ProductCreateApi(CreateAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductListApi(ListAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_serializer(self, *args, **kwargs):
        fields = self.request.query_params.get('fields')
        if fields:
            fields = fields.split(',')
        kwargs['fields'] = fields
        return super().get_serializer(*args, **kwargs)

class ProductDetailsApi(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,  IsAdminUser)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'patch', 'delete']
    

__all__ = [
    'ProductCreateApi',
    'ProductListApi',
    'ProductDetailsApi'
]
    
