from django.urls import path
from . import views

urlpatterns = [
    path('', views.buscar_cancion, name='buscar_cancion'),
    path('agregar/', views.agregar_cancion, name='agregar_cancion'),
    path('canciones/', views.lista_canciones, name='lista_canciones'),
    path('editar/<int:cancion_id>/', views.editar_cancion, name='editar_cancion'),
    path('eliminar/<int:cancion_id>/', views.eliminar_cancion, name='eliminar_cancion'),
]
