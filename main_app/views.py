from django.shortcuts import render
from .models import Run


def home(request):
    return render(request, 'home.html')

def run_index(request):
    runs = Run.objects.all()
    return render(request, 'runs/index.html', {'runs': runs})