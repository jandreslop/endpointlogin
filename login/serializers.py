from rest_framework import serializers
from .models import NombreUsuario

class NombreUsuarioSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    user_name =serializers.CharField()

    def create(self, data):
        nombreusuario = NombreUsuario()
        nombreusuario.user_name = data.get('user_name')
        nombreusuario.save()
        
        return nombreusuario
