
from django.http import HttpResponse
from .serializerscliente import DireccionSerializer, PersonaSerializer,ClienteSerializer,ClientePostSerializer
from web.models import Cliente, Direccion, Persona

from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.
def index(request):
    return HttpResponse("<h2>web21</h2>")


def SerializarDirecciones(direcciones,idPersona):
        for direccion in direcciones:
            dataDireccion={
            "idPersona": idPersona,
            "tipoDireccion": direccion["tipoDireccion"],
            "pais": direccion["pais"],
            "provincia": direccion["provincia"],
            "ciudad": direccion["ciudad"],
            "datoDireccion": direccion["datoDireccion"],
            "is_active": 1,
            }   
            idDireccion=direccion["idDireccion"]         
            if idDireccion==0:

                direcSerializer=DireccionSerializer(data=dataDireccion)
                if direcSerializer.is_valid():
                    
                    direcSerializer.save()
                else:
                    raise Exception("Direccion No valida")
            else:
                objDireccion=Direccion.objects.get(pk=idDireccion)
                direcSerializer=DireccionSerializer(objDireccion,data=dataDireccion)
                if direcSerializer.is_valid():
                    
                    direcSerializer.save()
                else:
                    print(idPersona)
                    raise Exception("Actualización de dirección No valida")                
def ObtenerJSONPersona(request):
        dataPersona={
            "nombre": request.data["nombre"],
            "apellido": request.data["apellido"],
            "tipodeIdentificacion": request.data["tipoDeIdentificacion"],
            "numeroIdentificacion": request.data["numeroIdentificacion"],
            "fechaNacimiento":request.data["fechaNacimiento"].split("T")[0],

            "sexo": request.data["sexo"],
            "estadoCivil": request.data["estadoCivil"],
            "tipoPersona": "cliente",
            "is_active": 1,
        }
        return dataPersona

def SerializarPersona(request):        
        dataPersona=ObtenerJSONPersona(request)
        persona=PersonaSerializer(data=dataPersona)
        return persona    

def ObtenerJSONCliente(request,idPersona):
    dataCliente={
        "idPersona":idPersona,
        "talla": request.data["talla"],
        "peso": request.data["peso"],
        "esBeneficiario": "1",
        "celular": request.data["celular"],
        "correo": request.data["correo"],
        "referidoNombre": request.data["referidoNombre"],
        "referidoCorreo": request.data["referidoCorreo"],
        "referidoCelular": request.data["referidoCelular"],
        "is_active": 1,
        "ingresoNoboa": request.data["ingresoNoboa"].split("T")[0],
        "agenteAsignado": request.data["agenteAsignado"],
    }
    return dataCliente 

def SerializarCliente(request,idPersona):
    dataCliente=ObtenerJSONCliente(request,idPersona)    
    cliente=ClientePostSerializer(data=dataCliente)
    if cliente.is_valid():
        return cliente
    else:
        raise Exception(cliente.errors)

#Obtener Todas las Companias o crear una nueva
class ClienteList(APIView):
    #GET list de companias
    #permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
       #Obtener todas las companias       
       clientes = Cliente.objects.all()
       #Filtrar, solo companias activas, no borradas*
       clientesActivas = clientes.filter(is_active=1)
       #many=true, devolver  arreglo json
       serializer = ClienteSerializer(clientesActivas,many=True)
       #return JsonResponse(serializer.data,safe=False)
       return Response(serializer.data)
    #CREATE una nueva Cliente
    def post(self, request, format=None):           
        direcciones=request.data["direcciones"]     
        persona=SerializarPersona(request)
        if persona.is_valid():
            objPersona=persona.save()
            idPersona=objPersona.idPersona
            try:
                cliente=SerializarCliente(request,idPersona)
            except Exception  as e:            
                return Response(e,status=status.HTTP_400_BAD_REQUEST)
            cliente.save()

            try:
                SerializarDirecciones(direcciones,idPersona)
            except:      
                return Response("Direccion No valida",status=status.HTTP_400_BAD_REQUEST)            
            return Response("Cliente Creado", status=status.HTTP_201_CREATED)
        else:
            return Response("Ya existe una persona con esa identificación", status=status.HTTP_201_CREATED)



class ClienteDetail(APIView):
    
    #Retrieve, update or delete a snippet instance.
    def post(self, request, pk, format=None):
        try:
            pkDireccion=request.data["idDireccion"]
            print(pkDireccion)
            direccion=Direccion.objects.get(pk=pkDireccion).delete()            
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)      
    def get_object(self, pk):
        try:
            return Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            raise Http404      
    #GET una compania por pk
    def get(self, request, pk, format=None):
        cliente = self.get_object(pk)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)
    #UPDATE los datos de la compania pk=?pk
    def put(self, request, pk, format=None):
        print(pk)        
        cliente = self.get_object(pk)
        persona = cliente.idPersona
        dataCliente=ObtenerJSONCliente(request,persona.pk)
        dataPersona=ObtenerJSONPersona(request)
        personaSerializer=PersonaSerializer(persona,data=dataPersona)
        clienteSerializer=ClientePostSerializer(cliente,data=dataCliente)
        if personaSerializer.is_valid():
            personaSerializer.save()
            if clienteSerializer.is_valid():
                clienteSerializer.save()
                direcciones=request.data["direcciones"]   
                try:
                    SerializarDirecciones(direcciones,persona.pk)
                    return Response(status=status.HTTP_207_MULTI_STATUS)
                except:      
                    return Response("Direccion No valida",status=status.HTTP_400_BAD_REQUEST)                  
                
                return Response(status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_200_OK)
        return Response(personaSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    #DELETE ,actualiza el estado de la compania a "no activo"
    def delete(self, request, pk, format=None):  
        try:              
            cliente = self.get_object(pk).idPersona.pk
            persona=Persona.objects.get(pk=cliente).delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

