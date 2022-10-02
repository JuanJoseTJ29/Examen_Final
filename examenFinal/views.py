from django.shortcuts import render
from django.urls import reverse
from .models import tareasExamen, usuariosFinal
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
import json

# Create your views here.
def index(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        passwordUsuario = request.POST.get('passwordUsuario')
        #Validacion de informacion
        usuario_registrado = 0
        usuarios_totales = usuariosFinal.objects.all()

        for usuario in usuarios_totales:
            if usuario.usuario == nombreUsuario and usuario.contra == passwordUsuario:
                usuario_registrado = 1
        
        if usuario_registrado == 1:
            return HttpResponseRedirect(reverse('examenFinal:dashboard'))
        else:
            return render(request,'examenFinal/ingresar.html',{
                'mensaje':'Los datos ingresados son incorrectos',
            })
    return render(request,'examenFinal/ingresar.html')

def dashboard(request):
    return render(request,'examenFinal/dashboard.html',{
        'tareas_totales':tareasExamen.objects.all().order_by('id')
    })

# La informacion de la tarea sera devuelta como un Json
def obtener_info_tarea(request):
    id_tarea = str(request.GET.get('idTarea'))
    tareas = tareasExamen.objects.get(id=id_tarea)
    return JsonResponse({
        'mostrar_detalles': {
            'id': tareas.id,
            'fechaCreacion': tareas.fechaCreacion,
            'fechaEntrega': tareas.fechaEntrega,
            'descripcion': tareas.descripcion,
            'estadoTarea': tareas.estadoTarea
        }
    })


    
def agregarTarea(response,fechaCreacion,fechaEntrega,descripcion): 
    #Se insertan los datos de la tarea creada a la BD
    tareasExamen(fechaCreacion=fechaCreacion,fechaEntrega=fechaEntrega,descripcion=descripcion).save()
    tareas_totales = tareasExamen.objects.all()
    infoTareas  = []
    for tarea in tareas_totales:
        infoTareas.append([tarea.id,tarea.fechaCreacion,tarea.fechaEntrega,tarea.descripcion,tarea.estadoTarea])
    # Se devolvera la lista de tarea que hay y con la que se acaba de crear
    return JsonResponse({
        'tareaInformacion':infoTareas, 
    })


def eliminarTarea(request):
    id_Elimtarea= str(request.GET.get('idTarea'))
    Elimtarea = tareasExamen.objects.get(id=id_Elimtarea)
    lista_Elimtarea = [Elimtarea.id,Elimtarea.fechaCreacion,Elimtarea.fechaEntrega,Elimtarea.descripcion,Elimtarea.estadoTarea]
    #Se eliminara la tarea de la BD 
    tareasExamen.objects.get(id=id_Elimtarea).delete()
    # Se devolvera la lista de tareas que hay y ya no aparecera la que se ha eliminado 
    return JsonResponse({
        'Elimtarea':lista_Elimtarea
    })

def editarTarea(request):
    id_editTarea = str(request.GET.get('idTarea'))
    Edittarea = tareasExamen.objects.get(id=id_Edittarea)
    return JsonResponse({
        'Editartarea':lista_editTarea
    })


