from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from .seralizers import CartSerializer
from apps.shop.models import Cart



class CartDetailsApi(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    http_method_names = ['get', 'patch']
    
    def get_queryset(self):
        return Cart.objects.filter(user = self.request.user)

__all__ = [
    'CartDetailsApi'
]