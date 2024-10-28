from rest_framework import serializers

from apps.shop.models import Product, ProductSize


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class ProductSizeSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = ProductSize
        fields = ('image', 'price', 'size', 'name', 'name_ru')
        extra_kwargs = {
            'name_ru' : {'write_only': True}
        }        



class ProductSerializer(DynamicFieldsModelSerializer):
    size = ProductSizeSerializer(many=True)
    
    class Meta:
        model = Product
        fields = ('id', 'category', 'title', 'title_ru', 'description', 'description_ru', 'size')
        extra_kwargs = {
            'title_ru': {'write_only': True},
            'description_ru': {'write_only': True},
        }
    
    def create(self, validated_data):
        size_data = validated_data.pop('size')
        
        product = Product.objects.create(**validated_data)
        
        product_size_objs = [ProductSize(product = product, **size) for size in size_data]
        ProductSize.objects.bulk_create(product_size_objs)
        
        return product    

