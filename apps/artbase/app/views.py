from django.shortcuts import render
from .forms import CustomerForm, FoodForm

def index(request):

    form_customer = CustomerForm(prefix='form_customer')
    form_food = FoodForm(prefix='form_food')

    if request.method == 'POST':
        form_customer = CustomerForm(request.POST, prefix='form_customer')
        form_food = FoodForm(request.POST, prefix='form_food')
        if form_customer.is_valid():
            form_customer.save()
            form_food.save()
    else:
        form_customer = CustomerForm()
        form_food = FoodForm()

    context = {'form_customer': form_customer, 'form_food': form_food}
    return render(request, 'index.html', context)
