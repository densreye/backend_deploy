
from django.urls import path, include

from web import viewsplan
from . import views
from .emisiones.cliente import viewscliente
from .emisiones.agente import viewsagente
from .emisiones.dependiene import viewsdependiente
from .emisiones.datosfinancieros import views_datos_financieros
from .emisiones.datosfacturacion import views_datos_facturacion
from .emisiones.preexistencia import views_preexistencia
from .emisiones.utilidades import views_utilidades
from .emisiones.contrato import views_contrato

from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
app_name = "web"

urlpatterns = [
    #path('admin/', admin.site.urls),


    path('', views.index, name = "index"),

    path('compania/', views.CompaniaList.as_view(),name="companialist"),
    path('compania/<int:pk>/', views.CampaniaDetail.as_view(),name="companiadetails"),

    path('plan/', viewsplan.PLanList.as_view(),name="planlist"),
    path('plan/<int:pk>/', viewsplan.PLanDetail.as_view(),name="plandetails"),
    path('plan-compania=<int:idCompania>/',viewsplan.get_plan_compania,name='planDeCompania'),

    path('deducible/', viewsplan.DeducibleList.as_view(),name="deduciblelist"),
    path('deducible/<int:pk>/', viewsplan.DeducibleDetail.as_view(),name="deducibledetails"),

    path('cliente/', viewscliente.ClienteList.as_view(), name="clientelist"),
    path('cliente/<int:pk>/', viewscliente.ClienteDetail.as_view(),name="clientedetails"),
    
    path('agente/', viewsagente.AgenteList.as_view(), name="agentelist"),
    path('agente/<int:pk>/', viewsagente.AgenteDetail.as_view(),name="agentedetails"),
    
    path('dependiente/',viewsdependiente.DependienteList.as_view(),name="dependientelist"),
    path('dependiente&cliente=<int:idCliente>/',viewsdependiente.get_dependiente_cliente,name='dependientecliente'),
    path('dependiente/<int:pk>/',viewsdependiente.DependienteDetail.as_view(),name="dependientedetail"),

    path('datos_financieros/',views_datos_financieros.DatosFinancierosList.as_view(),name="datosFinancierosList"),
    path('datos_financieros&cliente=<int:idCliente>/',views_datos_financieros.get_datos_financieros_cliente,name='datosFinancieroscliente'),
    path('datos_financieros/<int:pk>/',views_datos_financieros.DatosFinancierosDetail.as_view(),name="datosFinancierosDetail"),
    path('datos_financieros&borrararchivo=<int:idDocumento>/',views_datos_financieros.eliminar_documento_financiero,name="eliminarDocumentoFinanciero"),

    path('datos_facturacion/',views_datos_facturacion.DatosFacturacionList.as_view(),name="datosFacturacionList"),
    path('datos_facturacion&cliente=<int:idCliente>/',views_datos_facturacion.get_datos_facturacion_cliente,name='datosFacturacioncliente'),
    path('datos_facturacion/<int:pk>/',views_datos_facturacion.DatosFacturacionDetail.as_view(),name="datosFacturacionDetail"),

    path('preexistencia/',views_preexistencia.PreexistenciaList.as_view(),name="preexistenciaList"),
    path('preexistencia-persona=<int:idPersona>&titular=<int:esTitular>/',views_preexistencia.get_preexistencia_persona,name='preexistenciaEspecifica'),

    path('archivos-preexistencia-persona=<int:idPersona>&titular=<int:esTitular>/',views_preexistencia.cargar_documento_preexistencia_persona,name='cargar_documento_preexistencia_persona'),
    path('eliminar-archivo-hash=<str:hash>/',views_utilidades.eliminar_documento,name='eliminar_documento_sistema'),

    path('contrato/',views_contrato.ContratoList.as_view(),name="contratoListList"),
    path('contrato-cliente=<int:idCliente>/',views_contrato.get_contrato_cliente,name='contratoCliente'),
    path('contrato/<int:pk>/',views_contrato.ContratoDetail.as_view(),name="contratoDetail"),
]
urlpatterns = format_suffix_patterns(urlpatterns)