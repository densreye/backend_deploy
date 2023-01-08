from rest_framework.parsers import JSONParser
from auth_manage.views import obtener_cargo, obtener_usuario
from crm.models import *
from crm.serializers import UsuarioSerializer, PersonaSerializer, EmpleadoSerializer, ProspectoSerializer

from datetime import datetime
import json

cargos_supervisor = [301]

def es_cargo_supervisor(cargo):
    return cargo in cargos_supervisor

def es_supervisor(nombreusuario):
    try:
        cargo = obtener_cargo(nombreusuario)
    except:
        return False
    return es_cargo_supervisor(cargo)

def obtener_informacion_empleado(nombreusuario):
    try:
        usuario = Usuario.objects.get(nombreusuario=nombreusuario)
        
        persona = Persona.objects.get(idusuario=usuario.idusuario)
        
        empleado = Empleado.objects.get(idpersona = persona.idpersona)
        
        data={
            'nombreusuario': usuario.idusuario,
            'fotousuario': usuario.fotousuario,

            'idpersona': persona.idpersona,
            'nombre': persona.nombre,
            'apellido': persona.apellido,
            'tipodeidentificacion': persona.tipodeidentificacion,
            'numeroidentificacion': persona.numeroidentificacion,
            'fechanacimiento': persona.fechanacimiento,
            'edad': persona.edad,
            'sexo': persona.sexo,
            'estadocivil': persona.estadocivil,
            'tipopersona': persona.tipopersona,
            'idempleado': empleado.idempleado,
            'idcargo': empleado.idcargo.idcargo,
            'descripcioncargo':empleado.idcargo.descripcion,
            #'fechaingresonoboa': Empleado.fechaingresonoboa,
        }

        return data
    except Exception as e:
        print(e)
        return None

def obtener_idagente(nombreusuario):
    try:
        empleado = obtener_informacion_empleado(nombreusuario)
        idagente = empleado['idempleado']
        return idagente
    except Exception as e:
        print(e)
        return None

def validar_prospecto_agente(idagente, idprospecto):
    try:
        prospectos = Prospecto.objects.filter(idagente=idagente, idprospecto=idprospecto)
        serializer = ProspectoSerializer(prospectos, many=True)
        return True
    except Prospecto.DoesNotExist:
        return False

def obtener_fecha_actual():
    return datetime.now()

def json_to_csv(json_string):
    csv = ''
    try:
        file_data = json.loads(json_string)
        for key in file_data[0].keys():
            csv += f'{key};'
        csv = csv[:-1] + "\n"
        
        for obj in file_data:
            for key in obj.keys():
                csv += f'{obj[key] or None};'
            csv = csv[:-1] + "\n"
        csv = csv[:-1]
        return csv
    except:
        return csv