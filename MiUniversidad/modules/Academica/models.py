from django.db import models

# Create your models here.

class Carrera(models.Model):
    codigo = models.Charfield(max_length=3, primary_key=True)
    nombre = models.Charfield(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=5)

class Estudiante(models.Model):
    dni = models.Charfield(max_length=8, primary_key=True)
    apellidoPaterno = models.Charfield(max_length=35)
    apellidoMaterno = models.Charfield(max_length=35)
    nombres = models.Charfield(max_length=35)
    fechaNacimiento = models.DateField()
    #lista de opciones
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    #columna con opciones
    sexo = models.Charfield(max_length=1, choices= sexos, default= 'F)
    #unimos estudiante a carrera, si se borra la carrera se borran todos los estudiantes que esten en esa carrera
    carrera = models.ForeingKey(Carrera, null=False, blank=False, on_delete=models.CASCADE)
    #el estudiante tiene una fecha limite
    vigencia = models.BooleanField(default=True)
    #para que se coloque el nombre de esa forma
    def nombreCompleto(self):
        txt = "{0} {1}. {2}"
        return tex.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

class Curso(models.Model):
    codigo =models.Charfield(max_length=6, primary_key=True)
    nombre = models.Charfield(max_length=30)
    creditos = models.PositiveSmallIntegerField() 
    docente = models.Charfield(max_length=100)

class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeingKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeingKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    fechaMatricula = models.DateTimeField(auto_now_add=True)
