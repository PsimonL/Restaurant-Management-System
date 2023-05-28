from .models import Customer, Catalog, Order


class Calculator:

    def __init__(self):
        self.data_customer = list(Customer.objects.all().values())
        self.data_catalog = list(Catalog.objects.all().values())
        self.data_order = list(Order.objects.all().values())

        print(self.data_order)
