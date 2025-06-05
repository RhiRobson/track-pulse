from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('runs/', views.run_index, name='run-index'),
]
