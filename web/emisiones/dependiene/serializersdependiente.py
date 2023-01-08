from rest_framework import serializers
from ...models import Persona,Cliente,Dependiente

class DependienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependiente
        exclude = ["creado_por_usuario","creado_id_usuario","fecha_modificado","modificado_por_usuario","modificado_id_usuario"]
        #fields = "__all__"

