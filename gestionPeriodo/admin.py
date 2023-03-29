from django.contrib import admin
from import_export.admin import ImportExportModelAdmin 
from import_export import resources

from gestionPeriodo.models import *

class FacultadResource(resources.ModelResource):
    class Meta:
        model = Facultad
class Facultad_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'nombre')
    class Meta:
        model = Facultad
admin.site.register(Facultad, Facultad_Admin)

class CalendarioAcademicoResource(resources.ModelResource):
    class Meta:
        model = CalendarioAcademico
class CalendarioAcademico_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('facultad','fecha_inicio_matricula', 'fecha_final_matricula', 'fecha_inicio_ajustes', 'fecha_final_ajustes')
    class Meta:
        model = CalendarioAcademico
admin.site.register(CalendarioAcademico, CalendarioAcademico_Admin)

class SemestreAcademicoResource(resources.ModelResource):
    class Meta:
        model = SemestreAcademico
class SemestreAcademico_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('fecha_inicio_semestre','fecha_culminacion_semestre', 'fecha_limite_40porciento', 'fecha_inicio_habilitacion', 'fecha_culminacion_habilitacion', 'fecha_cierre_periodo_academico')
    class Meta:
        model = SemestreAcademico
admin.site.register(SemestreAcademico, SemestreAcademico_Admin)
