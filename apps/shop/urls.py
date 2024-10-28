from django.urls import path

from .api_endpotins import *

app_name = 'shop'


urlpatterns = [
    path('category/list/', CategoryListApi.as_view(), name='category-list'),
    path('category/add/', CategoryCreateApi.as_view(), name='category-add'),
    path('category/details/<uuid:pk>/', CategoryDetails.as_view(), name='category-details'),
    
    path('product/add/', ProductCreateApi.as_view(), name='product-add'),
    path('product/list/', ProductListApi.as_view(), name='product-list'),
    path('product/details/<uuid:pk>/', ProductDetailsApi.as_view(), name='product-details'),
    
    path('order/admin/add/', OrderAdminCreateApi.as_view(), name='order-admin-add'),
    path('order/add/', OrderUserCreateApi.as_view(), name='order-user-add'),
    path('order/admin/list/', OrderAdminListApi.as_view(),name='order-admin-list'),
    path('order/list/', OrderUserListApi.as_view(), name='order-user-list'),
    path('order/details/<uuid:pk>/', OrderDetailsApi.as_view(), name='order-details'),
    
    path('cart/details/<uuid:pk>/', CartDetailsApi.as_view(), name='cart-details')
]
