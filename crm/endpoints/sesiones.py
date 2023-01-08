from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

from crm.models import Prospecto, Prospectosesion
from crm.serializers import *

from auth_manage.views import obtener_cargo
from crm.decoradores import supervisor
from crm.utilidades import es_supervisor, obtener_informacion_empleado

tipos_sesion = ['todos', 'llamadas', 'reuniones']

tipo_llamada = 1
tipo_reunion = 2

class Lista_Sesiones_Prospecto(APIView):
    """ listar sesiones """
    permission_classes = [IsAuthenticated]
    def get(self, request, idprospecto, tipo, format=None):
        nombreusuario = request.user
        # validamos si idprospecto
        if idprospecto is None:
            return Response({'msg':'idprospecto no valido'}, status.HTTP_404_NOT_FOUND)

        if tipo not in tipos_sesion:
            return Response({'msg':f'tipo [{tipo}] no valido. valido : {tipos_sesion}'}, status.HTTP_404_NOT_FOUND)

        # si es supervisor, entregamos la información rapidamente
        if es_supervisor(nombreusuario):
            try:
                if tipo == 'todos':
                    sesiones = Prospectosesion.objects.filter(idprospecto=idprospecto).order_by('-inicio')
                if tipo == 'llamadas':
                    sesiones = Prospectosesion.objects.filter(idprospecto=idprospecto, tipo=tipo_llamada).order_by('-inicio')
                if tipo == 'reuniones':
                    sesiones = Prospectosesion.objects.filter(idprospecto=idprospecto, tipo=tipo_reunion).order_by('-inicio')
                serializer = ProspectosesionSerializer(sesiones, many=True)
                return Response(serializer.data)
            except Exception as e:
                return Response({'msg':'elemento no encontrado'}, status.HTTP_404_NOT_FOUND)

        # si es empleado validamos su información
        
        try:
            info = obtener_informacion_empleado(nombreusuario)
            idagente = info['idempleado']

            # verificamos que tenga asignado al prospecto
            es_owner = Prospecto.objects.filter(idagente=idagente, idprospecto = idprospecto).exists()
            if not es_owner:
                return Response({'msg':'no tienes acceso a este recurso'}, status.HTTP_401_UNAUTHORIZED)

            if tipo == 'todos':
                sesiones = Prospectosesion.objects.filter(idprospecto=idprospecto).order_by('-inicio')
            if tipo == 'llamadas':
                sesiones = Prospectosesion.objects.filter(idprospecto=idprospecto, tipo=tipo_llamada).order_by('-inicio')
            if tipo == 'reuniones':
                sesiones = Prospectosesion.objects.filter(idprospecto=idprospecto, tipo=tipo_reunion).order_by('-inicio')
            
            serializer = ProspectosesionSerializer(sesiones, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'msg':'sucedio un problema'}, status=status.HTTP_400_BAD_REQUEST)
        # ---------------------------------------------------------------------------
        """if idprospecto != None:
            sesiones = Prospectosesion.objects.filter(idprospecto=idprospecto)
            serializer = ProspectosesionSerializer(sesiones, many=True)
            return Response(serializer.data, safe=False)
        else:
            return Response({'msg':'elemento no encontrado'}, status.HTTP_404_NOT_FOUND)"""

class Sesion_CRUD(APIView):
    """
    Clase manejadora de prospecto
    """
    permission_classes = [IsAuthenticated]

    def get(self, request,idprospecto, idsesion, format=None):
        ''' informacion sobre un prospecto '''
        if idprospecto == None:
            return Response({'msg':'idprospecto es requerido'}, status=status.HTTP_400_BAD_REQUEST)

        nombreusuario = request.user

        # si el usuario es supervisor regresamos la información
        if es_supervisor(nombreusuario):
            sesiones = Prospectosesion.objects.filter(idprospectosesion=idsesion)
            if not sesiones.exists():
                return Response({'msg': 'recurso no encontrado'}, status=status.HTTP_404_NOT_FOUND)
            sesiones = ProspectosesionSerializer(data=sesiones, many=True)
            return Response(sesiones.data, safe=False)

        # si es un empleado buscamos su informacion
        try:
            info = obtener_informacion_empleado(nombreusuario)
            idagente = info['idempleado']
        except Exception as e:
            return Response({'msg':'sucedio un problema'}, status=status.HTTP_400_BAD_REQUEST)

        # verificamos que tenga asignado al prospecto
        es_owner = Prospecto.objects.filter(idagente=idagente, idprospecto = idprospecto).exists()
        if not es_owner:
                return Response({'msg':'no tienes acceso a este recurso'}, status.HTTP_401_UNAUTHORIZED)
        
        try:
            sesiones = Prospectosesion.objects.filter(idprospectosesion=idsesion)
            sesiones = ProspectosesionSerializer(data=sesiones, many=True)
            return Response(sesiones.data)
        except:
            return Response({'msg':'recurso no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request,idprospecto,idsesion, format=None): 
        '''crear prospecto'''
        nombreusuario = request.user
        serializer = ProspectosesionSerializer(data=request.data)

        if es_supervisor(nombreusuario):

            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            try:
                serializer.save()
                return Response(serializer.data)
            except:
                return Response({'msg':'sucedio un problema. Sesion no creada'}, status=status.HTTP_400_BAD_REQUEST)  

        # si es un agente validamos que pueda acceder al usuario
        info = obtener_informacion_empleado(nombreusuario)
        idagente = info['idempleado']
        es_owner = Prospecto.objects.filter(idagente=idagente, idprospecto = idprospecto).exists()
        if not es_owner:
            return Response({'msg':'no tienes acceso a este recurso'}, status.HTTP_401_UNAUTHORIZED)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            serializer.save()
            return Response(serializer.data)
        except Exception as e:
            return Response({'msg':'sucedio un problema. Sesion no creada'}, status=status.HTTP_400_BAD_REQUEST)  

    def put(self, request,idprospecto,idsesion, format=None): 
        '''actualizar prospecto'''
        nombreusuario = request.user

        if es_supervisor(nombreusuario):

            try:
                old = Prospectosesion.objects.filter(idprospectosesion = idsesion).first()
                serializer = ProspectosesionSerializer(old, data= request.data)
                if not serializer.is_valid():
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                serializer.save()
                return Response(serializer.data)
            except Prospectosesion.DoesNotExist:
                return Response("", status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response("", status=status.HTTP_400_BAD_REQUEST)  

        # si es un agente validamos que pueda acceder al usuario
        info = obtener_informacion_empleado(nombreusuario)
        idagente = info['idempleado']
        es_owner = Prospecto.objects.filter(idagente=idagente, idprospecto = idprospecto).exists()
        if not es_owner:
            return Response({'msg':'no tienes acceso a este recurso'}, status.HTTP_401_UNAUTHORIZED)

        try:
            old = Prospectosesion.objects.filter(idprospectosesion = idsesion).first()
            serializer = ProspectosesionSerializer(old, data= request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data)
        except Prospectosesion.DoesNotExist:
            return Response("", status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("", status=status.HTTP_400_BAD_REQUEST)     

        