from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('runs/', views.run_index, name='run-index'),
    path('runs/<int:run_id>/', views.run_detail, name='run-detail'),
    path('runs/create/', views.RunCreate.as_view(), name='run-create'),
    path('runs/<int:pk>/update/', views.RunUpdate.as_view(), name='run-update'),
    path('runs/<int:pk>/delete/', views.RunDelete.as_view(), name='run-delete'),

]
