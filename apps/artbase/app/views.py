from django.shortcuts import render
from .forms import MainForm

def index(request):

    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MainForm()

    context = {'form': form}
    return render(request, 'index.html', context)
