from django.forms import ModelForm, TextInput, Select, ModelChoiceField, CheckboxInput, BooleanField
from .models import Customer, Catalog, Order, Employee

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'customer_name': TextInput(attrs={
                'class': 'button-48'            
            }),
            'customer_status': BooleanField(),
            'customer_address': Select(choices={
                ("Area A", "Area A"),
                ("Area B", "Area B"),
                ("Area C", "Area C"),
                ("Area D", "Area D"),
            }, attrs={
                'class': 'button-48'            
            }),
            'customer_contact': TextInput()
        }

class FoodForm(ModelForm):
    class Meta:
        model = Catalog
        fields = '__all__'
        widgets = {
            'food_name': TextInput(attrs={
                'class': 'button-48'            
            }),
            'food_price': TextInput(attrs={
                'class': 'button-48'            
            }),
            'food_description': TextInput(attrs={
                'class': 'button-48'            
            })
        }

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'employee_name': TextInput(attrs={
                'class': 'button-48'            
            })
        }

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    




