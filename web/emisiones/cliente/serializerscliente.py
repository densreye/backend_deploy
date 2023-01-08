from rest_framework import serializers

from web.emisiones.contrato.serializers_contrato import ContratoSerializer
from ...models import Contrato, Direccion, Empleado, Persona,Cliente
from ..agente.serializersagente import EmpleadoSerializer
class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        exclude = ["creado_por_usuario","creado_id_usuario","fecha_modificado","modificado_por_usuario","modificado_id_usuario"]
        #fields = "__all__"


class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        exclude = ["creado_por_usuario","creado_id_usuario","fecha_modificado","modificado_por_usuario","modificado_id_usuario"]
        #fields = "__all__"

class ClienteSerializer(serializers.ModelSerializer):
    Persona=serializers.SerializerMethodField()    
    Direccion=serializers.SerializerMethodField()
    Planes=serializers.SerializerMethodField()
    class Meta:
        model = Cliente
        exclude = ["creado_por_usuario","creado_id_usuario","fecha_modificado","modificado_por_usuario","modificado_id_usuario"]
        #fields = "__all__"
    def get_Persona(self,obj):        
        persona=obj.idPersona
        response = PersonaSerializer(persona).data
        return response
    def get_Direccion(self,obj):   
        direccion=Direccion.objects.filter(is_active=1,idPersona=obj.idPersona)
        response = DireccionSerializer(direccion,many=True)
        return response.data
    def get_Planes(self,obj):   
        planes=Contrato.objects.filter(is_active=1,idCliente=obj.idCliente)
        response = ContratoSerializer(planes,many=True)
        return response.data        

class ClientePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        exclude = ["creado_por_usuario","creado_id_usuario","fecha_modificado","modificado_por_usuario","modificado_id_usuario"]
        #fields = "__all__"

