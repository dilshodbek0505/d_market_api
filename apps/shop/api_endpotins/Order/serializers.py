from rest_framework import serializers
from apps.shop.models import Order, OrderItem, Product, ProductSize


class OrderItemSerializer(serializers.ModelSerializer):
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'item_price', 'total_price']


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'created_at', 'updated_at', 'status', 'order_items', 'delivery_time', 'payment_type', 'total_price']
        extra_kwargs = {
            'user': {'write_only': True},
        }

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)

        order_items_objs = [OrderItem(order=order, **item_date) for item_date in order_items_data]
        OrderItem.objects.bulk_create(order_items_objs)

        return order

