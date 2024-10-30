from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.utils import timezone

from apps.common.models import BaseModel


User = get_user_model()


class Category(BaseModel):
    name = models.CharField(max_length=128)
    index = models.SmallIntegerField(default=1)
    
    def __str__(self) -> str:
        return self.name
    
    
class Product(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=128)
    description = models.TextField()
    
    def __str__(self):
        return self.title

    
class ProductSize(BaseModel):
    class ProductSizeChoices(models.TextChoices):
        LITRE = 'l', 'Liter'
        CUBIC_METER = 'mcub', 'Kub metr'
        SQUARE_METER  = 'mkv', 'Kvadrat metr'
        TON = 't', 'Tonna'
        CENTIMETER  = 'cm', 'Santimetr'
        GRAM = 'g', 'Gramm'
        KILOGRAM = 'kg', 'Kilogramm'
        PORTION = 'port', 'Porsiya'
        METER = 'm', 'Metr'
        PIECE = 'pcs', 'Dona'
        
    product = models.ForeignKey(Product, models.CASCADE, related_name='size')
    name = models.CharField(max_length=128)
    size = models.CharField(max_length=50, choices=ProductSizeChoices.choices)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name=_('Price'))
    image = models.ImageField(upload_to='product/', blank=True, null=True)
    
    def __str__(self):
        return f'{self.name} | {self.size} | {self.product.title}'
        

class Order(BaseModel):
    user = models.ForeignKey(User, models.CASCADE, related_name='orders')
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', _('Pending')),
            ('processing', _('Processing')),
            ('shipped', _('Shipped')),
            ('completed', _('Completed')),
            ('cancelled', _('Cancelled'))
        ],
        default='pending'
    )
    delivery_time = models.DateTimeField(default=timezone.now)
    payment_type = models.CharField(
        max_length=20,
        choices=[
            ('card', 'card'),
            ('cash', 'cash')
        ],
        default='cash'
    )
    
    @property
    def total_price(self):
        return sum(item.total_price for item in self.order_items.all())
    
    def __str__(self) -> str:
        return self.user.phone_number


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_size = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def total_price(self):
        return self.quantity * self.item_price
    
    def __str__(self):
        return f'{self.product.title} - {self.quantity}'


class Cart(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
 
    @property
    def total_price(self):
        return sum(item.total_price for item in self.cart_items.all())

    def __str__(self):
        return self.user.phone_number


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_size = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.quantity * self.product_size.price

    def __str__(self):
        return f"{self.product.title} - {self.quantity}"
    
