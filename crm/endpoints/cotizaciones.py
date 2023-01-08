from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

from crm.models import Prospecto, Cotizacion
from crm.serializers import ProspectoSerializer, CotizacionSerializer

from auth_manage.views import obtener_cargo
from crm.decoradores import supervisor
from crm.utilidades import *

from auth_manage import files

class Lista_Cotizaciones_Por_Prospecto(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, idprospecto, format=None):

        if idprospecto == None:
            return Response({'msg':'idprospecto es requerido'}, status=status.HTTP_400_BAD_REQUEST)

        nombreusuario = request.user

        # si el usuario es supervisor regresamos la información
        if es_supervisor(nombreusuario):
            return lista_de_cotizaciones(idprospecto)

        # si es un empleado buscamos su informacion
        idagente = obtener_idagente(nombreusuario)
        if idagente == None:
            return Response({'msg':'sucedio un problema'}, status=status.HTTP_400_BAD_REQUEST)

        # verificamos que tenga asignado al prospecto
        if validar_prospecto_agente(idagente, idprospecto):
            return lista_de_cotizaciones(idprospecto)

        '''
        try:
            prospectos = Prospecto.objects.filter(idagente=idagente, idprospecto=idprospecto)
            serializer = ProspectoSerializer(prospectos, many=True)
            return lista_de_cotizaciones(idprospecto)
        except Prospecto.DoesNotExist:
            return Response({'msg':'recurso no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        '''

