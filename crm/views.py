from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.parsers import JSONParser

from crm.models import *
from crm.serializers import *


# Usuarios ----------------------------------------------
"""def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            message.success(request, f'Usuario {username}')
    else:
        form = UserCreationForm()
    context = {'form':form}
    return render(request, "template_name", context)
"""
#@api_view(['POST'])
def login (request):
    if request.method == 'POST':
        print(request.body)
        '''username= request.POST["user"]
        password = request.POST["pass"]'''
        #print(JSONParser().parse(request))
        return render(request, 'pruebas.html', {request.body})
    return Response({})

def index(request):
    data = dict()
    data.update({'title': 'HomePage CRM'})
    return render(request, "pruebas.html", data)


# API 
@api_view(['GET'])
def getData(request):
    #fun()
    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data)


        