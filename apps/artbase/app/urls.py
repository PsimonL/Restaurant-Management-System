from django.urls import path
from .views import index, customer_panel, order_panel, food_panel
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name="index"),
    path('customer_panel', customer_panel, name="customer_panel"),
    path('order_panel', order_panel, name="order_panel"),
    path('food_panel', food_panel, name="food_panel"),
]