import re

from rest_framework.response import Response
from rest_framework import status

REGEX_USER = '^[a-zA-Z][a-zA-Z0-9]{8,16}$'


def validar_nombreusuario(nombreusuario):
	'''
	Validar:
	   - que empiece con una letra
	   - solo tenga letras y numeros
	   - de 8 a 16 caracteres
   '''
	x = re.search(REGEX_USER, nombreusuario)

	if x:
		return nombreusuario
	else:
		return Response({'msg':'Nombre de usuario no cumple con los requisitos'});
