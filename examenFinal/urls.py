from . import views
from django.urls import path

app_name = 'examenFinal'

urlpatterns = [
    path('',views.index,name='index'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('obtener_info_tarea',views.obtener_info_tarea,name='obtener_info_tarea'),
    path('agregarTarea/<str:fechaCreacion>/<str:fechaEntrega>/<str:descripcion>',views.agregarTarea,name='agregarTarea'),
    path('eliminarTarea',views.eliminarTarea,name='eliminarTarea'),
    path('mostrarEditarTarea',views.mostrarEditarTarea,name='mostrarEditarTarea'),
    
] 
