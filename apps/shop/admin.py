from django.contrib import admin
from .models import Category, Product, ProductSize, Order, OrderItem, Cart, CartItem


class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    
class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductSizeInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]
    

