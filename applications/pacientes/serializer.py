from rest_framework import serializers
from .models import Pacientes

class PacientesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pacientes
        fields = (
            'Nombre',
            'Apellido',
            'TipoDocumento',
            'NroDocumento',
            'Celular',
            'Email',
            'Direccion',
            'Estado',
        )