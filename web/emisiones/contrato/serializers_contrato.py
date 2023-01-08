from rest_framework import serializers
from ...models import Plan,Dependiente,Contrato,Empleado,Compania,Persona,Cliente
from ..agente.serializersagente import EmpleadoSerializer

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        exclude = ["creado_por_usuario","creado_id_usuario","fecha_modificado","modificado_por_usuario","modificado_id_usuario"]
        #fields = "__all__"



class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        exclude = ["creado_por_usuario","creado_id_usuario","fecha_modificado","modificado_por_usuario","modificado_id_usuario"]
        #fields = "__all__"


class CompaniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compania
        exclude = ["creado_por_usuario","creado_id_usuario","fecha_modificado","modificado_por_usuario","modificado_id_usuario"]
        #fields = "__all__"


class PlanSerializer(serializers.ModelSerializer):
    Compania=serializers.SerializerMethodField()
    def get_Compania(self,obj):        
        response = CompaniaSerializer(obj.idCompania).data
        return response        
    
    class Meta:
        model = Plan
        exclude = ["creado_por_usuario","creado_id_usuario","fecha_modificado","modificado_por_usuario","modificado_id_usuario"]
        #fields = "__all__"


class DependienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependiente
        exclude = ["creado_por_usuario","creado_id_usuario","fecha_modificado","modificado_por_usuario","modificado_id_usuario"]
        #fields = "__all__"

class ContratoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        exclude = ["creado_por_usuario","creado_id_usuario","fecha_modificado","modificado_por_usuario","modificado_id_usuario"]
        #fields = "__all__"


class ContratoSerializer(serializers.ModelSerializer):
    Plan = serializers.SerializerMethodField()
    Agente = serializers.SerializerMethodField()
    dependientes = DependienteSerializer(many=True)
    Persona=serializers.SerializerMethodField()   
    Cliente= serializers.SerializerMethodField()  
    class Meta:
        model = Contrato
        exclude = ["creado_por_usuario","creado_id_usuario","fecha_modificado","modificado_por_usuario","modificado_id_usuario"]
        #fields = "__all__"
    def get_Plan(self,obj):        
        response = PlanSerializer(obj.idPlan).data
        return response        
    def get_Agente(self,obj):        
        response = EmpleadoSerializer(obj.idAgente).data
        return response        
    def get_Persona(self,obj):        
        persona=obj.idCliente.idPersona
        response = PersonaSerializer(persona).data
        return response
    def get_Cliente(self,obj):        
        cliente=obj.idCliente
        response = ClienteSerializer(cliente).data
        return response
