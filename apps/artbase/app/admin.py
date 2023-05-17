from django.contrib import admin
from .models import Customer, Catalog, Order

admin.site.register(Customer)

admin.site.register(Catalog)

admin.site.register(Order)