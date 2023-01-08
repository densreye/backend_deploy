from rest_framework import serializers
from crm.models import *

# usuario
class UsuarioSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Usuario
        fields = '__all__'

# Persona
class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

# Empleado
class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

# prospecto -------------------------------------------
class ProspectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prospecto
        fields = '__all__'

class ProspectosesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prospectosesion
        fields = '__all__'

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class CotizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cotizacion
        fields = '__all__'

class ContactoprospectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactoprospecto
        fields = '__all__'


#---------- nuevos serializadores--------------
class Formulario_ContactenosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formulario_Contactenos
        fields = '__all__'


class OfertasSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ofertas
        fields = '__all__'
        
   