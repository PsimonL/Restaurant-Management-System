from django.contrib import admin
from .models import Customer, Catalog, Order, Employee,OrderItem

admin.site.register(Customer)

admin.site.register(Catalog)

admin.site.register(Order)

admin.site.register(Employee)

admin.site.register(OrderItem)