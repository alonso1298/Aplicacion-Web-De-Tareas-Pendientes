from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy # Te lleva a una URL automaticamente ante la ocurrencia de un evento
from .models import Tarea

class Logueo(LoginView):
    template_name = "base/login.html"
    field = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tareas')

@login_required
class ListaPendientes(ListView):
    model = Tarea
    context_object_name = 'tareas' #Este es el alias de la clase

class DetalleTarea(DetailView):
    model = Tarea
    context_object_name = 'tarea'
    template_name = 'base/tarea.html'


class CrearTarea(CreateView):
    model = Tarea
    fields = '__all__' #Incrpora todos los campos del modelo
    success_url = reverse_lazy('tareas') #cargamos el sitio donde nos llevara automaticamente el sitio

class EditarTarea(UpdateView):
    model = Tarea
    fields = '__all__' #Incrpora todos los campos del modelo
    success_url = reverse_lazy('tareas') #cargamos el sitio donde nos llevara automaticamente el sitio

class EliminarTarea(DeleteView):
    model = Tarea
    context_object_name = 'tarea' # Los elementos del objetos son referenciados como tareas
    success_url = reverse_lazy('tareas')