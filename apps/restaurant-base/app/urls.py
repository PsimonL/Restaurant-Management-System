from django.urls import path
from .views import index, customer_panel, order_panel, food_panel, employee_panel, order_endpoint, customer_endpoint, catalog_endpoint, employee_endpoint
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name="index"),
    path('customer_panel', customer_panel, name="customer_panel"),
    path('order_panel', order_panel, name="order_panel"),
    path('food_panel', food_panel, name="food_panel"),
    path('employee_panel', employee_panel, name="employee_panel"),
    path('api/order_endpoint', order_endpoint, name="order_endpoint"),
    path('api/customer_endpoint', customer_endpoint, name="customer_endpoint"),
    path('api/catalog_endpoint', catalog_endpoint, name="catalog_endpoint"),
    path('api/employee_endpoint', employee_endpoint, name="employee_endpoint")
]