from urllib import request
from django.http import HttpResponse, JsonResponse
from .serializers_contrato import * 
from ...models import Contrato,Cliente,Dependiente,Plan

from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status

from rest_framework.decorators import api_view

def ObtenerJSONContrato(contrat):
    data=contrat       
    dataContrato={
        "porcentajeComisionAgente": data["porcentajeComision"],
        "fechaIngreso": data["fechaIngreso"].split("T")[0],
        "fechaVigencia": data["fechaVigencia"].split("T")[0],
        "fechaPrimerCuota": data["fechaPrimerCuota"].split("T")[0],
        
        "valorPrimeraCuota": data["valorPrimeraCuota"],
        "valorPagoAnual": data["valorPagoAnual"],
        "modalidadPrima": data["modalidadPrima"],
        "is_active": 1,
    }    
    if data["idContrato"] ==0:
        dataContrato["codigoContrato"]=data["codigoContrato"]
    return dataContrato


def crearContrato(contrat):     
    dataContrato = ObtenerJSONContrato(contrat)    
    contrato = ContratoCreateSerializer(data=dataContrato)
    if not contrato.is_valid():
        raise Exception(contrato.errors)    
    objContrato=contrato.save()
    guardarDatos(contrat,objContrato)


def updateContrato(contrat):
    dataContrato = ObtenerJSONContrato(contrat)      
    objContrato = Contrato.objects.get(pk=contrat["idContrato"]) 
    if objContrato.codigoContrato != contrat["codigoContrato"]:
        objContrato.codigoContrato = contrat["codigoContrato"]
    ContratoSerializer = ContratoCreateSerializer(objContrato,data=dataContrato)
    if not ContratoSerializer.is_valid():
        raise Exception(ContratoSerializer.errors) 
    objContratoGuardado=ContratoSerializer.save()
    guardarDatos(contrat,objContratoGuardado)


def guardarDatos(contrat,objContrato):
    dataDependientes = contrat["idsDependientes"]
    objContrato.dependientes.clear()
    for dataDependiente in dataDependientes:        
        idDependiente = dataDependiente["idDependiente"]
        
        dependiente=Dependiente.objects.get(pk=idDependiente)
        objContrato.dependientes.add(dependiente)
    
    idCliente= contrat["idCliente"]
    cliente = Cliente.objects.get(pk=idCliente)
    objContrato.idCliente=cliente

    idAgente = contrat["idAgente"]
    agente=Empleado.objects.get(pk=idAgente)
    objContrato.idAgente=agente

    idPlan=contrat["idPlan"]
    plan=Plan.objects.get(pk=idPlan)
    objContrato.idPlan=plan

    objContrato.save()    



@api_view(('GET',))
def get_contrato_cliente(request, idCliente):
    #Obtener todas las companias       
    contratos = Contrato.objects.all().filter(idCliente=idCliente)
    #Filtrar, solo companias activas, no borradas*
    contratosActivas = contratos.filter(is_active=1)
    #many=true, devolver  arreglo json
    serializer = ContratoSerializer(contratosActivas,many=True)    
    return Response(serializer.data)




class ContratoList(APIView):
    def get(self, request,  format=None):    
        contrato = Contrato.objects.all()
        contratoActivas = contrato.filter(is_active=1)
        serializer = ContratoSerializer(contratoActivas,many=True)    
        return Response(serializer.data)

    def post(self, request, format=None):           
        try:
            for i in request.data:
                contratoNuevo= i["idContrato"]
                if contratoNuevo==0:                    
                    crearContrato(i)
                else:
                    updateContrato(i)
                
            return Response("Datos Guardados", status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response("Ocurrio un error: %s " % (err), status=status.HTTP_409_CONFLICT)


class ContratoDetail(APIView):
    
   
    def get_object(self, pk):
        try:
            return Contrato.objects.get(pk=pk)
        except Contrato.DoesNotExist:
            raise Http404      
    #GET una compania por pk
    def get(self, request, pk, format=None):
        contrato = self.get_object(pk)
        serializer = ContratoSerializer(contrato)
        return Response(serializer.data)
        


    def delete(self, request, pk, format=None):  
        try:              
            self.get_object(pk).delete()            
            return Response("Datos Eliminados", status=status.HTTP_200_OK)
        except  Exception as err:
            return Response("Ocurrio un error: %s " % (err), status=status.HTTP_400_BAD_REQUEST)

