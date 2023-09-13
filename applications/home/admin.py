from django.contrib import admin
from applications.home.models import Ciudad, Persona, Habilidades

# Register your models here.

admin.site.register(Habilidades)
class ciudadAdmin(admin.ModelAdmin):
    list_display = ('id', 'Descripcion', 'short_name', 'estado')

admin.site.register(Ciudad, ciudadAdmin)

class personaAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Apellido', 'FechaNacimiento', 'ciudad')
    list_filter = ('ciudad', 'habilidades',)
    filter_horizontal = ('habilidades',)

admin.site.register(Persona, personaAdmin)