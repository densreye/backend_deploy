from django.http import HttpResponse, JsonResponse
from .serializers_datos_financieros import DatosFinancierosSerializer,DocumentoFinancieroSerializer 
from ...models import DatosFinancieros,Cliente,DocumentoFinanciero
from ..cliente.serializerscliente import ClientePostSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status

from rest_framework.decorators import api_view
from auth_manage import files

def ObtenerJSONDatosFinancieros(request):
        data=request.data
        dataPersona={
            "idCliente": data["idCliente"],
            "razonSocial": data["razonSocial"],
            "tipoActividadEconomica": data["tipoActividadEconomica"],
            "actividadEconomicaPrincipal": data["actividadEconomicaPrincipal"],
            
            "tiempoEmpleo": data["tiempoEmpleo"],
            "cargo": data["cargo"],
            "ingresoMensual": data["ingresoMensual"],
            "ingresoExtra": data["ingresoExtra"],
            "actividadExtra": data["actividadExtra"],
            "totalIngresos": data["totalIngresos"],
            "totalActivos": data["totalActivos"],
            "totalEgresos": data["totalEgresos"],
            "totalPasivos": data["totalPasivos"],
            "is_active": 1,
        }
        return dataPersona

def SerializarDatosFinancieros(request):        
        dataDatosFinancieros=ObtenerJSONDatosFinancieros(request)
        datosFinancieros=DatosFinancierosSerializer(data=dataDatosFinancieros)
        return datosFinancieros  


@api_view(('GET',))
def get_datos_financieros_cliente(request, idCliente):     
    cliente = Cliente.objects.all().get(pk=idCliente)
    serializer = DatosFinancierosSerializer(cliente.idDatosFinancieros).data     
    return Response(serializer)
@api_view(('DELETE',))
def eliminar_documento_financiero(request, idDocumento):     
    try:              
        objDocumento=DocumentoFinanciero.objects.get(pk=idDocumento)           
        files.eliminarArchivo(objDocumento.descripcionDocumento)
        objDocumento.delete() 
        return Response("Datos Eliminados", status=status.HTTP_200_OK)
    except  Exception as err:
        return Response("Ocurrio un error: %s " % (err), status=status.HTTP_400_BAD_REQUEST)         


def obtenerJSONDocumentoFinanciero(dataJson):
    documento=DocumentoFinanciero()    
    data={
        "urlArchivo": dataJson['jwt'],
        "descripcionDocumento": dataJson['path'],
        "is_active": 1
    }
    return data


class DatosFinancierosList(APIView):
    #GET list de companias
    def get(self, request,  format=None):
    
        #Obtener todas las companias       
        datosFinancieros = DatosFinancieros.objects.all()
        #Filtrar, solo companias activas, no borradas*
        datosFinancierosActivas = datosFinancieros.filter(is_active=1)
        #many=true, devolver  arreglo json
        serializer = DatosFinancierosSerializer(datosFinancierosActivas,many=True)
        #return JsonResponse(serializer.data,safe=False)
        return Response(serializer.data)
    #CREATE una nueva Cliente
    def post(self, request, format=None):           
        try:
            print(request.user)
            clienteObj=Cliente.objects.get(pk=request.data["idCliente"])
            #if  DatosFinancieros.objects.filter(pk=clienteObj.idDatosFinancieros_id).exists():
            #    return Response("Datos Financieros ya creados", status=status.HTTP_406_NOT_ACCEPTABLE)    
            datos=ObtenerJSONDatosFinancieros(request)
            
            datosFinancieros=DatosFinancierosSerializer(data=datos)
            if not datosFinancieros.is_valid():        
                return Response("Error en los Datos Financieros: %s" % (datosFinancieros.errors), status=status.HTTP_406_NOT_ACCEPTABLE)
            objDatosFinancieros=datosFinancieros.save()
            
            updateCliente=ClientePostSerializer(clienteObj,data={"idDatosFinancieros":objDatosFinancieros.pk,"idPersona":clienteObj.idPersona_id})
            if not updateCliente.is_valid():
                return Response("Error en los Datos Cliente: %s" % (updateCliente.errors), status=status.HTTP_406_NOT_ACCEPTABLE)
            objCliente=updateCliente.save()

            for file in request.FILES.getlist('uploadFile'):
                rutaPadre="Clientes/"+str(objCliente.idCliente)+"/Datosfinancieros/"
                js=files.guardarArchivo(file,rutaPadre+file.name)     
                datosDocumentoFinanciero=obtenerJSONDocumentoFinanciero(js) 
                serializerDocumentoFinanciero=DocumentoFinancieroSerializer(data=datosDocumentoFinanciero)  
                if not serializerDocumentoFinanciero.is_valid():
                    raise Exception(serializerDocumentoFinanciero.errors) 
                objDocumentoFinanciero=serializerDocumentoFinanciero.save()
                objDocumentoFinanciero.idCliente=objCliente
                objDocumentoFinanciero.save()
            return Response("Datos Creados", status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response("Ocurrio un error: %s " % (err), status=status.HTTP_409_CONFLICT)




class DatosFinancierosDetail(APIView):
    
    def get_object(self, pk):
        try:
            return DatosFinancieros.objects.get(pk=pk)
        except DatosFinancieros.DoesNotExist:
            raise Http404      
    #GET una compania por pk
    def get(self, request, pk, format=None):
        datosFinancieros = self.get_object(pk)
        serializer = DatosFinancierosSerializer(datosFinancieros)
        return Response(serializer.data)            