from django.http import HttpResponse, JsonResponse
from .serializers_preexistencia import PreexistenciaSerializer,DocumentoPreexistenciaSerializer,DocumentoSistemaSerializer
from ...models import Dependiente, Persona,Cliente,Preexistencia,DocumentoSistema
from ..cliente.serializerscliente import ClientePostSerializer
from ..dependiene.serializersdependiente import DependienteSerializer 

from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view

from auth_manage import files
from django.views.decorators.csrf import csrf_exempt
def ObtenerJSONDatosFinancieros(request):
        data=request.data
        dataPersona={
            "idPreexistencia": data["idPreexistencia"],
            "esTitular": data["esTitular"],
            "diagnosticoDetalle": data["diagnosticoDetalle"],
            "inicioEnfermedad": data["inicioEnfermedad"].split("T")[0],
            
            "continuaEnfermedad": data["continuaEnfermedad"],
            "tratamientoResultados": data["tratamientoResultados"],

            "descripcionEstadoActual": data["descripcionEstadoActual"],

            "idCliente": data["idCliente"],
            "idDependiente": data["idDependiente"],

            "is_active": 1,
        }
        return dataPersona


@api_view(('GET',))
def get_preexistencia_persona(request, idPersona,esTitular):    
    if esTitular==1:
        clienteObj=Cliente.objects.get(pk=idPersona)
        preexistenciaObj=clienteObj.idPreexistencia
        serializer=PreexistenciaSerializer(preexistenciaObj)
        return Response(serializer.data) 
    else:
        dependienteObj=Dependiente.objects.get(pk=idPersona)
        preexistenciaObj=dependienteObj.idPreexistencia
        serializer=PreexistenciaSerializer(preexistenciaObj)
        return Response(serializer.data) 


class PreexistenciaList(APIView):
    def get(self, request,  format=None):    
        preexistencias = Preexistencia.objects.all()
        preexistenciasActivas = preexistencias.filter(is_active=1)
        serializer = PreexistenciaSerializer(preexistenciasActivas,many=True)    
        return Response(serializer.data)

    def post(self, request, format=None):           
        try: 
            datos=ObtenerJSONDatosFinancieros(request)
            serializer=PreexistenciaSerializer(data=datos)
            if not serializer.is_valid():
                return Response("Ocurrio un error: %s " % (serializer.errors), status=status.HTTP_409_CONFLICT)            
            objPreexistencia=serializer.save()
            if datos["esTitular"]==1:
                clienteObj=Cliente.objects.get(pk=datos["idCliente"])
                clienteObj.idPreexistencia=objPreexistencia
                try:
                    clienteObj.save()
                    #cargarArchivos(clienteObj,request.FILES.getlist('uploadFile'),True);
                except Exception as err:
                    objPreexistencia.delete()
                    return Response("Ocurrio un error con el cliente: %s " % (err), status=status.HTTP_409_CONFLICT)                                                                   
            elif datos["esTitular"]==0:                
                dependienteObj=Dependiente.objects.get(pk=datos["idDependiente"])
                dependienteObj.idPreexistencia=objPreexistencia
                try:
                    dependienteObj.save()
                    #cargarArchivos(dependienteObj,request.FILES.getlist('uploadFile'),False);
                except Exception as err:
                    objPreexistencia.delete()
                    return Response("Ocurrio un error con el depedniente: %s " % (err), status=status.HTTP_409_CONFLICT)                    
            else:
                return Response("Ocurrio un error, en identificar al titular" , status=status.HTTP_409_CONFLICT)
            
            return Response("Datos Creados", status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response("Ocurrio un error: %s " % (err), status=status.HTTP_409_CONFLICT)

def obtenerJSONDocumentoPreexistencia(dataJson):

    data={
        "urlArchivo": dataJson['jwt'],
        "ruta": dataJson['path'],
        "is_active": 1
    }
    return data


def cargarArchivos(objClienteoDependiente,archivos,esTitular):
    for file in archivos:
            if esTitular:
                rutaPadre="Clientes/"+str(objClienteoDependiente.pk)+"/Preexistencias/Titular/"+str(objClienteoDependiente.idCliente)+"/"
                js=files.guardarArchivo(file,rutaPadre+file.name)     
                datosDocumentoPreexistencia=obtenerJSONDocumentoPreexistencia(js)                 
                datosDocumentoPreexistencia["esTitular"]=1
                datosDocumentoPreexistencia["idCliente"]=str(objClienteoDependiente.pk)
            else:
                rutaPadre="Clientes/"+str(objClienteoDependiente.idCliente)+"/Preexistencias/Dependiente/"+str(objClienteoDependiente.idDependiente)+"/"
                js=files.guardarArchivo(file,rutaPadre+file.name)     
                datosDocumentoPreexistencia=obtenerJSONDocumentoPreexistencia(js)                 
                datosDocumentoPreexistencia["esTitular"]=0
                datosDocumentoPreexistencia["idDependiente"]=str(objClienteoDependiente.pk)
            datosDocumentoPreexistencia["nombreArchivo"]=file.name
            serializerDocumentoPreexistencia=DocumentoPreexistenciaSerializer(data=datosDocumentoPreexistencia)  
            if not serializerDocumentoPreexistencia.is_valid():
                raise Exception(serializerDocumentoPreexistencia.errors) 
            objDocumentoPreexistencia=serializerDocumentoPreexistencia.save()
       
def obtenerJSONDocumento(dataJson,nombreArchivo):
     
    data={
        "nombreArchivo":nombreArchivo,
        "pathArchivo": dataJson['path'],
        "urlArchivo": dataJson['jwt'],        
        "is_active": 1
        
    }
    return data


@api_view(('POST',))
def cargar_documento_preexistencia_persona(request,idPersona,esTitular):    
    archivo=request.FILES.get('uploadFile')
    if esTitular==1:
        clienteObj=Cliente.objects.get(pk=idPersona)
        rutaPadre="Clientes/"+str(clienteObj.pk)+"/Preexistencias/Titular/"+str(clienteObj.idCliente)+"/"
    else:        
        dependienteObj=Dependiente.objects.get(pk=idPersona)
        rutaPadre="Clientes/"+str(dependienteObj.idCliente.pk)+"/Preexistencias/Dependiente/"+str(dependienteObj.idDependiente)+"/"
    js=files.guardarArchivo(archivo,rutaPadre+archivo.name)   
    
    data=obtenerJSONDocumento(js,archivo.name)    

    serializerDocumento=DocumentoSistemaSerializer(data=data)
    if not serializerDocumento.is_valid():
        Response("Ocurrio un error, los datos del archivo no son validos: %s" % (serializerDocumento.errors), status=status.HTTP_409_CONFLICT)
    serializerDocumento.save()
    return Response("Archivo Creado", status=status.HTTP_201_CREATED)


