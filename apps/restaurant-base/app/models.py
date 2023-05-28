from django.db import models


class Customer(models.Model):
    customer_name = models.CharField('Customer Full Name', max_length=50, blank=False, null=False)
    customer_status = models.BooleanField('Customer Status', default=False, blank=False, null=False)
    customer_address = models.CharField('Customer Address', max_length=60, blank=False, null=False)
    customer_contact = models.IntegerField('Customer Contact Number', default=0, blank=False, null=False)


class Catalog(models.Model):
    catalog_dish = models.CharField('Dish Name', max_length=30, blank=False, null=False)
    catalog_price = models.IntegerField('Dish Price', default=0, blank=False, null=False)
    catalog_description = models.CharField('Dish Description', max_length=100, blank=False, null=False)


class Employee(models.Model):
    employee_name = models.CharField("Employee Name", max_length=50, blank=False, null=False)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default="", blank=False, null=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, default="", blank=False, null=False)
    food = models.ForeignKey(Catalog, on_delete=models.CASCADE, default="", blank=False, null=False)
    date = models.DateTimeField(default='2023-05-25 10:30:00', blank=False, null=False)
