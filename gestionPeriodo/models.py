from django.db import models

# Create your models here.

class Facultad(models.Model):
    nombre= models.CharField(max_length=200, default="-")
    
    class Meta:
        verbose_name = 'Facultad'
        verbose_name_plural = 'Facultades'

    def __str__(self):
       return str(self.nombre)
    
class CalendarioAcademico(models.Model):
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)
    fecha_inicio_matricula = models.DateField()
    fecha_final_matricula = models.DateField()
    fecha_inicio_ajustes = models.DateField()
    fecha_final_ajustes = models.DateField()

    class Meta:
        verbose_name = 'Calendario Academico'
        verbose_name_plural = 'Calendario Academico'

    def __str__(self):
        return str(str(self.facultad.nombre) + " Inicio: " + str(str(self.fecha_inicio_matricula) + " termina: " + str(self.fecha_final_matricula)))
    
class SemestreAcademico(models.Model):
    fecha_inicio_semestre = models.DateField()
    fecha_culminacion_semestre = models.DateField()
    fecha_limite_40porciento = models.DateField()
    fecha_inicio_habilitacion = models.DateField()
    fecha_culminacion_habilitacion = models.DateField()
    fecha_cierre_periodo_academico = models.DateField()    

    class Meta:

        verbose_name = 'Semestre Academico'
        verbose_name_plural = 'Semestre Academico'

    def __str__(self):
        return str("Inicio semestre " + str(self.fecha_inicio_semestre) + " fin de semestre " + str(self.fecha_culminacion_semestre))

    


