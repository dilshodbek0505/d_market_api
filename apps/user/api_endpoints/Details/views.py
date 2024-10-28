from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated


from .seralizers import UserSerializer

class UserRetrieveUpdateApi(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )
    http_method_names = ['get', 'patch']
    
    def get_object(self):
        return self.request.user
    

__all__ = [
    'UserRetrieveUpdateApi'
]