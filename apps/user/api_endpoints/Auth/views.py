from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from django.core.cache import cache

from .serializers import LoginSerializer, RegisterSerializer, PhoneNumberOtpSerializer
from apps.user.utils import generate_sms_code

User = get_user_model()


class LoginApi(GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.create(serializer.validated_data))


class RegisterApi(CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        phone_number = serializer.validated_data['phone_number']
        
        confirm_code = cache.get(f'otp_{phone_number}')
        code = self.request.data.get('code')
        
        if code:
            if confirm_code != code:
                return Response({'code did not match'}, status=400)
        else:
            return Response({'code not found'}, status=400)
        
        cache.delete(f'otp_{phone_number}')
        
        
        response_data = serializer.create(serializer.validated_data)
        return Response(response_data)


class PhoneNumberOtpApi(GenericAPIView):
    serializer_class = PhoneNumberOtpSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        phone_number = serializer.validated_data['phone_number']
        
        if cache.get(f'otp_{phone_number}'):
           return Response({'code already sent'}, status=400) 
       
        code = generate_sms_code()
        cache.set(f'otp_{phone_number}', code, 60 * 2)
        print(code)
        
        return Response({'code sent'}, status=200) 


__all__ = [
    'LoginApi',
    'RegisterApi',
    'PhoneNumberOtpApi'
]