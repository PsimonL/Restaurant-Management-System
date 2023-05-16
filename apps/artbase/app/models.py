from django.db import models

class Customer(models.Model):
    customer_name = models.CharField('Customer Full Name: ', max_length=30)
    customer_spendings = models.IntegerField('Customer Spendings: ')
    customer_premium = models.BooleanField('Customer Premium: ', max_length=30, default=0)

class Order(models.Model):
    order_type = models.CharField('Order Type: ', max_length=30, default="")

class Catalog(models.Model):
    catalog_dish = models.CharField('Dish Name: ', max_length=30)
    catalog_price = models.IntegerField('Dish Price: ')