from django.shortcuts import render
from .forms import MainForm

def index(request):

    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            form.save()
            # Przekierowanie lub wykonanie innych działań po zapisaniu formularza
    else:
        form = MainForm()

    context = {'form': form}
    return render(request, 'index.html', context)
