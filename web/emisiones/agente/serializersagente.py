from rest_framework import serializers
from ...models import  Persona, Empleado,DocumentoEmpleado,Cargo,Direccion

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

class DocumentoEmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentoEmpleado
        exclude = ["creado_por_usuario","creado_id_usuario","fecha_modificado","modificado_por_usuario","modificado_id_usuario"]
        #fields = "__all__"

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        exclude = ["creado_por_usuario","creado_id_usuario","fecha_modificado","modificado_por_usuario","modificado_id_usuario"]
        #fields = "__all__"

class EmpleadoSerializer(serializers.ModelSerializer):
    Persona=serializers.SerializerMethodField() 
    Cargo=serializers.SerializerMethodField() 
    Direccion=serializers.SerializerMethodField() 
    class Meta:
        model = Empleado
        exclude = ["creado_por_usuario","creado_id_usuario","fecha_modificado","modificado_por_usuario","modificado_id_usuario"]
        #fields = "__all__"
    def get_Persona(self,obj):        
        persona=obj.idPersona
        response = PersonaSerializer(persona).data
        return response
    def get_Cargo(self,obj):
        cargo=obj.idCargo
        response=CargoSerializer(cargo).data
        return response
    def get_Direccion(self,obj):   
        direccion=Direccion.objects.filter(is_active=1,idPersona=obj.idPersona)
        response = DireccionSerializer(direccion,many=True)
        return response.data        