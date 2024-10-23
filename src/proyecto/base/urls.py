from django.urls import path
from .views import ListaPendientes, DetalleTarea

urlpatterns = [path('', ListaPendientes.as_view(), name='pendientes'),
               path('tarea/<int:pk>', DetalleTarea.as_view(), name='tarea')] # as_view() hace una lista de clases a una lista normal