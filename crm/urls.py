
from django.urls import path, include
from . import views

from django.contrib import admin
from auth_manage.views import login, UsuarioManage, EmpleadoManage
# my routes
#import './routes/prospectos' from prospecto

#my endpoints
from crm.endpoints import prospectos, sesiones, planes, cotizaciones, contactos, sumario, empleados_crm, historias_usuario
app_name = "crm"

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', views.index, name = "home"),
    path('', views.index),

    path('api/', views.getData ),
    path('api/login/', login),
    path('api/crearusuario/', UsuarioManage.as_view()),
    path('api/crearempleado/', EmpleadoManage.as_view()),

    # Rutas Finales ----------------------------------------------------------------------------

    # iniciar sesion y obtener token
    path('api/login/', login),

    #devuelve todos los prospectos si eres supervisor, y los asignados si eres agente de ventas
    path('api/prospectos/', prospectos.Lista_Prospectos.as_view()),

    # exportar prospectos
    path('api/prospectos/exportar/<str:tipo>/', prospectos.prospectosExportar.as_view()),

    # importar prospectos
    path('api/prospectos/importar/', prospectos.ProspectosImportar().as_view()),

    #lista de prospectos por agente - supervisor
    path('api/prospectos/<int:idagente>/', prospectos.Lista_Prospectos_Agente.as_view()),

    # CRUD de prospectos
    path('api/prospecto/<int:idprospecto>/', prospectos.Prospecto_CRUD.as_view()),

    # lista de sesiones por prospecto
    path('api/sesiones/<int:idprospecto>/<str:tipo>/', sesiones.Lista_Sesiones_Prospecto.as_view()), 

    # CRUD de sesiones
    path('api/sesion/<int:idprospecto>/<int:idsesion>/', sesiones.Sesion_CRUD.as_view()),

    # Lista de Planes
    path('api/planes/', planes.Lista_Planes.as_view()),

    # lista cotizaciones por prsopecto
    path('api/cotizaciones/<int:idprospecto>/', cotizaciones.Lista_Cotizaciones_Por_Prospecto.as_view()),

    # CRUD de Cotizaciones
    path('api/cotizacion/<int:idcotizacion>/', cotizaciones.Cotizacion_CRUD.as_view()),

    # CRUD de Cotizaciones
    path('api/cotizacion/cambiar_estado/<int:idprospecto>/', cotizaciones.Cotizacion_cambiar_estado.as_view()),

    # Contacto crear
    path('api/contacto/crear/<int:idprospecto>/', contactos.crear_contactoprospecto.as_view()),

    # Contacto lista por prospecto
    path('api/contacto/<str:tipocontacto>/<int:idprospecto>/', contactos.lista_contactos.as_view()),

    # Lista de empleados
    path('api/empleados/', empleados_crm.Lista_Empleados.as_view()),

    # Sumario todos, SOLO SUPERVISOR
    path('api/supervisor/sumario_planes/<str:inicio>/<str:fin>/', sumario.SumarioPlanesTodos.as_view()),

    # Sumario todos, SOLO SUPERVISOR
    path('api/supervisor/sumario_agentes/<str:inicio>/<str:fin>/', sumario.SumarioAgentesTodos.as_view()),

    # Sumario por agente
    path('api/supervisor/sumario_agente/<int:idagente>/<str:inicio>/<str:fin>/', sumario.SumarioAgentes.as_view()),
    
    #------------------------------------ API para historias de usuario ---------------------------------
    path('api/formulario_contactenos/', historias_usuario.formulario_contactenos),
    path('api/formulario_cotizar/', historias_usuario.formulario_cotizar),
    path('api/login_app/', historias_usuario.login),
    path('api/cambiar_password/', historias_usuario.cambiar_password),
    path('api/recuperar_password/', historias_usuario.actualizar_password),
    path('api/obtener_ofertas/', historias_usuario.obtener_oferta),
    
    
]