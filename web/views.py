import imp
from django.shortcuts import render
from django.http import HttpResponse
from .serializers import CompaniaSerializer
from .models import Compania,Plan
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
import json
# Create your views here.
def index(request):
    return HttpResponse("<h2>web</h2>")

#Obtener Todas las Companias o crear una nueva
class CompaniaList(APIView):
    #GET list de companias
    def get(self, request, format=None):
       #Obtener todas las companias
       companias = Compania.objects.all().order_by("nombreCompania")
       #Filtrar, solo companias activas, no borradas*
       companiasActivas = companias.filter(is_active=1)
       #many=true, devolver  arreglo json
       serializer = CompaniaSerializer(companiasActivas,many=True)
       #return JsonResponse(serializer.data,safe=False)
       return Response(serializer.data)
    #CREATE una nueva compania
    def post(self, request, format=None):
        serializer = CompaniaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CampaniaDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Compania.objects.get(pk=pk)
        except Compania.DoesNotExist:
            raise Http404
    #GET una compania por pk
    def get(self, request, pk, format=None):
        compania = self.get_object(pk)      
        serializer = CompaniaSerializer(compania)
        return Response(serializer.data)
    #UPDATE los datos de la compania pk=?pk
    def put(self, request, pk, format=None):
        compania = self.get_object(pk)
        serializer = CompaniaSerializer(compania, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #DELETE ,actualiza el estado de la compania a "no activo"
    def delete(self, request, pk, format=None):
        #Comprobar si existen datos comprometidos
        planes = Plan.objects.all().select_related("idCompania").filter(idCompania=pk)        
        if(planes.count()!=0):
            return Response(status=status.HTTP_409_CONFLICT)   
        
        try:
            
            compania = self.get_object(pk).delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
          
        
"""         #obtener la compania pk=?pk
        compania = self.get_object(pk)
        #Datos a actualizar en el objeto
        actualiza_activo ={"is_active":0}
        #se crea un objeto serializdor, donde se hace el reemplazo de datos
        serializer = CompaniaSerializer(compania, data=actualiza_activo)
        #si todo es correcto se guarda el objeto
        if serializer.is_valid():
            #cuando se elimina una compania se eliminan sus planes
            planes = Plan.objects.all().select_related("idCompania").filter(idCompania=pk).update(is_active=0)
            #se guardan los datos
            serializer.save()
            #se responde con los datos actuales
            return Response(serializer.data)
        #si no es correcto se envia un error
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) """
        
