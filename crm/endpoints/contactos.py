from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

from crm.models import Prospecto, Contactoprospecto
from crm.serializers import *

from auth_manage.views import obtener_cargo
from crm.decoradores import supervisor
from crm.utilidades import es_supervisor, obtener_informacion_empleado

tipocontactos_contactos = {"email":0, "telefono":1}

class crear_contactoprospecto(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request,idprospecto, format=None):
        nombreusuario = request.user
        # si el usuario es supervisor regresamos la información
        if es_supervisor(nombreusuario):
            return crear_contacto(data=request.data)

        idagente = obtener_idagente(nombreusuario)
        if idagente == None:
            return Response({'msg':'sucedio un problema'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            if validar_prospecto_agente(idagente, idprospecto):
                return crear_contacto(data=request.data)
            else:
                return Response({"msg":"no tiene permisos"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'msg':'sucedio un problema'}, status=status.HTTP_400_BAD_REQUEST) 
        

class lista_contactos(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, idprospecto, tipocontacto, format=None):

        nombreusuario = request.user
        # validamos si idprospecto
        if idprospecto is None:
            return Response({'msg':'idprospecto no valido'}, status.HTTP_404_NOT_FOUND)

        tipo = obtener_tipocontacto_contacto(tipocontacto)
        if tipo == None:
            return Response({'msg':f'tipocontacto [{tipocontacto}] no valido. valido : {tipocontactos_contactos}'}, status.HTTP_404_NOT_FOUND)
        
        if es_supervisor(nombreusuario):
            return responder_lista_contactos(idprospecto=idprospecto,tipo=tipo)

        idagente = obtener_idagente(nombreusuario)
        if idagente == None:
            return Response({'msg':'sucedio un problema'}, status=status.HTTP_400_BAD_REQUEST)

        if validar_prospecto_agente(idagente=idagente, idprospecto=idprospecto):
            return responder_lista_contactos(idprospecto=idprospecto,tipo=tipo)

def responder_lista_contactos(idprospecto,tipo):
    try:
        contactos = Contactoprospecto.objects.filter(idprospecto=idprospecto, tipo=tipo)
        serializer = ContactoprospectoSerializer(contactos,many=True)
        return Response(serializer.data)
    except Contactoprospecto.DoesNotExist:
        return Response({'msg':'elemento no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'msg':'sucedio un problema'}, status=status.HTTP_400_BAD_REQUEST)

def crear_contacto(data):
    contacto = ContactoprospectoSerializer(data=data)

    if not contacto.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    try:
        contacto.save()
        return Response(contacto.data)
    except Exception as e:
        return Response({"msg": "ha ocurrido un error"}, status=status.HTTP_400_BAD_REQUEST)

def obtener_tipocontacto_contacto(tipocontacto):
    return tipocontactos_contactos.get(tipocontacto)