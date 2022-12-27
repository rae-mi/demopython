from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from forms import TodoForm
from .models import Lists
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


# Create your views here.

class Tasklistview(ListView):
    model = Lists
    template_name = 'home.html'
    context_object_name = 'task1'


class Taskdetailview(DetailView):
    model = Lists
    template_name = 'details.html'
    context_object_name = 'task'


class Taskupdateview(UpdateView):
    model = Lists
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'order', 'date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs={'pk': self.object.id})


class Taskdeleteview(DeleteView):
    model = Lists
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')


def add(request):
    task1 = Lists.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        order = request.POST.get('order', '')
        date = request.POST.get('date', '')

        task = Lists(name=name, order=order, date=date)
        task.save()
    return render(request, 'home.html', {'task1': task1})


def details(request):
    return render(request, 'details.html')


def delete(request, taskid):
    task = Lists.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, taskid):
    task = Lists.objects.get(id=taskid)
    f = TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'edit.html', {'f': f, 'task': task})
