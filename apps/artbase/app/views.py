from django.shortcuts import render
from .forms import CustomerForm, FoodForm, OrderForm

def index(request):

    form_customer = CustomerForm(prefix='form_customer')
    form_food = FoodForm(prefix='form_food')
    form_order = OrderForm(prefix='form_order')

    if request.method == 'POST':
        form_customer = CustomerForm(request.POST, prefix='form_customer')
        form_food = FoodForm(request.POST, prefix='form_food')
        form_order = OrderForm(request.POST, prefix='form_order')
        if form_customer.is_valid() and form_food.is_valid() and form_order.is_valid():
            form_customer.save()
            form_food.save()
            form_order.save()
    else:
        form_customer = CustomerForm()
        form_food = FoodForm()
        form_order = OrderForm()

    context = {'form_customer': form_customer, 'form_food': form_food, 'form_order': form_order}
    return render(request, 'index.html', context)
