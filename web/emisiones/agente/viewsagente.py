
from xml.etree.ElementTree import tostring
from django.http import HttpResponse

from auth_manage.models import Cliente
from .serializersagente import EmpleadoSerializer,PersonaSerializer,DireccionSerializer
from web.models import Empleado, Direccion, Persona,Cargo
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status

def index(request):
    return HttpResponse("<h2>web21</h2>")
def ObtenerJSONPersona(request):
        dataPersona={
            "nombre": request.data["nombre"],
            "apellido": request.data["apellido"],
            "tipodeIdentificacion": request.data["tipoDeIdentificacion"],
            "numeroIdentificacion": request.data["numeroIdentificacion"],
            "fechaNacimiento":request.data["fechaNacimiento"].split("T")[0],
            
            "sexo": request.data["sexo"],
            "estadoCivil": request.data["estadoCivil"],
            "tipoPersona": "empleado",
            "is_active": 1,
        }
        return dataPersona

def SerializarPersona(request):        
        dataPersona=ObtenerJSONPersona(request)
        persona=PersonaSerializer(data=dataPersona)
        return persona  
def ObtenerJSONEmpleado(request,idPersona,idCargo):
    datos=request.data 
    dataEmpleado={
        "idPersona":idPersona,
        "fechaIngresoNoboa":datos["ingresoNoboa"].split("T")[0],
        "idCargo":idCargo,
        "celular":datos["celular"],
        "correo":datos["correo"],
        "is_active": 1,        
    }
    return dataEmpleado
def SerializarEmpleado(request,idPersona,idCargo):
    dataEmpleado=ObtenerJSONEmpleado(request,idPersona,idCargo)
    empleado=EmpleadoSerializer(data=dataEmpleado)
    return empleado
def ObtenerJSONDireccion(request,idPersona):
    datos=request.data 
    dataDireccion={
        "idPersona": idPersona,
        "tipoDireccion": datos["tipoDireccion"],
        "pais": datos["pais"],
        "provincia": datos["provincia"],
        "ciudad": datos["ciudad"],
        "datoDireccion": datos["datoDireccion"],
        "is_active": 1,
    }     
    return dataDireccion
def SerializarDireccion(request,idPersona):
    datosDireccion=ObtenerJSONDireccion(request,idPersona)
    direccion=DireccionSerializer(data=datosDireccion)
    return direccion
class AgenteList(APIView):
    def get(self, request, format=None):
       #Obtener todas las companias       
       todosEmpleados = Empleado.objects.all().select_related("idCargo")
       cargoAgente=Cargo.objects.get(descripcion="Agente").pk
       agentes=todosEmpleados.filter(idCargo=cargoAgente)
       #Filtrar, solo companias activas, no borradas*
       agentesActivas = agentes.filter(is_active=1)
       #many=true, devolver  arreglo json
       serializer = EmpleadoSerializer(agentesActivas,many=True)
       #return JsonResponse(serializer.data,safe=False)
       return Response(serializer.data)    

    def post(self, request, format=None): 
        try:
            persona=SerializarPersona(request)
            if not persona.is_valid():
                return Response("Ya existe una persona con esa identificación", status=status.HTTP_406_NOT_ACCEPTABLE)
            objPersona=persona.save()
            idPersona=objPersona.idPersona
            #if not Cargo.objects.filter(descripcion="Agente").exists():
            #        Cargo.objects.create(descripcion="Agente")
            cargoAgente=Cargo.objects.get(descripcion="Agente")
            print(cargoAgente.idCargo)
            empleado=SerializarEmpleado(request,idPersona,cargoAgente.idCargo)
            if not empleado.is_valid():
                objPersona.delete()
                return Response("Error en los datos del Agente", status=status.HTTP_406_NOT_ACCEPTABLE)
            direccion=SerializarDireccion(request,idPersona)
            if not direccion.is_valid():
                return Response("Error en los datos del Agente", status=status.HTTP_406_NOT_ACCEPTABLE)            
            empleado.save()
            direccion.save()
            return Response("Agente Creado", status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response("Ocurrio un error "+tostring(err), status=status.HTTP_406_NOT_ACCEPTABLE)
class AgenteDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Empleado.objects.get(pk=pk)
        except Empleado.DoesNotExist:
            raise Http404      
    #GET una compania por pk
    def get(self, request, pk, format=None):
        cliente = self.get_object(pk)
        serializer = EmpleadoSerializer(cliente)
        return Response(serializer.data)    
    def delete(self, request, pk, format=None):  
        try:              
            agente = self.get_object(pk).idPersona.pk
            persona=Persona.objects.get(pk=agente).delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def put(self, request, pk, format=None):
        try:

            objAgente=self.get_object(pk)
            objPersona = objAgente.idPersona
            dataPersona=ObtenerJSONPersona(request)
            persona=PersonaSerializer(objPersona,data=dataPersona)

            dataAgente=ObtenerJSONEmpleado(request,objPersona.pk,objAgente.idCargo.pk)
            agente=EmpleadoSerializer(objAgente,data=dataAgente)
            if request.data["idDireccion"]==0:
                direccion=SerializarDireccion(request,objPersona.pk)
            else:
                dataDireccion=ObtenerJSONDireccion(request,objPersona.pk)
                objDireccion=Direccion.objects.get(pk=request.data["idDireccion"]) 
                direccion=DireccionSerializer(objDireccion,data=dataDireccion)
            if not persona.is_valid() or not agente.is_valid() or not direccion.is_valid() :
                return Response("Error en los datos del Agente", status=status.HTTP_406_NOT_ACCEPTABLE)
            persona.save()
            agente.save()
            direccion.save()
            return Response("Datos actualizados", status=status.HTTP_200_OK)
        except Exception as err:
            return Response("Ocurrio un error ", status=status.HTTP_406_NOT_ACCEPTABLE)        