from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin # Restinge el acceso si no estas logueado
from django.urls import reverse_lazy # Te lleva a una URL automaticamente ante la ocurrencia de un evento
from .models import Tarea

class Logueo(LoginView):
    template_name = "base/login.html"
    field = '__all__' #Incrpora todos los campos del modelo
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tareas')
    
class PaginaRegistro(FormView):
    template_name = 'base/registro.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tareas')

    def form_valid(self, form):
        usuario = form.save() # Usuario sera igual al valor de lo que se haya guardado en el formulario
        if usuario is not None:
            login(self.request, usuario)
        return super(PaginaRegistro, self).form_valid(form)

class ListaPendientes(LoginRequiredMixin, ListView):
    model = Tarea
    context_object_name = 'tareas' #Este es el alias de la clase

    def get_context_data(self, **kwarg):
        context = super().get_context_data(**kwarg)
        context['tareas'] = context['tareas'].filter(usuario=self.request.user)
        context['count'] = context['tareas'].filter(completo=False).count()
        return context

class DetalleTarea(LoginRequiredMixin, DetailView):
    model = Tarea
    context_object_name = 'tarea'
    template_name = 'base/tarea.html'


class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'completo']
    success_url = reverse_lazy('tareas') #cargamos el sitio donde nos llevara automaticamente el sitio

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(CrearTarea, self).form_valid(form)

class EditarTarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'completo'] 
    success_url = reverse_lazy('tareas') #cargamos el sitio donde nos llevara automaticamente el sitio

class EliminarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    context_object_name = 'tarea' # Los elementos del objetos son referenciados como tareas
    success_url = reverse_lazy('tareas')