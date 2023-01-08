from django.db.models import Count

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from crm.models import Prospecto, Prospectosesion, Cotizacion, Plan
from crm.serializers import ProspectoSerializer, ProspectosesionSerializer, CotizacionSerializer, PlanSerializer

from crm.utilidades import es_supervisor, obtener_informacion_empleado
from crm.endpoints.empleados_crm import listar_empleados

from datetime import datetime

formato_fecha_hora = '%Y-%m-%dT%H:%M:%S%z'


class SumarioAgentes(APIView):
    """ Sumario por Agente """
    permission_classes = [IsAuthenticated]

    def get(self, request, idagente, inicio, fin, format=None):
        nombreusuario = request.user
        if not es_supervisor(nombreusuario):
            try:
                info = obtener_informacion_empleado(nombreusuario)
                idagente = info['idempleado']
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(sumario_por_agente(idagente, inicio, fin))


class SumarioAgentesTodos(APIView):
    """ Sumario todos los agentes, Solo Supervisores """
    permission_classes = [IsAuthenticated]

    def get(self, request, inicio, fin, format=None):
        nombreusuario = request.user

        if not es_supervisor(nombreusuario):
            return Response(status=status.HTTP_404_NOT_FOUND)
        return responder_sumario_todos(inicio, fin)


class SumarioPlanesTodos(APIView):
    """ Sumario todos los agentes, Solo Supervisores """
    permission_classes = [IsAuthenticated]

    def get(self, request, inicio, fin, format=None):
        nombreusuario = request.user
        return reponder_sumario_planes_todos(inicio, fin)


# funciones individuales -----------------------------------------------------------------------------
def sumario_por_agente(idagente, inicio, fin):
    return {
        'idagente': idagente,
        'inicio': inicio,
        'fin': fin,
        'prospectos': sumario_prospectos(idagente, inicio, fin),
        'llamadas': sumario_sesiones(idagente, inicio, fin, 1),
        'reuniones': sumario_sesiones(idagente, inicio, fin, 2),
        'cotizaciones': sumario_cotizaciones(idagente, inicio, fin)
    }


def sumario_prospectos(idagente, inicio, fin):
    '''sumario de prospectos'''
    try:
        creados = Prospecto.objects.filter(
            idagente=idagente, creado__range=[inicio, fin])
        serializer = ProspectoSerializer(creados, many=True)
        creados = len(serializer.data)

        sumario = {
            'creados': creados,
        }
        return sumario
    except Exception as e:
        print(e)
        return {}


def sumario_sesiones(idagente, inicio, fin, tipo=1):
    '''
    sumarios de reuniones
    tipos: llamada = 1  reunion = 2
    '''
    try:
        llamadas = Prospectosesion.objects.filter(
            idprospecto__idagente=idagente, inicio__range=[inicio, fin], tipo=tipo)
        serializer = ProspectosesionSerializer(llamadas, many=True)
        # print(serializer.data)
        total = 0
        agendadas = 0
        realizadas = 0
        perdidas = 0

        tiempo_realizadas = 0

        for llamada in serializer.data:
            total += 1
            est = llamada['estado']
            if est == 0:
                agendadas += 1
            elif est == 1:
                realizadas += 1
                # print(llamada['idprospectosesion'],llamada)
                if llamada['inicio'] == None or llamada['fin'] == None:
                    # si falta informacion ponemos el tiempo minimo que son 15 min
                    tiempo_realizadas += 15 * 60
                else:
                    inicio = datetime.strptime(
                        llamada['inicio'], formato_fecha_hora)
                    fin = datetime.strptime(llamada['fin'], formato_fecha_hora)
                    diferencia = fin - inicio
                    tiempo_realizadas += diferencia.total_seconds()
            else:
                # est == 2
                perdidas += 0

        '''
        0:'Agendada',
        1:'Realizada',
        2:'Perdida',
        '''
        sumario = {
            'total': total,
            'agendadas': agendadas,
            'realizadas': realizadas,
            'perdidas': perdidas,
            'tiempo_realizadas': tiempo_realizadas,
        }
        return sumario
    except Exception as e:
        print(e)
    return {}


def sumario_cotizaciones(idagente, inicio, fin):
    '''sumario de cotizaciones'''
    try:
        creadas = Cotizacion.objects.filter(
            idprospecto__idagente=idagente, creado__range=[inicio, fin])
        serializer = CotizacionSerializer(creadas, many=True)
        creadas = len(serializer.data)

        cotizaciones = Cotizacion.objects.filter(
            idprospecto__idagente=idagente, modificado__range=[inicio, fin])
        serializer = CotizacionSerializer(cotizaciones, many=True)

        total, abiertas, vendidas, cerradas = 0, 0, 0, 0
        '''{'abierta': 0, 'vendida': 1, 'cerrada': 2}'''
        for cot in serializer.data:
            est = cot['estado']
            total += 1

            if est == 0:
                abiertas += 1
            elif est == 1:
                vendidas += 1
            else:
                # cerrada == 2
                cerradas += 1

        sumario = {
            'creadas': creadas,
            'total': total,
            'abiertas': abiertas,
            'vendidas': vendidas,
            'cerradas': cerradas,
        }

        return sumario
    except Exception as e:
        print(e)
        return {}

# funciones todos ----------------------------------------------


def responder_sumario_todos(inicio, fin):
    try:
        sumario = list()
        for e in listar_empleados():
            idagente = e['idempleado']
            sumario.append(sumario_por_agente(idagente, inicio, fin))

        return Response(sumario)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_404_NOT_FOUND)

# funciones planes -----------------------------------------------


