from django.urls import path
from .views import ListaPendientes

urlpatterns = [path('', ListaPendientes.as_view(), name='pendientes')] # as_view() hace una lista de clases a una lista normal