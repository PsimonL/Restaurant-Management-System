from django.db import models

class Customer(models.Model):
    customer_name = models.CharField('Customer Full Name', max_length=30)
    customer_type = models.BooleanField('Customer Type', max_length=30, default=0)
    customer_location = models.CharField('Customer Location', max_length=30, default=0)

class Catalog(models.Model):
    catalog_dish = models.CharField('Dish Name: ', max_length=30)
    catalog_price = models.IntegerField('Dish Price: ')
    
class Order(models.Model):
    order_type = models.CharField('Order Type: ', max_length=30, default="")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default="")
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, default="")

