from rest_framework import serializers

from apps.shop.models import Category



class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('id', 'name', 'name_ru', 'index')
        extra_kwargs = {
            'name_ru': {'write_only': True},
        }
        