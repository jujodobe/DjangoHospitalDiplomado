from django.db import models

# Create your models here.
class Pacientes(models.Model):

    tipodoc_choices = (
        ('CI','Cedula de Identidad'),
        ('pasaporte', 'Pasaporte'),
    )

    estado_choices = (
        ('Activo', 'Activo'),
        ('Eliminado', 'Eliminado'),
        ('Bloqueado', 'Bloqueado'),
        ('Suspendido', 'Suspendido'),
    )

    Nombre = models.CharField('Nombre', max_length=30)
    Apellido = models.CharField('Apellido', max_length=30)
    TipoDocumento = models.CharField('Tipo de Documento', max_length=30, choices=tipodoc_choices)
    NroDocumento = models.CharField('N˚ de Documento', max_length=15)
    Celular = models.CharField('N˚ de Celular', max_length=20)
    Email = models.CharField('Email', max_length=50)
    Direccion = models.CharField('Direccion', max_length=30)
    Estado = models.CharField('Estado', max_length=10, choices=estado_choices)

    def __str__(self):
        return f"{self.Nombre} {self.Apellido}"