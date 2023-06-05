from rest_framework import serializers
from .models import Rol, Usuario, Servicio, Publicacion 

class RolSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ServicioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'        

class PublicacionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = '__all__'                