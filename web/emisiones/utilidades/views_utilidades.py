from rest_framework.decorators import api_view
from auth_manage import files
from rest_framework.response import Response
from ...models import DocumentoSistema
from rest_framework import status

@api_view(('DELETE',))
def eliminar_documento(request,hash):    
    decodificado=files.decode(hash)
    if decodificado == None:
        return  Response("Archivo no encontrado", status=status.HTTP_404_NOT_FOUND)
    path=decodificado['path']
    documentos=DocumentoSistema.objects.all().filter(urlArchivo=hash)
    for doc in documentos:
        doc.is_active=0
        doc.save()
    files.eliminarArchivo(path)
    return  Response("Archivo Eliminado", status=status.HTTP_200_OK)