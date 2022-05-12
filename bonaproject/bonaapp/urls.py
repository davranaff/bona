from django.urls import path
from .views import *


urlpatterns = [
    path('', home_page, name='home_page'),
    path('category/<pk>', category_detail, name='category_detail'),
    path('cart/', cart, name='cart_url'),
    path('add_to_cart/<pk>', add_to_cart, name='add_to_cart_url'),
    path('delete_cart_item/', delete_cart_item, name='delete_cart_item'),
    path('product_detail/<pk>', product_detail, name='product_detail_url'),
    path('create_order/', create_order, name='create_order_url'),
    path('history_order/', history_order, name='history_order_url'),
    path('buy_later/<pk>', buylater, name='buy_later_url'),
    path('return_order/<pk>', return_order, name='return_order_url'),
    path('buy_now/<pk>', buynow, name='buy_now_url'),
    path('about/', about, name='about_url')
]