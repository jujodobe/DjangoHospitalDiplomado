from django.db import models

# Create your models here.
class Ciudad(models.Model):

    JOB_CHOICES = (
        ('A', 'Activo'),
        ('I', 'Inactivo'),
        ('B', 'Bloqueado'),
    )

    Descripcion = models.CharField('Nombre de Ciudad', max_length=50, null=False)
    estado = models.CharField('Estado', max_length=10, null=False, choices=JOB_CHOICES)
    short_name = models.CharField('Nombre corto', max_length=5, null=True)

    class Meta:
        verbose_name = 'Tabla Ciudad'
        verbose_name_plural = 'Registro de ciudades'
        ordering = ['Descripcion']
        unique_together = ('Descripcion', 'short_name')


    def __str__(self):
        return f" {self.Descripcion} "

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=30)

    def __str__(self):
        return f"{self.habilidad}"

class Persona(models.Model):
    Nombre = models.CharField('Nombre de la persona', max_length=50)
    Apellido = models.CharField('Apellido de la persona', max_length=50)
    FechaNacimiento=models.DateField('Fecha de Nacimiento')
    Celular=models.CharField('Celular', max_length=20)
    ciudad=models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)
