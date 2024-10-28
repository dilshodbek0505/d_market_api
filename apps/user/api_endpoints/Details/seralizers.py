from rest_framework import serializers

from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'phone_number', 'telegram_id', 'username', 'name', 'avatar', 'coins')
        read_only_fields = ('coins', 'telegram_id', 'username')
