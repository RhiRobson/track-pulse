from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Run


def home(request):
    return render(request, 'home.html')

def run_index(request):
    runs = Run.objects.all()
    return render(request, 'runs/index.html', {'runs': runs})

def run_detail(request, run_id):
    run = Run.objects.get(id=run_id)
    return render(request, 'runs/detail.html', {'run': run})

class RunCreate(CreateView):
    model = Run
    fields = '__all__'

class RunUpdate(UpdateView):
    model = Run
    fields = '__all__'

class RunDelete(DeleteView):
    model = Run
    success_url = '/runs/'