import imp
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .serializers import CompaniaSerializer,PlanSerializer,DeducibleSerializer,PlanPostSerializer,DeducibleDeleteSerializer
from .models import Compania,Plan,Deducible
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
import json
from rest_framework.decorators import api_view
# Create your views here.
def index(request):
    return HttpResponse("<h2>web</h2>")

@api_view(('GET',))
def get_plan_compania(request, idCompania):
    #Obtener todas las companias       
    planes = Plan.objects.all().filter(idCompania=idCompania)
    #Filtrar, solo companias activas, no borradas*
    planesActivas = planes.filter(is_active=1)
    #many=true, devolver  arreglo json
    serializer = PlanSerializer(planesActivas,many=True)    
    return Response(serializer.data)


#Obtener Todas las Companias o crear una nueva
class PLanList(APIView):
    #GET list de companias
    def get(self, request, format=None):
       #Obtener todas las companias
       planes = Plan.objects.all().order_by("nombrePlan").select_related('idCompania')
       #Filtrar, solo companias activas, no borradas*
       planesActivas = planes.filter(is_active=1)
       
       
       #many=true, devolver  arreglo json
       serializer = PlanSerializer(planesActivas,many=True)
       #return JsonResponse(serializer.data,safe=False)
       return Response(serializer.data)
    #CREATE una nueva compania
    def post(self, request, format=None):
        serializer = PlanPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PLanDetail(APIView):
    
    #Retrieve, update or delete a snippet instance.
    
    def get_object(self, pk):
        try:
            return Plan.objects.get(pk=pk)
        except Plan.DoesNotExist:
            raise Http404
    #GET una compania por pk
    def get(self, request, pk, format=None):
        plan = self.get_object(pk)
        serializer = PlanSerializer(plan)
        return Response(serializer.data)
    #UPDATE los datos de la compania pk=?pk
    def put(self, request, pk, format=None):
        plan = self.get_object(pk)
        serializer = PlanPostSerializer(plan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #DELETE ,actualiza el estado de la compania a "no activo"
    def delete(self, request, pk, format=None):
        #deducibles=Deducible.objects.all().select_related("idPlan").filter(idPlan=pk)
        #if(deducibles.count()!=0):
        #    return Response(status=status.HTTP_409_CONFLICT)  
        try:            
            plan = self.get_object(pk).delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
"""         deducibles.update(is_active=0)        
        plan = self.get_object(pk)    
        actualiza_activo ={"is_active":0}
        serializer = PlanPostSerializer(plan, data=actualiza_activo)
        if serializer.is_valid():
            serializer.save()            
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) """
         


#------------------------------------------------------------------------------------------------------------------------

#Obtener Todas las Companias o crear una nueva
class DeducibleList(APIView):
    #GET list de companias
    def get(self, request, format=None):
       #Obtener todas las companias
       deducibles = Deducible.objects.all().order_by("idDeducible")
       
       #Filtrar, solo companias activas, no borradas*
       planesActivas = deducibles.filter(is_active=1)
       #many=true, devolver  arreglo json
       serializer = DeducibleSerializer(planesActivas,many=True)
       #return JsonResponse(serializer.data,safe=False)
       return Response(serializer.data)
    #CREATE una nueva compania
    def post(self, request, format=None):
        serializer = DeducibleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeducibleDetail(APIView):
    
    #Retrieve, update or delete a snippet instance.
    
    def get_object(self, pk):
        try:
            return Deducible.objects.get(pk=pk)
        except Deducible.DoesNotExist:
            raise Http404
    #GET una compania por pk
    def get(self, request, pk, format=None):
        deducible = self.get_object(pk)
        serializer = DeducibleSerializer(deducible)
        return Response(serializer.data)
    #UPDATE los datos de la compania pk=?pk
    def put(self, request, pk, format=None):
        deducible = self.get_object(pk)
        serializer = DeducibleSerializer(deducible, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #DELETE ,actualiza el estado de la compania a "no activo"
    def delete(self, request, pk, format=None):
        deducible = self.get_object(pk)
        print(deducible)
        actualiza_activo ={"is_active":0}
        serializer = DeducibleDeleteSerializer(deducible, data=actualiza_activo)
        if serializer.is_valid():
            serializer.save()        
            return Response(serializer.data)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)