def reponder_sumario_planes_todos(inicio, fin):
    '''lista de planes con su informacion y detalles de las veces que han sido cotizados'''
    try:
        planes = Plan.objects.all()
        planes_serializer = PlanSerializer(planes, many=True)

        planes_cotizados = []

        for plan in planes_serializer.data:
            plan['sumario'] = sumario_cotizaciones_por_plan(plan, inicio, fin)
            """ sub = {
                'plan': plan,
                'cotizaciones': sumario_cotizaciones_por_plan(plan, inicio, fin)
            } """
            planes_cotizados.append(plan)

        sumario = {
            'planes_cotizados': planes_cotizados,
            'descriptiva': sumario_cotizaciones_por_plan_descriptivo(planes_cotizados)
        }

        return Response(sumario)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_404_NOT_FOUND)


def sumario_cotizaciones_por_plan(plan, inicio, fin):
    try:
        cotizacion_creadas = Cotizacion.objects.filter(
            idplan=plan['idplan'], creado__range=[inicio, fin])
        cotizacion_creadas = CotizacionSerializer(
            cotizacion_creadas, many=True)

        creadas = len(cotizacion_creadas.data)

        cotizacion = Cotizacion.objects.filter(
            idplan=plan['idplan'], modificado__range=[inicio, fin])
        serializer = CotizacionSerializer(cotizacion, many=True)

        total, abiertas, vendidas, cerradas = 0, 0, 0, 0
        '''{'abierta': 0, 'vendida': 1, 'cerrada': 2}'''
        for cot in serializer.data:
            est = cot['estado']
            total += 1

            if est == 0:
                abiertas += 1
            elif est == 1:
                vendidas += 1
            else:
                # cerrada == 2
                cerradas += 1

        sumario = {
            'creadas': creadas,
            'total': total,
            'abiertas': abiertas,
            'vendidas': vendidas,
            'cerradas': cerradas,
        }
        return sumario
    except Exception as e:
        return []

def sumario_cotizaciones_por_plan_descriptivo(lista_cotizaciones_por_plan, top = 5):
    try:
        top_creadas = []
        top_abiertas = []
        top_vendidas = []
        top_cerradas = []

        menos_creadas = []
        menos_abiertas = []
        menos_vendidas = []
        menos_cerradas = []

        top_creada = None
        top_abierta = None
        top_vendida = None
        top_cerrada = None

        menos_creada = None
        menos_abierta = None
        menos_vendida = None
        menos_cerrada = None


        count = min(top, len(lista_cotizaciones_por_plan))
        while (count > 0) :
            count -= 1

            for cot in lista_cotizaciones_por_plan:
                # mas cerradas 
                if (top_cerrada == None) and ((cot not in top_cerradas)):
                    top_cerrada = cot
                elif (cot not in top_cerradas) and (cot['sumario']['cerradas'] >= top_cerrada['sumario']['cerradas']):
                    top_cerrada = cot
                # menos cerradas 
                if (menos_cerrada == None) and ((cot not in menos_cerradas)):
                    menos_cerrada = cot
                elif (cot not in menos_cerradas) and (cot['sumario']['cerradas'] <= menos_cerrada['sumario']['cerradas']):
                    menos_cerrada = cot

                # mas abiertas 
                if (top_abierta == None) and ((cot not in top_abiertas)):
                    top_abierta = cot
                elif (cot not in top_abiertas) and (cot['sumario']['abiertas'] >= top_abierta['sumario']['abiertas']):
                    top_abierta = cot
                # menos abiertas 
                if (menos_abierta == None) and ((cot not in menos_abiertas)):
                    menos_abierta = cot
                elif (cot not in menos_abiertas) and (cot['sumario']['abiertas'] <= menos_abierta['sumario']['abiertas']):
                    menos_abierta = cot
                # mas vendidas 
                if (top_vendida == None) and ((cot not in top_vendidas)):
                    top_vendida = cot
                elif (cot not in top_vendidas) and (cot['sumario']['vendidas'] >= top_vendida['sumario']['vendidas']):
                    top_vendida = cot
                # menos vendidas 
                if (menos_vendida == None) and ((cot not in menos_vendidas)):
                    menos_vendida = cot
                elif (cot not in menos_vendidas) and (cot['sumario']['vendidas'] <= menos_vendida['sumario']['vendidas']):
                    menos_vendida = cot
                
                # mas creadas 
                if (top_creada == None) and ((cot not in top_creadas)):
                    top_creada = cot
                elif (cot not in top_creadas) and (cot['sumario']['creadas'] >= top_creada['sumario']['creadas']):
                    top_creada = cot
                # menos creadas 
                if (menos_creada == None) and ((cot not in menos_creadas)):
                    menos_creada = cot
                elif (cot not in menos_creadas) and (cot['sumario']['creadas'] <= menos_creada['sumario']['creadas']):
                    menos_creada = cot

            top_creadas.append(top_creada)
            top_creada = None
            menos_creadas.append(menos_creada)
            menos_creada = None

            top_vendidas.append(top_vendida)
            top_vendida = None
            menos_vendidas.append(menos_vendida)
            menos_vendida = None

            top_abiertas.append(top_abierta)
            top_abierta = None
            menos_abiertas.append(menos_abierta)
            menos_abierta = None

            top_cerradas.append(top_cerrada)
            top_cerrada = None
            menos_cerradas.append(menos_cerrada)
            menos_cerrada = None

        return {
            'top_creadas': top_creadas,
            'menos_creadas': menos_creadas,
            'top_abiertas': top_abiertas,
            'menos_abiertas': menos_abiertas,
            'top_cerradas': top_cerradas,
            'menos_cerradas': menos_cerradas,
            'top_vendidas': top_vendidas,
            'menos_vendidas': menos_vendidas,
        }
    except Exception as e:
        return {}
    
