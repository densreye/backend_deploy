from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

from crm.models import Prospecto, Plan
from crm.serializers import PlanSerializer

from auth_manage.views import obtener_cargo
from crm.decoradores import supervisor
from crm.utilidades import es_supervisor, obtener_informacion_empleado

class Lista_Planes(APIView):
    """
    Clase manejadora de Planes
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        ''' * -> permite obtener todos los planes '''
        try:
            planes = Plan.objects.all()
            serializer = PlanSerializer(planes, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'msg':f'{e}'}, status=status.HTTP_400_BAD_REQUEST)