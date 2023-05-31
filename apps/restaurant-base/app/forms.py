from django.forms import ModelForm, TextInput, Select, DateInput,formset_factory,ModelChoiceField
from .models import Customer, Catalog, Order, Employee,OrderItem


class CustomerForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'] = CustomerChoiceField(queryset=Customer.objects.all(), required=True)
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

class CatalogChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.catalog_dish
class CustomerChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.customer_name
class EmployeeChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.areaCode

class OrderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'] = CustomerChoiceField(queryset=Customer.objects.all(), required=True)
        self.fields['employee'] = EmployeeChoiceField(queryset=Employee.objects.all(), required=True)
        self.fields['item_id'] = CatalogChoiceField(queryset=Catalog.objects.all(), required=True)

    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'date': DateInput(format='%d/%m/%Y', attrs={
                'type': 'date'
            }),
        }