class Cotizacion_CRUD(APIView):
    # Clase manejadora de prospecto

    permission_classes = [IsAuthenticated]

    def get(self, request,idcotizacion, format=None):
        if idcotizacion == None:
            return Response({'msg':'idcotizacion es requerido'}, status=status.HTTP_400_BAD_REQUEST)
        
        nombreusuario = request.user

        cotizacion = obtener_cotizacion(idcotizacion)
        # si el usuario es supervisor regresamos la información
        if es_supervisor(nombreusuario):
            data = CotizacionSerializer(cotizacion)
            return Response(data.data)

        
        # si es un empleado buscamos su informacion
        idagente = obtener_idagente(nombreusuario)
        if idagente == None:
            return Response({'msg':'sucedio un problema'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            if validar_prospecto_agente(idagente, idprospecto):
                data = CotizacionSerializer(cotizacion)
                return Response(data.data)
            else:
                return Response({"msg":"no tiene permisos"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"msg": "ha ocurrido un error"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request,idcotizacion, format=None):
        if idcotizacion == None:
            return Response({'msg':'idcotizacion es requerido'}, status=status.HTTP_400_BAD_REQUEST)
        nombreusuario = request.user
        request.POST._mutable = True
        request.data['modificado'] = obtener_fecha_actual()
        request.data['creado'] = obtener_fecha_actual()
        request.POST._mutable = False
       
       # revisamos si la entrada es valida
        serializer = CotizacionSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # si es supervisor regresamos la informacion
        if es_supervisor(nombreusuario):
            try:
                serializer.save()
                return Response(serializer.data)
            except:
                return Response({'msg':'sucedio un problema'}, status=status.HTTP_400_BAD_REQUEST)
        
        # si no es supervisor validamos si tiene permisos
        try:
            idprospecto = serializer.validated_data.get('idprospecto').idprospecto
            idagente = obtener_idagente(nombreusuario)
        except Exception as e:
            return Response({'msg':'sucedio un problema'}, status=status.HTTP_400_BAD_REQUEST)

        if idagente == None:
            return Response({'msg':'sucedio un problema'}, status=status.HTTP_400_BAD_REQUEST)
        
        puede_editar = validar_prospecto_agente(idagente, idprospecto)
        try:
            if puede_editar:
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({"msg":"no tiene permisos"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            print(e)
            return Response({"msg": "ha ocurrido un error"}, status=status.HTTP_400_BAD_REQUEST)

    """ def put(self, request,idcotizacion, format=None):
        nombreusuario = request.user
        if idcotizacion == None:
            return Response({'msg':'idcotizacion es requerido'}, status=status.HTTP_400_BAD_REQUEST)
        
        # revisamos si la entrada es valida

        try:
            old = Cotizacion.objects.get(idcotizacion= idcotizacion)

            request.PUT._mutable = True
            request.data['modificado'] = obtener_fecha_actual()
            request.data['creado'] = old.creado
            request.PUT._mutable = False

            serializer = CotizacionSerializer(old,data= request.data)
        except Exception as e:
            return Response({'msg':e}, status=status.HTTP_400_BAD_REQUEST)



        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # si es supervisor regresamos la informacion
        if es_supervisor(nombreusuario):
            try:
                serializer.save()
                return Response(serializer.data)
            except:
                return Response({'msg':'sucedio un problema'}, status=status.HTTP_400_BAD_REQUEST)
        
        # si no es supervisor validamos si tiene permisos
        try:
            idprospecto = serializer.validated_data.get('idprospecto').idprospecto
            idagente = obtener_idagente(nombreusuario)
        except Exception as e:
            return Response({'msg':'sucedio un problema'}, status=status.HTTP_400_BAD_REQUEST)

        if idagente == None:
            return Response({'msg':'sucedio un problema'}, status=status.HTTP_400_BAD_REQUEST)
        
        puede_editar = validar_prospecto_agente(idagente, idprospecto)
        try:
            if puede_editar:
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({"msg":"no tiene permisos"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"msg": "ha ocurrido un error"}, status=status.HTTP_400_BAD_REQUEST) """

"""
class Cotizacion_CRUD(APIView):
    # Clase manejadora de prospecto

    permission_classes = [IsAuthenticated]

    def get(self, request,idcotizacion, format=None):
        ''' informacion sobre un prospecto '''
        if idcotizacion == None:
            return Response({'msg':'idcotizacion es requerido'}, status=status.HTTP_400_BAD_REQUEST)

        nombreusuario = request.user
        
        # buscamos la cotizacion
        try:
            cotizacion = Cotizacion.objects.get(idcotizacion=idcotizacion)
        except Cotizacion.DoesNotExist:
            return Response({"msg": "el recurso no existe"}, status=status.HTTP_404_NOT_FOUND)


        # si el usuario es supervisor regresamos la información
        if es_supervisor(nombreusuario):
            return Response(cotizacion)

        # si es un empleado buscamos su informacion
        try:
            info = obtener_informacion_empleado(nombreusuario)
            idagente = info['idempleado']
        except Exception as e:
            return Response({'msg':e}, status=status.HTTP_400_BAD_REQUEST)

        # verificamos que tenga asignado al prospecto
        try:
            prospectos = Prospecto.objects.filter(idagente=idagente, idcotizacion=idcotizacion)
            serializer = ProspectoSerializer(prospectos, many=True)
        except Prospecto.DoesNotExist:
            return Response({'msg':'No tienes permisos para acceder a este prospecto'}, status=status.HTTP_401_UNAUTHORIZED)
"""

class Cotizacion_cambiar_estado(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request,idprospecto, format=None):
        nombreusuario = request.user

        idcotizacion = request.data['idcotizacion']
        estado = request.data['estado']
        motivocierre = request.data['motivocierre']

        if not idcotizacion or not estado:
            return Response({'msg':'idcotizacion y estado son campos requeridos, motivo cierre es opcional'}, status=status.HTTP_400_BAD_REQUEST)
        
        if es_supervisor(nombreusuario):
            return cambiar_estado_cotizacion(idcotizacion= idcotizacion,estado=estado , motivocierre=motivocierre)
        
        idagente = obtener_idagente(nombreusuario)
        if validar_prospecto_agente(idagente=idagente,idprospecto=idprospecto):
            return cambiar_estado_cotizacion(idcotizacion= idcotizacion,estado=estado , motivocierre=motivocierre)
        return Response({"msg":"no tiene permisos"}, status=status.HTTP_401_UNAUTHORIZED)
 
        

def lista_de_cotizaciones(idprospecto):
    try:
        cotizacion = Cotizacion.objects.filter(idprospecto=idprospecto).order_by('-creado')
        serializer = CotizacionSerializer(cotizacion, many=True)
        for c in serializer.data:
            c['filepath'] = files.obtener_hash_file(c['filepath'])

        return Response(serializer.data)
    except Cotizacion.DoesNotExist:
        return Response({"msg": "Recurso no encontrado"}, status=status.HTTP_404_NOT_FOUND)

def obtener_cotizacion(idcotizacion):
    try:
        cotizacion = Cotizacion.objects.get(idcotizacion = idcotizacion)
        return cotizacion
    except Cotizacion.DoesNotExist:
        return null

def cambiar_estado_cotizacion(idcotizacion,estado, motivocierre=None):
    try:
        old = Cotizacion.objects.get(idcotizacion=idcotizacion)
    except Cotizacion.DoesNotExist:
        return Response({"msg": "Recurso no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    data = {'estado': estado, 'motivocierre':motivocierre, 'modificado':obtener_fecha_actual()}
    serializer = CotizacionSerializer(old, data=data,partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)