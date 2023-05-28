from django.forms import ModelForm, TextInput, Select, DateInput
from .models import Customer, Catalog, Order, Employee


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'customer_name': TextInput(),
            'customer_status': Select(choices={
                ("not VIP", "not VIP"),
                ("VIP", "VIP")
            }),
            'customer_address': Select(choices={
                ("Area A #postalcode", "Area A #postalcode"),
                ("Area B #postalcode", "Area B #postalcode"),
                ("Area C #postalcode", "Area C #postalcode"),
                ("Area D #postalcode", "Area D #postalcode"),
            }),
            'customer_contact': TextInput()
        }


class FoodForm(ModelForm):
    class Meta:
        model = Catalog
        fields = '__all__'
        widgets = {
            'food_name': TextInput(),
            'food_price': TextInput(),
            'food_description': TextInput()
        }


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'employee_name': TextInput()
        }


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'customer': Select(),
            'employee': Select(),
            'food': Select(),
            'date': DateInput(format='%d/%m/%Y', attrs={
                'type': 'date'
            })
        }
