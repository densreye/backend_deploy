from django.http import HttpResponse, JsonResponse
from .serializers_datos_facturacion import DatosFacturacionSerializer 
from ...models import Persona,Cliente,DatosFacturacion
from ..cliente.serializerscliente import ClientePostSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status

from rest_framework.decorators import api_view
from auth_manage import files

def ObtenerJSONDatosFacturacion(request):
        data=request.data
        dataFacturacion={
            "idCliente": data["idCliente"],
            "tipoFormadePago": data["tipoFormadePago"],
            "tipoDeIdentificacion": data["tipoDeIdentificacion"],
            "numeroIdentificacion": data["numeroIdentificacion"],
            
            "nombre": data["nombre"],
            "apellido": data["apellido"],
            "correo": data["correo"],
            "celular": data["celular"],
            "contactoNombre": data["ContactoNombre"],
            "contactoCorreo": data["ContactoCorreo"],
            "contactoCelular": data["ContactoCelular"],
            "nombreTarjeta": data["NombreTarjeta"],
            "nombreInstitucionBancaria": data["NombreInstitucionBancaria"],
            "numeroCuenta": data["NumeroCuenta"],
            "is_active": 1,
        }
        return dataFacturacion




@api_view(('GET',))
def get_datos_facturacion_cliente(request, idCliente):    
    cliente = Cliente.objects.all().get(pk=idCliente)    
    serializer = DatosFacturacionSerializer(cliente.idDatosFacturacion)    
    return Response(serializer.data)


from django.core.files.storage import default_storage
class DatosFacturacionList(APIView):
    def get(self, request,  format=None):    
        print("--------")
        directories, archivos=files.obtenerArchivosDirectorio("")
        for filename in archivos:
            #print(filename.__str__())
            print(filename)
        print("--------")
        datosFacturacion = DatosFacturacion.objects.all()
        datosFacturacionActivas = datosFacturacion.filter(is_active=1)
        serializer = DatosFacturacionSerializer(datosFacturacionActivas,many=True)    
        return Response(serializer.data)

    def post(self, request, format=None):           
        try:
            clienteObj=Cliente.objects.get(pk=request.data["idCliente"])
              
            datos=ObtenerJSONDatosFacturacion(request)
            
            datosFacturacion=DatosFacturacionSerializer(data=datos)
            if not datosFacturacion.is_valid():        
                return Response("Error en los Datos de Facturacion: %s" % (datosFacturacion.errors), status=status.HTTP_406_NOT_ACCEPTABLE)
            objDatosFacturacion=datosFacturacion.save()
            print(clienteObj)
            updateCliente=ClientePostSerializer(clienteObj,data={"idDatosFacturacion":objDatosFacturacion.pk,"idPersona":clienteObj.idPersona_id})
            if not updateCliente.is_valid():
                return Response("Error en los Datos Cliente: %s" % (updateCliente.errors), status=status.HTTP_406_NOT_ACCEPTABLE)
            updateCliente.save()
            return Response("Datos Guardados", status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response("Ocurrio un error: %s " % (err), status=status.HTTP_409_CONFLICT)





 
class DatosFacturacionDetail(APIView):
    
    def get_object(self, pk):
        try:
            return DatosFacturacion.objects.get(pk=pk)
        except DatosFacturacion.DoesNotExist:
            raise Http404      
    #GET una compania por pk
    def get(self, request, pk, format=None):
        datosFacturacion = self.get_object(pk)
        serializer = DatosFacturacionSerializer(datosFacturacion)
        return Response(serializer.data)            