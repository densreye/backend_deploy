
from rest_framework.response import Response
from django.db import transaction,connection
from rest_framework.decorators import api_view
from crm.serializers import Formulario_ContactenosSerializer, PlanSerializer, UsuarioSerializer, OfertasSerializer
from crm.models import Plan, Usuario, Ofertas
#modulo de envio de correo electronico
from ..correo.send_email import enviar_correo


#historia de usuario: NC-0000-0001 (Necesito enviar mi informacion para ser contactado por un asesor)
@api_view(['POST'])
def formulario_contactenos(request):
    
    print('request: ',request.data)
    
    if request.method == 'POST':
        formulario_serializer=Formulario_ContactenosSerializer(data=request.data)
        if formulario_serializer.is_valid():
            formulario_serializer.save()
            return Response({'resp':'exito'})
        else:
            print('formulario no valido')
            return Response({'resp':'error'})
        

@api_view(['POST'])
def formulario_cotizar(request):
    
    print('request: ',request.data)
    
    if request.method == 'POST':
        formulario_serializer=Formulario_ContactenosSerializer(data=request.data)
        if formulario_serializer.is_valid():
            formulario_serializer.save()
            
            
            #plan_model=Plan.objects.filter(genero='Hombre',edad_minima__lte=50,edad_maxima__gte=30).all()
            plan_model=Plan.objects.filter(genero=request.data['genero']).all()
            
            plan_serializer=PlanSerializer(plan_model, many=True)
            
            
            return Response({'resp':'exito','data':plan_serializer.data})
            
            #return Response({'resp':'exito'})
        else:
            print('formulario no valido')
            return Response({'resp':'error'})


@api_view(['POST'])
def login(request):
    
    if request.method == 'POST':
        print('login')
        credenciales=request.data
        
        #plan_model=Plan.objects.filter(genero='Hombre',edad_minima__lte=50,edad_maxima__gte=30).all()
        usuario_model=Usuario.objects.filter(nombreusuario=credenciales['user'],claveusuario=credenciales['password']).all()        
        usuario_serializer=UsuarioSerializer(usuario_model, many=True)
        
        return Response({'resp':'exito','data': usuario_serializer.data})
    
    
@api_view(['POST'])
def cambiar_password(request):
    
    if request.method == 'POST':
        print('password cambiar')
        
        print(request.data)
        
        user = request.data['user']
        password=request.data['password']
        
        try:
            cursor = connection.cursor()
            q = 'UPDATE usuario SET claveUsuario = %s WHERE nombreUsuario =%s'
            cursor.execute(q, (password,user))
            return Response({"resp": "exito"})
        except Exception as e:
            print('error: ',e)
            return Response({"resp": "error"})
        

#--------- historias de usuario num 3 --------------------------------------------------------
@api_view(['GET'])
def obtener_oferta(request):
    
    if request.method == 'GET':
        ofertas=Ofertas.objects.all()
        ofertas_serializer=OfertasSerializer(ofertas, many=True)
        
        #ofertas_serializer.data['clave']='123'
        for elemento in ofertas_serializer.data:
            id_plan=Plan.objects.filter(pk=elemento['idplan'])
            plan_serializer=PlanSerializer(id_plan, many=True)
            lista_plan=plan_serializer.data
            elemento['nombrePlan']=lista_plan[0]['nombreplan']
        return Response({'resp':'exito','data': ofertas_serializer.data})
    




#------------ funcionalidad de correo----------------
@api_view(['POST'])
def actualizar_password(request):
    print('bien')
    
    
    if request.method == 'POST':
    
        credenciales=request.data 
        usuario_model=Usuario.objects.filter(nombreusuario=credenciales['user']).all()        
        usuario_serializer=UsuarioSerializer(usuario_model, many=True)
        
        enviar_correo(usuario_serializer.data[0]['nombreusuario'],usuario_serializer.data[0]['claveusuario'],usuario_serializer.data[0]['correo'])
        return Response({'resp':'exito','data': usuario_serializer.data})

