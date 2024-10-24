from django.urls import path
from .views import ListaPendientes, DetalleTarea, CrearTarea, EditarTarea

urlpatterns = [path('', ListaPendientes.as_view(), name='tareas'), # as_view() hace una lista de clases a una lista normal
               path('tarea/<int:pk>', DetalleTarea.as_view(), name='tarea'),
               path('crear-tarea/', CrearTarea.as_view(), name='crear-tarea'),
               path('editar-tarea/<int:pk>', EditarTarea.as_view(), name='editar-tarea')] 