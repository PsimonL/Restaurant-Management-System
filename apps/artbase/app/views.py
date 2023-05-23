from django.shortcuts import render
from .forms import CustomerForm, FoodForm, OrderForm

def index(request):

    form_food = FoodForm(prefix='form_food')
    form_order = OrderForm(prefix='form_order')

    if request.method == 'POST':
        form_food = FoodForm(request.POST, prefix='form_food')
        form_order = OrderForm(request.POST, prefix='form_order')
        if form_food.is_valid() and form_order.is_valid():
            form_food.save()
            form_order.save()
    else:
        form_food = FoodForm()
        form_order = OrderForm()

    context = {'form_food': form_food, 'form_order': form_order}
    return render(request, 'main.html', context)

def customer_panel(request):
    
    form_customer = CustomerForm(prefix='form_customer')
    if request.method == 'POST':
        form_customer = CustomerForm(request.POST, prefix='form_customer')
        if form_customer.is_valid():
            form_customer.save()
    else:
        form_customer = CustomerForm()

    context = {'form_customer': form_customer}
    return render(request, 'customer_panel.html', context=context)

def food_panel(request):
    form_food = FoodForm(prefix='form_food')
    if request.method == 'POST':
        form_food = FoodForm(request.POST, prefix='form_food')
        if form_food.is_valid():
            form_food.save()
    else:
        form_food = FoodForm()

    context = {'form_food': form_food}
    return render(request, 'food_panel.html', context=context)

def order_panel(request):
    form_order = OrderForm(prefix='form_order')
    if request.method == 'POST':
        form_order = OrderForm(request.POST, prefix='form_order')
        if form_order.is_valid():
            form_order.save()
    else:
        form_order = OrderForm()

    context = {'form_order': form_order}
    return render(request, 'order_panel.html', context=context)
