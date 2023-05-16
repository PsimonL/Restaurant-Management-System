from django.forms import ModelForm, TextInput, Select
from .models import Customer, Catalog

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'customer_name': TextInput(),
            'customer_type': Select(choices={
                ("A", "A"),
                ("B", "B"),
                ("C", "C"),
                ("D", "D"),
            }),
            'customer_location': Select(choices={
                ("A", "A"),
                ("B", "B"),
                ("C", "C"),
                ("D", "D"),
            })
        }

class FoodForm(ModelForm):
    class Meta:
        model = Catalog
        fields = '__all__'
        widgets = {
            'food_name': TextInput(),
            'food_price': TextInput()
        }



