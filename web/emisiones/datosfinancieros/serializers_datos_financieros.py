from rest_framework import serializers
from ...models import  Persona,Cliente,DatosFinancieros,DocumentoFinanciero



class DocumentoFinancieroSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentoFinanciero
        exclude = ["creado_por_usuario","creado_id_usuario","fecha_modificado","modificado_por_usuario","modificado_id_usuario"]
        #fields = "__all__"


class DatosFinancierosSerializer(serializers.ModelSerializer):
    DocumentosFinancieros=serializers.SerializerMethodField()
    class Meta:
        model = DatosFinancieros
        exclude = ["creado_por_usuario","creado_id_usuario","fecha_modificado","modificado_por_usuario","modificado_id_usuario"]
        #fields = "__all__"
    def get_DocumentosFinancieros(self,obj): 
        documentoFinanciero=DocumentoFinanciero.objects.filter(is_active=1,idCliente=obj.idCliente)
        response = DocumentoFinancieroSerializer(documentoFinanciero,many=True)
        return response.data        