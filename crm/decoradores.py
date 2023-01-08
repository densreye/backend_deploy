from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from crm.utilidades import es_supervisor

import inspect

metodos = ['get', 'post', 'put', 'delete']

cargos_supervisor = [301]
  

def supervisor(methods=[], err_message="Autentificacion necesaria."):
    def decorator(view_function):
        def decorated_function(self, *args, **kwargs):
            # validate token existence
            request= args[0]

            if request is None:
                return Response({"msg": err_message}, status=status.HTTP_401_UNAUTHORIZED)

            if not 'Authorization' in request.headers:
                return Response({"msg": err_message}, status=status.HTTP_401_UNAUTHORIZED)

            # validamos que sea un supervisor
            if es_supervisor(request.user):
                return view_function(request, *args, **kwargs)
            else:
                return Response({"msg": "no tienes permisos suficientes."}, status=status.HTTP_401_UNAUTHORIZED)

        return decorated_function
    return decorator