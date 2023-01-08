from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from auth_manage.models import Usuario, Persona, Empleado

# from rest_framework.serializers import Serializer, FileField, ListField

# Serializers define the API representation.
class UploadSerializer(serializers.Serializer):
    file_uploaded = serializers.FileField(max_length=1024)
    path = serializers.CharField(max_length=1024)
    class Meta:
        fields = ['file_uploaded']

# usuario
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'

# usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'