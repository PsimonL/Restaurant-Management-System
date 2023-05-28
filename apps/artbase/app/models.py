from django.db import models

class Customer(models.Model):
    customer_name = models.CharField('Customer Full Name', max_length=30)
    customer_status = models.BooleanField('Customer Status', max_length=30, default=0)
    customer_address = models.CharField('Customer Address', max_length=30, default=0)
    customer_contact = models.IntegerField('Customer Contact Number', default=0)

class Catalog(models.Model):
    catalog_dish = models.CharField('Dish Name', max_length=30, default=0)
    catalog_price = models.IntegerField('Dish Price', default=0)
    catalog_description = models.CharField('Dish Description', max_length=100, default=0)

class Employee(models.Model):
    employee_name = models.CharField("Employee Name", max_length=30, default=0)
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default="")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, default="")
    food = models.ForeignKey(Catalog, on_delete=models.CASCADE, default="")
    date = models.DateTimeField(default='2023-05-25 10:30:00')
