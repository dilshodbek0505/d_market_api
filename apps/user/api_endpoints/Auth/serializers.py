from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed

from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import make_password


User = get_user_model()


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    telegram_id = serializers.CharField(required=False)

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')

        user = authenticate(phone_number=phone_number, password=password)

        if user is None:
            raise AuthenticationFailed('Invalid phone number or password.')

        attrs['user'] = user
        return attrs

    def create(self, validated_data):
        user = validated_data['user']
        telegram_id =validated_data.get('telegram_id')
        if telegram_id:
            user.telegram_id = telegram_id
            user.save()

        token, _  = Token.objects.get_or_create(user = user)

        return {
            'id': user.id,
            'token': token.key,
        }


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['name', 'phone_number', 'password', 'telegram_id', 'avatar']


    def create(self, validated_data):
        
        user = User(
            name=validated_data['name'],
            phone_number=validated_data['phone_number'],
            telegram_id=validated_data.get('telegram_id'),
            avatar=validated_data.get('avatar')
        )
        
        user.set_password(validated_data['password'])
        
        user.save()
        
        # Token yaratish
        token = Token.objects.create(user = user)
        print({
            'id': user.id,
            'token': token.key,
        })
        return {
            'id': user.id,
            'token': token.key,
        }


class PhoneNumberOtpSerializer(serializers.Serializer):
    phone_number = serializers.CharField()

    def validate_phone_number(self, value):
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError( "user with this phone number already exists.")
        return value