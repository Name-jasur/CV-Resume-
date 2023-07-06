from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Task,Product
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .forms import TaskForm, TaskCreateForm
def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'tasks/index.html', context)

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = request.session.get('cart', [])
    cart.append(product_id)
    request.session['cart'] = cart
    return redirect('index')


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('index')


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'tasks/task_edit.html'
    success_url = reverse_lazy('index')
    fields = ['title', 'descript', 'deadline']

class TaskCreateView(CreateView):
    model = Task  # 'task_list'
    template_name = 'tasks/task_create.html'
    form_class = TaskCreateForm
    success_url = reverse_lazy('index')
