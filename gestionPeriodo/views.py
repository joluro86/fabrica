from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages

from gestionPeriodo.models import CalendarioAcademico, Facultad, SemestreAcademico

# Create your views here.

def index(request):
    facultades = Facultad.objects.all().order_by('nombre')

    context = {
        'facultades': facultades
    }
    return render(request, 'index.html', context)

def guardar(request):
    if request.method == 'POST':
        id_facultad = int(request.POST.get('facultad'))

        if int(id_facultad) ==0:
            messages.warning(request, "Debe seleccionar una Facultad")
            form_data = request.POST.copy()
            form_data['error'] = True
            facultades = Facultad.objects.all().order_by('nombre')
            return HttpResponse(render(request, 'index.html', {'form_data': form_data, 'facultades':facultades}), status=400)

        facultad = Facultad.objects.get(id=id_facultad)
        

        fecha_inicio_matricula = request.POST.get('fecha_inicio_matricula') 
        fecha_final_matricula = request.POST.get('fecha_final_matricula') 

        if fecha_inicio_matricula>fecha_final_matricula:
            messages.warning(request, "Fecha de inicio de matricula debe ser menor a la fecha final.")
            form_data = request.POST.copy()
            form_data['error'] = True
            facultades = Facultad.objects.all().order_by('nombre')
            return HttpResponse(render(request, 'index.html', {'form_data': form_data, 'facultades':facultades}), status=400)

        fecha_inicio_ajustes = request.POST.get('fecha_inicio_ajustes') 
        fecha_final_ajustes = request.POST.get('fecha_final_ajustes') 

        if fecha_inicio_ajustes>fecha_final_ajustes:
            messages.warning(request, "Fecha de inicio de ajustes debe ser menor a la fecha final.")
            form_data = request.POST.copy()
            form_data['error'] = True
            facultades = Facultad.objects.all().order_by('nombre')
            return HttpResponse(render(request, 'index.html', {'form_data': form_data, 'facultades':facultades}), status=400)

        calendario = CalendarioAcademico()
        calendario.facultad = facultad
        calendario.fecha_inicio_matricula = fecha_inicio_matricula
        calendario.fecha_final_matricula = fecha_final_matricula
        calendario.fecha_inicio_ajustes = fecha_inicio_ajustes
        calendario.fecha_final_ajustes = fecha_final_ajustes
        calendario.save()

        fecha_inicio_semestre = request.POST.get('fecha_inicio_semestre')
        fecha_final_semestre = request.POST.get('fecha_final_semestre') 

        if fecha_inicio_semestre>fecha_final_semestre:
            messages.warning(request, "Fecha de inicio de semestre debe ser menor a la fecha final.")
            form_data = request.POST.copy()
            form_data['error'] = True
            facultades = Facultad.objects.all().order_by('nombre')
            return HttpResponse(render(request, 'index.html', {'form_data': form_data, 'facultades':facultades}), status=400)

        
        fecha_limite_40porciento = request.POST.get('fecha_limite_40porciento')
        fecha_inicio_habilitacion = request.POST.get('fecha_inicio_habilitacion')
        fecha_final_habilitacion = request.POST.get('fecha_final_habilitacion') 
        fecha_cierre_periodo_academico = request.POST.get('fecha_cierre_periodo_academico') 

        semestre = SemestreAcademico()
        semestre.fecha_inicio_semestre = fecha_inicio_semestre
        semestre.fecha_culminacion_semestre = fecha_final_semestre
        semestre.fecha_limite_40porciento = fecha_limite_40porciento
        semestre.fecha_inicio_habilitacion = fecha_inicio_habilitacion
        semestre.fecha_culminacion_habilitacion = fecha_final_habilitacion
        semestre.fecha_cierre_periodo_academico = fecha_cierre_periodo_academico
        semestre.save()

        print(facultad) 
        print(fecha_inicio_matricula)  
        print(fecha_final_matricula) 
        print(fecha_inicio_ajustes)
        print(fecha_final_ajustes)

        print(fecha_inicio_semestre)
        print(fecha_final_semestre)
        print(fecha_limite_40porciento)
        print(fecha_inicio_habilitacion)
        print(fecha_final_habilitacion)
        print(fecha_cierre_periodo_academico)



    return HttpResponse(facultad)
