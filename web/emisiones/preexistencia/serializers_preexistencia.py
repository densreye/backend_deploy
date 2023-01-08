from rest_framework import serializers
from ...models import Persona,Cliente,Preexistencia,Dependiente,DocumentoPreexistencia,DocumentoSistema
from auth_manage import files

class ArchivoSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=1024)
    path = serializers.CharField(max_length=1024)
    urlArchivo = serializers.CharField(max_length=1024)
    class Meta:
        fields = "__all__"



class PreexistenciaSerializer(serializers.ModelSerializer):
    Archivos=serializers.SerializerMethodField()
    class Meta:
        model = Preexistencia
        exclude = ["creado_por_usuario","creado_id_usuario","fecha_modificado","modificado_por_usuario","modificado_id_usuario"]
        #fields = "__all__"
    def get_Archivos(self,obj): #obj=plan
        try:
            esTitular=obj.esTitular

            if esTitular==1:
                carpeta="Clientes/"+str(obj.idCliente.pk)+"/Preexistencias/Titular/"+str(obj.idCliente.pk)+"/"
            else:
                carpeta="Clientes/"+str(obj.idCliente.pk)+"/Preexistencias/Dependiente/"+str(obj.idCliente.pk)+"/"
        except:
            return []
        archivosConFormato=[]
        try:
            directorios,archivos=files.obtenerArchivosDirectorio(carpeta)
            for archivo in archivos:
                urlHash=files.obtener_hash_file(carpeta+archivo)
                archivosConFormato.append({
                    "nombre":archivo,
                    "path":carpeta+archivo,
                    "urlArchivo":urlHash
                    })
        except:
            respuesta="No hubo archivos"

        response=ArchivoSerializer(archivosConFormato,many=True)
        return response.data
                 
          
class DependienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependiente
        #exclude = ["creado_por_usuario","creado_id_usuario","fecha_modificado","modificado_por_usuario","modificado_id_usuario"]
        fields = ["idPreexistencia","idDependiente","idCliente"]


class DocumentoPreexistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentoPreexistencia
        exclude = ["creado_por_usuario","creado_id_usuario","fecha_modificado","modificado_por_usuario","modificado_id_usuario"]
        #fields = "__all__"
""" 
class PreexistenciaSerializer(serializers.ModelSerializer):
    DocumentosPreexistencia=serializers.SerializerMethodField()
    class Meta:
        model = Preexistencia
        exclude = ["creado_por_usuario","creado_id_usuario","fecha_modificado","modificado_por_usuario","modificado_id_usuario"]
        #fields = "__all__"
    def get_DocumentosFinancieros(self,obj): 
        documentosPreexistencia=DocumentoPreexistencia.objects.filter(is_active=1,idCliente=obj.idCliente)
        response = DocumentoPreexistenciaSerializer(documentosPreexistencia,many=True)
        return response.data   """

class DocumentoSistemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentoSistema
        exclude = ["creado_por_usuario","creado_id_usuario","fecha_modificado","modificado_por_usuario","modificado_id_usuario"]
        #fields = "__all__"