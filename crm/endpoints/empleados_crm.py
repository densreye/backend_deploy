from django.db.models import Count

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from crm.models import Usuario, Persona, Empleado
from crm.serializers import PersonaSerializer, UsuarioSerializer, EmpleadoSerializer
from crm.utilidades import es_supervisor, obtener_informacion_empleado

class Lista_Empleados(APIView):
    #permission_classes = [IsAuthenticated]
    
    

    def get(self, request, format=None):
        
        print('bien empleado')
        nombreusuario = request.user

        empleados = listar_empleados()
        print(empleados)
        if empleados == None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # si es supervisor retornamos la lista de empleados
        if es_supervisor(nombreusuario):
            return Response(empleados)
        
        # Si no es supervisor regresamos solo su informacion
        try:
            # FIXME arregla esto
            for e in empleados.values():
                if e['nombreusuario'] == str(nombreusuario):
                    res = list()
                    res.append(e)
                    return Response(res)
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)

def responder_todos():
    empleados = listar_empleados()
    if empleados == None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(empleados)

def responder_info():
    return Response(status=status.HTTP_404_NOT_FOUND)

def listar_empleados():
    try:
        cargos = [301,302,303]
        empleados = Empleado.objects.filter(idcargo__in = cargos)
        empleados_idpersona = empleados.values_list('idpersona', flat=True)
        serializer_empleados = EmpleadoSerializer(empleados, many= True)

        personas = Persona.objects.filter(idpersona__in = empleados_idpersona)
        personas_idusuario = personas.values_list('idusuario', flat=True)
        serializer_persona = PersonaSerializer(personas, many=True)

        usuarios = Usuario.objects.filter(idusuario__in = personas_idusuario)
        serializer_usuarios = UsuarioSerializer(usuarios,many= True)

        resultado = list()

        for empleado in serializer_empleados.data:
            idempleado = empleado["idempleado"]
            idpersona ,idusuario = None, None
            sub = dict()
            sub['idempleado'] = idempleado
            for persona in serializer_persona.data:
                if persona['idpersona'] == empleado['idpersona']:
                    idpersona = empleado['idpersona']
                    idusuario = persona['idusuario']
                    sub['idpersona'] = idpersona
                    sub['idusuario'] = idusuario
                    sub['nombre'] = persona['nombre']
                    sub['apellido'] = persona['apellido']
                    continue
            for usuario in serializer_usuarios.data:
                if usuario['idusuario'] == idusuario:
                    sub['nombreusuario'] = usuario['nombreusuario']
                    continue
            resultado.append(sub)

        return resultado
    except Exception as e:
        return None