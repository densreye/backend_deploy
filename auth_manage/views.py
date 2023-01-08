from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password, check_password

from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.views import APIView

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from auth_manage.serializers import *
from auth_manage.models import Usuario, Cargo, Persona, Empleado

@csrf_exempt
@api_view(['POST'])
def login(request, *args, **kwargs):
    
    print('bien')
    # Obtenemos los valores post
    username = request.POST.get('username')
    password = request.POST.get('password')

    # revisamos si existe caso contrario enviamos unauthorized
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response("", status.HTTP_401_UNAUTHORIZED)

    # validamos contraseña
    pwd_valid = check_password(password, user.password)
    if not pwd_valid:
        return Response("contraseña invalida", status.HTTP_401_UNAUTHORIZED)
    
    # resivamos si el token existe sino lo creamos y retornamos el token
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token':token.key, 'idcargo':obtener_cargo(username)})


class UsuarioManage(APIView):
    
    """ crear usuarios """
    def post(self, request, format=None):

        serializer = UsuarioSerializer(data=request.data)

        # si los datos no son validos regresamas el error
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # recopilamos la informacion
        data = serializer.data
        originalpass = data.get('claveusuario')
        newpass = make_password(originalpass)
        username = data.get('nombreusuario')
        foto = data.get('fotousuario')

        # validamos si el nombre de usuario existe
        if User_username_exists(username) or Usuario_username_exists(username):
            return Response("el nombre de usuario ya existe", status=status.HTTP_400_BAD_REQUEST)

        # creamos el usuario en django.User
        try:
            user = User.objects.get_or_create(username=username, password=newpass)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # creamos el usuario en la tabla models.usuario
        try:
            usuario = Usuario(nombreusuario=username, claveusuario=newpass, fotousuario=foto)
            usuario.save()
        except:
            # si ocurre un error eliminamos el usuario en User
            u = User.objects.get(username = username)
            u.delete()
            return Response('sucedio un error, usuario no creado', status=status.HTTP_400_BAD_REQUEST)

        return Response(request.data, status=status.HTTP_201_CREATED)

    '''actualizar usuarios - en progreso'''
    def put(self, request, pk, format=None):
        '''en progreso'''
    
    '''eliminar usuarios - en progreso'''
    def delete(self, request, format=None):
        '''en progreso'''
        serializer = UsuarioSerializer(data=request.data)

        # si los datos no son validos regresamas el error
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

         # recopilamos la informacion
        data = serializer.data
        password = data.get('claveusuario')
        username = data.get('nombreusuario')
        foto = data.get('fotousuario')

        # validamos si el nombre de usuario existe
        if User_username_exists(username) and Usuario_username_exists(username):
            return Response("el nombre de usuario ya existe", status=status.HTTP_400_BAD_REQUEST)


        return Response(status=status.HTTP_204_NO_CONTENT)

class EmpleadoManage(APIView):
    
    """ crear usuario tipo empleado """
    def post(self, request, format=None):
        # validamos el cargo
        idcargo = request.data['idcargo']
        if idcargo is None or idcargo == "":
            return Response("idcargo es un campo necesario", status=status.HTTP_400_BAD_REQUEST)
        try:
            cargo = Cargo.objects.get(idcargo = idcargo)
        except Cargo.DoesNotExist():
            return Response("el cargo no existe", status=status.HTTP_400_BAD_REQUEST)
        
        # inicamos la creacion del usuario
        serializer = UsuarioSerializer(data=request.data)

        # si los datos no son validos regresamas el error
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # recopilamos la informacion
        data = serializer.data
        originalpass = data.get('claveusuario')
        newpass = make_password(originalpass)
        username = data.get('nombreusuario')
        foto = data.get('fotousuario')

        # validamos si el nombre de usuario existe
        if User_username_exists(username) or Usuario_username_exists(username):
            return Response("el nombre de usuario ya existe", status=status.HTTP_400_BAD_REQUEST)

        # creamos el usuario en django.User
        try:
            user = User.objects.get_or_create(username=username, password=newpass)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # creamos el usuario en la tabla models.usuario
        try:
            usuario = Usuario(nombreusuario=username, claveusuario=newpass, fotousuario=foto)
            usuario.save()
        except:
            # si ocurre un error eliminamos el usuario en User
            u = User.objects.get(username = username)
            u.delete()
            return Response('sucedio un error, usuario no creado', status=status.HTTP_400_BAD_REQUEST)

        # creamos la persona para el empleado
        usuario = Usuario.objects.get(nombreusuario=username)
        try:
            persona = Persona.objects.get_or_create(idusuario=usuario)[0]
        except Exception as e:
            u = User.objects.get(username = username)
            u.delete()
            u = Usuario.objects.get(username = username)
            return Response("Error empleado no creado", status=status.HTTP_400_BAD_REQUEST)

        # creamos al empleado
        try:
            empleado = Empleado.objects.get_or_create(idpersona=persona, idcargo=cargo)
        except Exception as e:
            u = User.objects.get(username = username)
            us = Usuario.objects.get(username = username)
            p = Persona.objects.get(idusuario=persona)
            p.delete()
            u.delete()
            us.delete()
            return Response("Error empleado no creado", status=status.HTTP_400_BAD_REQUEST)


        return Response(serializer.data, status=status.HTTP_201_CREATED)

    '''actualizar empleados - en progreso'''
    def put(self, request, pk, format=None):
        '''en progreso'''
    
    '''eliminar empleados - en progreso'''
    def delete(self, request, format=None):
        '''en progreso'''
        serializer = UsuarioSerializer(data=request.data)

        # si los datos no son validos regresamas el error
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

         # recopilamos la informacion
        data = serializer.data
        password = data.get('claveusuario')
        username = data.get('nombreusuario')
        foto = data.get('fotousuario')

        # validamos si el nombre de usuario existe
        if User_username_exists(username) and Usuario_username_exists(username):
            return Response("el nombre de usuario ya existe", status=status.HTTP_400_BAD_REQUEST)


        return Response(status=status.HTTP_204_NO_CONTENT)



'''recibe un token y devuelve un usuario [models.Usuario]'''
def obtener_usuario(nombreusuario):

    '''buscamos el usuario al que pertenece el token'''
    try:
        usuario = Usuario.objects.get(nombreusuario=nombreusuario)
    except User.DoesNotExist:
        return None
    return usuario

'''obtener cargo de un usuario'''
def obtener_cargo(nombreusuario):
    '''buscamos el usuario al que pertenece el token'''
    try:
        usuario = Usuario.objects.get(nombreusuario=nombreusuario)
    except User.DoesNotExist:
        return None

    '''buscamos la persona a la que pertenece'''
    try:
        persona = Persona.objects.get(idusuario = usuario)
        #persona = PersonaSerializer(persona)
        empleado = Empleado.objects.get(idpersona=persona.idpersona)
        '''empleado = EmpleadoSerializer(empleado, many= True).data'''
        cargo = empleado.idcargo
        return cargo.idcargo
    except Exception as e:
        return None

def User_username_exists(username):
    return User.objects.filter(username=username).exists()

def Usuario_username_exists(username):
    return Usuario.objects.filter(nombreusuario=username).exists()
