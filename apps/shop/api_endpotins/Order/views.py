from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import OrderSerializer
from apps.shop.models import Order, OrderItem
from apps.shop.permissions import IsOwner


class OrderAdminCreateApi(CreateAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderUserCreateApi(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)

class OrderAdminListApi(ListAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class OrderUserListApi(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        orders = Order.objects.filter(user = self.request.user)
        return orders

class OrderDetailsApi(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    

__all__ = [
    'OrderAdminListApi',
    'OrderUserListApi',
    'OrderAdminCreateApi',
    'OrderUserCreateApi',
    'OrderDetailsApi'
]
    
    
