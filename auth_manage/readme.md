# ...

Se utilizara el framework **Django Rest Framework**

# Uso Frontend
Usaremos una autentificacion basada en tokens, considere las siguientes indicaciones del lado del cliente https://www.django-rest-framework.org/topics/api-clients/#token-authentication_1

Recuerde usar la cabecera ```Authorization: Token [token generado]``` cuando genere su solicitud


# Backend
## Inicio de Sesion

en el archivo de rutas
```python
from auth_manage.views import login
...

[
    ...
    path('[rutalogin]/', login),
]
```

## Registrar empleado

Usar la clase ```EmpleadoManage```, pasando los parametros de un usuario y el parameto ```idcargo``` en la solicitud

```python
from auth_manage.views import EmpleadoManage
...

[
    ...
    path('[rutalogin]/', EmpleadoManage.as_view()),
]
```





## Proteger rutas
Basandonos en el esquema de classes APIview, proteger una clase se reduce a incluir el permiso en la clase 

```python
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class ExampleView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)
```

## Obtener información del Token

retorna un objeto de clase ````Usuario```` especificado en ```models.py```

```python
from auth_manage.views import get_usuario_token

usuario = obtener_usuario_token('[token]')

```

# Cosas que faltan

- autenticar todas las rutas que sean necesarias
- Crear empleado podria generar problemas
- metodos de actualizacion y eliminacion para empleados y usuarios