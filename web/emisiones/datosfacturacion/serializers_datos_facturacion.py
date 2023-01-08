from rest_framework import serializers
from ...models import  Persona,Cliente,DatosFacturacion
from auth_manage import files

# Serializers define the API representation.
class ArchivoSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=1024)
    path = serializers.CharField(max_length=1024)
    urlArchivo = serializers.CharField(max_length=1024)
    class Meta:
        fields = "__all__"

class DatosFacturacionSerializer(serializers.ModelSerializer):
    Archivos=serializers.SerializerMethodField()
    class Meta:
        model = DatosFacturacion
        exclude = ["creado_por_usuario","creado_id_usuario","fecha_modificado","modificado_por_usuario","modificado_id_usuario"]
            
    def get_Archivos(self,obj): #obj=plan
        directorios,archivos=files.obtenerArchivosDirectorio("")
        archivosConFormato=[]
        for archivo in archivos:
            urlHash=files.obtener_hash_file(archivo)
            archivosConFormato.append({
                "nombre":archivo,
                "path":"Clientes/"+archivo,
                "urlArchivo":urlHash
                })
        response=ArchivoSerializer(archivosConFormato,many=True)
        return response.data
                 

