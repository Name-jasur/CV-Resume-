from django.urls import path
from .views import TaskListView, TaskDetailView, TaskUpdateView, TaskDeleteView, TaskCreateView
from django.contrib import admin
from . import views


urlpatterns = [
    path('task/create', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/delete', TaskDeleteView.as_view(), name='task_delete'),
    path('task/<int:pk>/edit', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('', views.home, name='index'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

]

