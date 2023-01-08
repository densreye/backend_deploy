from datetime import datetime
import json
import csv

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

from crm.models import Prospecto, Prospectosesion
from crm.serializers import *

from auth_manage.views import obtener_cargo
from crm.decoradores import supervisor
from crm.utilidades import es_supervisor, obtener_informacion_empleado, json_to_csv, obtener_idagente, obtener_fecha_actual



base_tipos = ['csv', 'json']

class Lista_Prospectos(APIView):
    """
    Clase manejadora de prospectos
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        ''' supervisor -> permite obtener todos los prospectos '''
        nombreusuario = request.user

        if es_supervisor(nombreusuario):
            prospectos = Prospecto.objects.all().order_by('-creado')
            serializer = ProspectoSerializer(prospectos, many=True)
            return Response(serializer.data)

        try:
            info = obtener_informacion_empleado(nombreusuario)
            idagente = info['idempleado']
            prospectos = Prospecto.objects.filter(idagente=idagente).order_by('-creado').values()
            serializer = ProspectoSerializer(prospectos, many=True)

            return JsonResponse(serializer.data, safe=False)
            
        except Exception as e:
            return Response({'msg':f'{e}'}, status=status.HTTP_400_BAD_REQUEST)

class Prospecto_CRUD(APIView):
    """
    Clase manejadora de prospecto
    """
    permission_classes = [IsAuthenticated]

    def get(self, request,idprospecto, format=None):
        ''' informacion sobre un prospecto '''
        if idprospecto == None:
            return Response({'msg':'idprospecto es requerido'}, status=status.HTTP_400_BAD_REQUEST)

        nombreusuario = request.user

        # si el usuario es supervisor regresamos la información
        if es_supervisor(nombreusuario):
            prospectos = Prospecto.objects.filter(idprospecto=idprospecto).values()
            prospectos = ProspectoSerializer(prospectos, many=True)
            return Response(prospectos.data)

        # si es un empleado buscamos su informacion
        try:
            info = obtener_informacion_empleado(nombreusuario)
            idagente = info['idempleado']
        except Exception as e:
            return Response({'msg':'sucedio un problema'}, status=status.HTTP_400_BAD_REQUEST)

        # verificamos que tenga asignado al prospecto
        try:
            prospectos = Prospecto.objects.filter(idagente=idagente, idprospecto=idprospecto)
            serializer = ProspectoSerializer(prospectos, many=True)
            return JsonResponse(serializer.data, safe=False)
        except Prospecto.DoesNotExist:
            return Response({'msg':'recurso no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request,idprospecto, format=None): 
        '''crear prospecto'''
        try:
            nombreusuario= request.user
            user = obtener_informacion_empleado(nombreusuario)
            request.data["idagente"] = user['idempleado']
            request.data['creado'] = datetime.now()
        except Exception as e:
            print(e)
            return Response({'msg':f'sucedio un problema. Prospecto no creado ${e}'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ProspectoSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        try:
            serializer.save()
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response({'msg':'sucedio un problema. Prospecto no creado'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,idprospecto, format=None):

        # validamos si es supervisor
        if es_supervisor(request.user):
            try:
                old = Prospecto.objects.filter(idprospecto = idprospecto).first()
                serializer = ProspectoSerializer(old, data= request.data)
                serializer.save()
                return Response(serializer.data)
            except Prospecto.DoesNotExist:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
        
        try:
            # obtenemos información del empleado
            info = obtener_informacion_empleado(request.user)
            idempleado = info['idempleado']
 
        except:
            return Response({'msg':'sucedio un problema. Prospecto no actualizado'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # serializamos y actualizamos
            old = Prospecto.objects.filter(idprospecto = idprospecto, idagente= idempleado).first()
            serializer = ProspectoSerializer(old, data= request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       


# Supervisor -----------------------------------------------------------

class Lista_Prospectos_Agente(APIView):
    """
    Clase manejadora de prospectos
    """
    permission_classes = [IsAuthenticated]

    @supervisor()
    def get(self, request, format=None):
        ''' supervisor -> permite obtener todos los prospectos '''
        try:
            prospectos = Prospecto.objects.all()
            prospectos = ProspectoSerializer(prospectos, many=True)
            return Response(prospectos.data, safe=False)
        except Exception as e:
            return Response({'msg':'sucedio un problema'}, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, format=None):
        '''trabajo en ello'''

class prospectosExportar(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,tipo,format= None):
        nombreusuario = request.user
        if es_supervisor(nombreusuario):
            return exportar_prospectos(tipo)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
# importar prospectos
class ProspectosImportar(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        nombreusuario = request.user
        
        # obtenemos el csv
        try:
            data = request.data.get('data')
            data = json.loads(data)
            idagente = obtener_idagente(nombreusuario)
            for p in data:
                p['idprospecto'] = None
                p['idagente'] = idagente
                p['creado'] = obtener_fecha_actual()
        except Exception as e:
            return Response({'msg':'sucedio un problema'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ProspectoSerializer(data=data, many=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            serializer.save()
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response({'msg':'sucedio un problema'}, status=status.HTTP_400_BAD_REQUEST)
        

def exportar_prospectos(tipo):
    tipo = tipo or 'json'
    try:
        prospectos = Prospecto.objects.all()
        serializer = ProspectoSerializer(prospectos, many=True)

        file_data = json.dumps(serializer.data)
            
        if tipo == 'csv':
            file_data = json_to_csv(file_data)
            response = HttpResponse(file_data, content_type='application/text charset=utf-8')
            response['Content-Disposition'] = f'attachment; filename="prospecto_backup_{datetime.now()}.csv"'
        else:
            response = HttpResponse(file_data, content_type='application/text charset=utf-8')
            response['Content-Disposition'] = f'attachment; filename="prospecto_backup_{datetime.now()}.json"'
        return response
        #return Response(serializer.data)
    except Exception as e:
        return Response({'msg':'sucedio un problema'}, status=status.HTTP_400_BAD_REQUEST)