from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Run
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(LoginView):
    template_name = 'home.html'


@login_required
def run_index(request):
    runs = Run.objects.filter(user=request.user)
    return render(request, 'runs/index.html', {'runs': runs})

@login_required
def run_detail(request, run_id):
    run = Run.objects.get(id=run_id)
    return render(request, 'runs/detail.html', {'run': run})

class RunCreate(LoginRequiredMixin, CreateView):
    model = Run
    fields = ['name', 'distance', 'time', 'notes']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RunUpdate(LoginRequiredMixin, UpdateView):
    model = Run
    fields = '__all__'

class RunDelete(LoginRequiredMixin, DeleteView):
    model = Run
    success_url = '/runs/'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('run-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)