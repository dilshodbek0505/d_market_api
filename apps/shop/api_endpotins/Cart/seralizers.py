from rest_framework import serializers
from apps.shop.models import Cart, CartItem



class CartItemSerializer(serializers.ModelSerializer):
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'total_price']
        

class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'created_at', 'cart_items', 'total_price']
        extra_kwargs = {
            'user': {'write_only': True},
        }

    def create(self, validated_data):
        cart_items_data = validated_data.pop('cart_items')
        cart = Cart.objects.create(**validated_data)

        cart_items_objs = [CartItem(cart=cart, **item_data) for item_data in cart_items_data]
        CartItem.objects.bulk_create(cart_items_objs)
        
        return cart

