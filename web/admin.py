from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Compania)
admin.site.register(Plan)
admin.site.register(Deducible)
admin.site.register(Persona)
admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Direccion)
admin.site.register(Cargo)
admin.site.register(Empleado)
admin.site.register(DocumentoEmpleado)
admin.site.register(Dependiente)
admin.site.register(DatosFinancieros)
admin.site.register(DocumentoFinanciero)
admin.site.register(DatosFacturacion)
admin.site.register(Preexistencia)
admin.site.register(Contrato)
admin.site.register(DependientesContrato)