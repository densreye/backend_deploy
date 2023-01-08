from django.http import HttpResponse, JsonResponse
from .serializersdependiente import DependienteSerializer 
from ...models import Persona,Cliente,Dependiente

from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status

from rest_framework.decorators import api_view
def ObtenerJSONDependiente(request):
    data=request.data
    
    dataDependiente={
        "idCliente": data["idCliente"],
        "talla": data["talla"],
        "peso": data["peso"],
        "nombres": data["nombres_dependiente"],
        "apellidos": data["apellidos_dependiente"],
        
        "tipoDeIdentificacion": data["tipoDeIdentificacion"],
        "numeroIdentificacion": data["numeroIdentificacion"],
        "celular": data["telefono"],
        "correo": data["correo"],
        "parentesco": data["parentesco"],
        

        "is_active": 1,
    }
    return dataDependiente


@api_view(('GET',))
def get_dependiente_cliente(request, idCliente):
    #Obtener todas las companias       
    dependientes = Dependiente.objects.all().filter(idCliente=idCliente)
    #Filtrar, solo companias activas, no borradas*
    dependientesActivas = dependientes.filter(is_active=1)
    #many=true, devolver  arreglo json
    serializer = DependienteSerializer(dependientesActivas,many=True)    
    return Response(serializer.data)


class DependienteList(APIView):
    def get(self, request,  format=None):    
        dependientes = Dependiente.objects.all()
        dependientesActivas = dependientes.filter(is_active=1)
        serializer = DependienteSerializer(dependientesActivas,many=True)    
        return Response(serializer.data)


    def post(self, request, format=None):           
        try:
            dataDependiente=ObtenerJSONDependiente(request)
            serializerDependiente=DependienteSerializer(data=dataDependiente)
            if not serializerDependiente.is_valid():
                return Response("Ocurrio un error: %s " % (serializerDependiente.errors), status=status.HTTP_409_CONFLICT)
            serializerDependiente.save()
            return Response("Datos Creados", status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response("Ocurrio un error: %s " % (err), status=status.HTTP_409_CONFLICT)
        



 
class DependienteDetail(APIView):
    
   
    def get_object(self, pk):
        try:
            return Dependiente.objects.get(pk=pk)
        except Dependiente.DoesNotExist:
            raise Http404      
    #GET una compania por pk
    def get(self, request, pk, format=None):
        dependiente = self.get_object(pk)
        serializer = DependienteSerializer(dependiente)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:                        
            dependiente = self.get_object(pk)
            datosDependiente=ObtenerJSONDependiente(request)
            serializerDependiente = DependienteSerializer(dependiente, data=datosDependiente)
            if not serializerDependiente.is_valid():
                return Response("Ocurrio un error: %s " % (serializerDependiente.errors), status=status.HTTP_409_CONFLICT)
            serializerDependiente.save()
            return Response("Datos Actualizados", status=status.HTTP_200_OK)
        except  Exception as err:
            return Response("Ocurrio un error: %s " % (err), status=status.HTTP_400_BAD_REQUEST)

        


    def delete(self, request, pk, format=None):  
        try:              
            self.get_object(pk).delete()            
            return Response("Datos Eliminados", status=status.HTTP_200_OK)
        except  Exception as err:
            return Response("Ocurrio un error: %s " % (err), status=status.HTTP_400_BAD_REQUEST)


    #UPDATE los datos de la compania pk=?pk