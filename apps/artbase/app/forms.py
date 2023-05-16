from django.forms import ModelForm, TextInput, Select
from .models import Customer

class MainForm(ModelForm):
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



