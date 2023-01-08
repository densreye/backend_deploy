from ast import Str
from enum import unique
from django.db import models



class Compania(models.Model):
    idCompania = models.AutoField(db_column='idCompania', primary_key=True)  # Field name made lowercase.
    nombreCompania = models.CharField(db_column='nombreCompania', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ruc = models.CharField(unique=True, max_length=45, blank=True, null=True)
    nombreCoordinador = models.CharField(db_column='nombreCoordinador', max_length=45, blank=True, null=True)  # Field name made lowercase.
    celular = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Compania'
    def __str__(self):
        return self.nombreCompania


class Plan(models.Model):
    idPlan = models.AutoField(db_column='idPlan', primary_key=True)  # Field name made lowercase.
    idCompania = models.ForeignKey(Compania,  db_column='idCompania', blank=True, null=True,on_delete=models.CASCADE)  # Field name made lowercase.
    tipoDePlan = models.CharField(db_column='tipoDePlan', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tipoDeSeguro = models.CharField(db_column='tipoDeSeguro', max_length=45, blank=True, null=True)  # Field name made lowercase.
    nombrePlan = models.CharField(db_column='nombrePlan', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tieneLimite = models.IntegerField(db_column='tieneLimite', blank=True, null=True)  # Field name made lowercase.
    cobertura = models.FloatField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)
    
     #campos adicionales
    genero= models.CharField(max_length=50, blank=True, null=True)
    edad_minima= models.CharField(max_length=50, blank=True, null=True)
    edad_maxima= models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Plan'
    def __str__(self):
        return self.nombrePlan



class Deducible(models.Model):
    idDeducible = models.AutoField(db_column='idDeducible', primary_key=True)  # Field name made lowercase.
    idPlan = models.ForeignKey('Plan',related_name="deducible", db_column='idPlan',on_delete=models.CASCADE)  # Field name made lowercase.
    tipoDeducible = models.CharField(db_column='tipoDeducible', max_length=45, blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Deducible'



class Persona(models.Model):
    idPersona = models.AutoField(db_column='idPersona', primary_key=True)  # Field name made lowercase.    
    idUsuario = models.ForeignKey("Usuario", models.CASCADE, db_column='idUsuario',null=True,blank=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellido = models.CharField(max_length=45, blank=True, null=True)
    tipodeIdentificacion = models.CharField(db_column='tipoDeIdentificacion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    numeroIdentificacion = models.CharField(unique=True,db_column='numeroIdentificacion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fechaNacimiento = models.DateField(db_column='fechaNacimiento', blank=True, null=True)  # Field name made lowercase.
    
    sexo = models.CharField(max_length=45, blank=True, null=True)
    estadoCivil = models.CharField(db_column='estadoCivil', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tipoPersona = models.CharField(db_column='tipoPersona', max_length=45, blank=True, null=True)  # Field name made lowercase.
    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'Persona'
    def __str__(self):
        return  ' %s %s' % (self.nombre,self.apellido)





class Direccion(models.Model):
    idDireccion = models.AutoField(db_column='idDireccion', primary_key=True)  # Field name made lowercase.
    idPersona = models.ForeignKey(Persona, models.CASCADE, db_column='idPersona', blank=True, null=True)  # Field name made lowercase.
    tipoDireccion = models.CharField(db_column='tipoDireccion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pais = models.CharField(max_length=45, blank=True, null=True)
    provincia = models.CharField(max_length=45, blank=True, null=True)
    ciudad = models.CharField(max_length=45, blank=True, null=True)
    datoDireccion = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Direccion'

    def __str__(self):
        return  '%s , %s %s' % (self.ciudad,self.idPersona.nombre,self.idPersona.apellido)

class Usuario(models.Model):
    idusuario = models.AutoField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    nombreusuario = models.CharField(db_column='nombreUsuario', unique=True, max_length=45)  # Field name made lowercase.
    claveusuario = models.CharField(db_column='claveUsuario', max_length=255)  # Field name made lowercase.
    token = models.CharField(max_length=45, blank=True, null=True)
    fotousuario = models.CharField(db_column='fotoUsuario', max_length=45, blank=True, null=True)  # Field name made lowercase.

    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Usuario'


    def __str__(self):
        return  '%s , %s ' % (self.idusuario,self.nombreusuario)


class Cargo(models.Model):
    idCargo = models.AutoField(db_column='idCargo', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Cargo'
    def __str__(self):
        return  '%s , %s' % (self.idCargo,self.descripcion)



class Empleado(models.Model):
    idEmpleado = models.AutoField(db_column='idEmpleado', primary_key=True)  # Field name made lowercase.
    idPersona = models.ForeignKey('Persona', models.CASCADE, db_column='idPersona')  # Field name made lowercase.
    fechaIngresoNoboa = models.DateField(db_column='fechaIngresoNoboa', blank=True, null=True)  # Field name made lowercase.
    idCargo = models.ForeignKey(Cargo, models.CASCADE, db_column='idCargo', blank=True, null=True)  # Field name made lowercase.

    celular = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(unique=True,max_length=45, blank=True, null=True)

    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Empleado'
    def __str__(self):
        return  '%s %s' % (self.idPersona.nombre,self.idPersona.apellido)



class DocumentoEmpleado(models.Model):
    idDocumento = models.AutoField(db_column='idDocumento', primary_key=True)  # Field name made lowercase.
    idEmpleado = models.ForeignKey('Empleado', models.CASCADE, db_column='idEmpleado')  # Field name made lowercase.
    urlArchivo = models.CharField(db_column='urlArchivo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tipoDocumento = models.CharField(db_column='tipoDocumento', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descripcionDocumento = models.CharField(db_column='descripcionDocumento', max_length=255, blank=True, null=True)  # Field name made lowercase.

    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DocumentoEmpleado'

    def __str__(self):
        return  '%s %s %s' % (self.idEmpleado.idPersona.nombre,self.idEmpleado.idPersona.apellido,self.urlArchivo)

class DatosFinancieros(models.Model):
    idDatosFinancieros = models.AutoField(db_column='idDatosFinancieros', primary_key=True)  # Field name made lowercase.
    idCliente = models.ForeignKey("Cliente", models.CASCADE, db_column='idCliente')  # Field name made lowercase.    
    razonSocial = models.CharField(max_length=255, blank=True, null=True)
    tipoActividadEconomica = models.CharField(max_length=45, blank=True, null=True)
    actividadEconomicaPrincipal = models.CharField(max_length=45, blank=True, null=True)
    tiempoEmpleo = models.IntegerField(blank=True, null=True)
    cargo = models.CharField(max_length=45, blank=True, null=True)
    ingresoMensual = models.FloatField(blank=True, null=True)
    ingresoExtra = models.FloatField(blank=True, null=True)
    actividadExtra = models.CharField(max_length=45, blank=True, null=True)
    totalIngresos = models.FloatField(blank=True, null=True)
    totalActivos = models.FloatField(blank=True, null=True)
    totalEgresos = models.FloatField(blank=True, null=True)
    totalPasivos = models.FloatField(blank=True, null=True)

    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'DatosFinancieros'
    def __str__(self):
        return  '%s %s' % (self.idDatosFinancieros,self.tipoActividadEconomica)



class Cliente(models.Model):
    idCliente = models.AutoField(db_column='idCliente', primary_key=True)  # Field name made lowercase.
    idPersona = models.ForeignKey(Persona, models.CASCADE, db_column='idPersona')  # Field name made lowercase.
    idDatosFinancieros = models.OneToOneField(DatosFinancieros, models.DO_NOTHING, db_column='idDatosFinancieros',blank=True, null=True)  # Field name made lowercase.
    idDatosFacturacion = models.OneToOneField("DatosFacturacion", models.DO_NOTHING, db_column='idDatosFacturacion',blank=True, null=True)  # Field name made lowercase.
    idPreexistencia = models.OneToOneField("preexistencia", models.DO_NOTHING, db_column='idPreexistencia',blank=True, null=True)  # Field name made lowercase.
    talla = models.CharField(max_length=45, blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    esBeneficiario = models.IntegerField(db_column='esBeneficiario', blank=True, null=True)  # Field name made lowercase.
    celular = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)

    referidoNombre = models.CharField(max_length=45, blank=True, null=True)
    referidoCorreo = models.CharField(max_length=45, blank=True, null=True)
    referidoCelular = models.CharField(max_length=45, blank=True, null=True)

    ingresoNoboa = models.DateField(blank=True, null=True)
    agenteAsignado = models.ForeignKey(Empleado, models.CASCADE, db_column='agenteAsignado', blank=True, null=True)  # Field name made lowercase.    

    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'Cliente'

    def __str__(self):
        return  '%s %s' % (self.idPersona.nombre,self.idPersona.apellido)


class Dependiente(models.Model):
    idDependiente = models.AutoField(db_column='idDependiente', primary_key=True)  # Field name made lowercase.
    idCliente = models.ForeignKey(Cliente, models.CASCADE, db_column='idCliente')  # Field name made lowercase.
    idPreexistencia = models.OneToOneField("preexistencia", models.DO_NOTHING, db_column='idPreexistencia',blank=True, null=True)  # Field name made lowercase.
    talla = models.FloatField(blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    nombres = models.CharField(max_length=45, blank=True, null=True)
    apellidos = models.CharField(max_length=45, blank=True, null=True)
    tipoDeIdentificacion = models.CharField(db_column='tipoDeIdentificacion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    numeroIdentificacion = models.CharField(db_column='numeroIdentificacion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    celular = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)
    parentesco = models.CharField(max_length=45, blank=True, null=True)

    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'Dependiente'
    def __str__(self):
        return  '%s %s | %s' % (self.apellidos,self.nombres,self.idCliente.idPersona.apellido)


class DocumentoFinanciero(models.Model):
    idDocumento = models.AutoField(db_column='idDocumento', primary_key=True)  # Field name made lowercase.
    idCliente = models.ForeignKey(Cliente, models.CASCADE, db_column='idCliente',blank=True, null=True)  # Field name made lowercase.
    urlArchivo = models.CharField(db_column='urlArchivo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tipoDocumento = models.CharField(db_column='tipoDocumento', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descripcionDocumento = models.CharField(db_column='descripcionDocumento', max_length=255, blank=True, null=True)  # Field name made lowercase.

    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DocumentoFinanciero'

    def __str__(self):
        return  '%s %s %s' % (self.idDocumento ,self.idCliente,self.urlArchivo)




class DatosFacturacion(models.Model):
    idDatosFacturacion = models.AutoField(db_column='idDatosFacturacion', primary_key=True)  # Field name made lowercase.
    idCliente = models.ForeignKey(Cliente, models.CASCADE, db_column='idCliente')  # Field name made lowercase.

    tipoDeIdentificacion = models.CharField(db_column='tipoDeIdentificacion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    numeroIdentificacion = models.CharField(db_column='numeroIdentificacion', max_length=45, blank=True, null=True)  # Field name made lowercase.

    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellido = models.CharField(max_length=45, blank=True, null=True)
    
    celular = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)
    
    tipoFormadePago = models.CharField(max_length=45, blank=True, null=True)
    nombreTarjeta = models.CharField(max_length=45, blank=True, null=True)
    nombreInstitucionBancaria = models.CharField(max_length=45, blank=True, null=True)
    numeroCuenta = models.CharField(max_length=45, blank=True, null=True)

    contactoNombre = models.CharField(max_length=45, blank=True, null=True)
    contactoCorreo = models.CharField(max_length=45, blank=True, null=True)
    contactoCelular = models.CharField(max_length=45, blank=True, null=True)

    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'datosFacturacion'
    def __str__(self):
        return  '%s %s | %s' % (self.apellido,self.nombre,self.idCliente.idPersona.apellido)





class Preexistencia(models.Model):
    idPreexistencia = models.AutoField(db_column='idPreexistencia', primary_key=True)  # Field name made lowercase.
    idCliente = models.ForeignKey(Cliente, models.CASCADE, db_column='idCliente',blank=True, null=True)  # Field name made lowercase.
    idDependiente = models.ForeignKey(Dependiente, models.CASCADE, db_column='idDependiente',blank=True, null=True)  # Field name made lowercase.
    esTitular = models.IntegerField(blank=True, null=True)

    diagnosticoDetalle = models.CharField(max_length=1000, blank=True, null=True)
    inicioEnfermedad = models.DateField(blank=True, null=True)
    continuaEnfermedad = models.IntegerField(blank=True, null=True)
    tratamientoResultados = models.CharField(max_length=1000, blank=True, null=True)
    descripcionEstadoActual = models.CharField(max_length=1000, blank=True, null=True)


    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'preexistencia'

    def __str__(self):
        return  '%s  %s' % (self.idPreexistencia,self.diagnosticoDetalle )




class Contrato(models.Model):
    idContrato = models.AutoField(db_column='idContrato', primary_key=True)  # Field name made lowercase.
    idCliente = models.ForeignKey(Cliente, models.CASCADE, db_column='idCliente',blank=True, null=True)  # Field name made lowercase.
    idPlan = models.ForeignKey(Plan, models.CASCADE, db_column='idPlan',blank=True, null=True)  # Field name made lowercase.
    
    codigoContrato = models.CharField(max_length=255, blank=True, null=True,unique=True)

    idAgente = models.ForeignKey(Empleado, models.CASCADE, db_column='idAgente',blank=True, null=True)  # Field name made lowercase.
    comisionAgente = models.FloatField(blank=True, null=True)
    porcentajeComisionAgente = models.FloatField(blank=True, null=True)

    fechaIngreso = models.DateField(blank=True, null=True)
    fechaVigencia = models.DateField(blank=True, null=True)
    fechaPrimerCuota = models.DateField(blank=True, null=True)

    valorPrimeraCuota = models.FloatField(blank=True, null=True)
    valorPagoAnual = models.FloatField(blank=True, null=True)

    primaAnioActual = models.FloatField(blank=True, null=True)
    modalidadPrima = models.CharField(max_length=45, blank=True, null=True)
    valorCuotaPrima = models.FloatField(blank=True, null=True)
    primaAnioSeiguiente = models.FloatField(blank=True, null=True)
    aumentoPrima = models.FloatField(blank=True, null=True)
    porcentajeAumentoPrima = models.FloatField(blank=True, null=True)

    estadoContratoFirma = models.IntegerField(blank=True, null=True)
    diaFirma = models.DateField(blank=True, null=True)
    fechaFirmaContrato = models.DateField(blank=True, null=True)

    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)
    dependientes = models.ManyToManyField(Dependiente,through="dependientesContrato",related_name="contratos")

    class Meta:
        managed = False
        db_table = 'contrato'

    def __str__(self):
        return  '%s' % (self.idContrato)



class DependientesContrato(models.Model):
    idDependientesContrato = models.AutoField(db_column='idDependientesContrato', primary_key=True)  # Field name made lowercase.
    idDependiente = models.ForeignKey(Dependiente, models.CASCADE, db_column='idDependiente',blank=True, null=True)  # Field name made lowercase.
    idContrato = models.ForeignKey(Contrato, models.CASCADE, db_column='idContrato',blank=True, null=True)  # Field name made lowercase.
    
    is_active = models.IntegerField(blank=True, null=True,default=1)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)
    

    class Meta:
        managed = False
        unique_together=[['idDependiente','idContrato']]
        db_table = 'dependientesContrato'

    def __str__(self):
        return  '%s' % (self.idDependientesContrato)


class DocumentoPreexistencia(models.Model):
    idDocumento = models.AutoField(db_column='idDocumento', primary_key=True)  # Field name made lowercase.
    idCliente = models.ForeignKey(Cliente, models.CASCADE, db_column='idCliente',blank=True, null=True)  # Field name made lowercase.
    idDependiente = models.ForeignKey(Dependiente, models.CASCADE, db_column='idDependiente',blank=True, null=True)  # Field name made lowercase.

    urlArchivo = models.CharField(db_column='urlArchivo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tipoDocumento = models.CharField(db_column='tipoDocumento', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descripcionDocumento = models.CharField(db_column='descripcionDocumento', max_length=255, blank=True, null=True)  # Field name made lowercase.

    ruta = models.CharField(db_column='ruta', max_length=45, blank=True, null=True)  # Field name made lowercase.
    nombreArchivo = models.CharField(db_column='nombreArchivo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    esTitular = models.IntegerField(blank=True, null=True)


    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DocumentoPreexistencia'

    def __str__(self):
        return  '%s %s %s' % (self.idDocumento ,self.idCliente,self.urlArchivo)

class DocumentoSistema(models.Model):
    idDocumento = models.AutoField(db_column='idDocumento', primary_key=True)  # Field name made lowercase.

    nombreArchivo = models.CharField(db_column='nombreArchivo', max_length=255, blank=True, null=True)  
    pathArchivo = models.CharField(db_column='pathArchivo', max_length=255, blank=True, null=True)  
    urlArchivo = models.CharField(db_column='urlArchivo', max_length=255, blank=True, null=True)  
    

    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DocumentoSistema'

    def __str__(self):
        return  '%s %s %s' % (self.idDocumento ,self.nombreArchivo,self.pathArchivo)

