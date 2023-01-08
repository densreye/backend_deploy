# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cargo(models.Model):
    idcargo = models.AutoField(db_column='idCargo', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)

    class Meta:
            
            db_table = 'cargo'

class Cliente(models.Model):
    idcliente = models.AutoField(db_column='idCliente', primary_key=True)  # Field name made lowercase.
    idpersona = models.ForeignKey('persona', models.DO_NOTHING, db_column='idPersona')  # Field name made lowercase.
    iddatosfacturacion = models.IntegerField(db_column='idDatosFacturacion', blank=True, null=True)  # Field name made lowercase.
    iddatosfinancieros = models.IntegerField(db_column='idDatosFinancieros', blank=True, null=True)  # Field name made lowercase.
    iddatospreexistencia = models.IntegerField(db_column='idDatosPreexistencia', blank=True, null=True)  # Field name made lowercase.
    idsolicitud = models.IntegerField(db_column='idSolicitud', blank=True, null=True)  # Field name made lowercase.
    talla = models.CharField(max_length=45, blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    esbeneficiario = models.IntegerField(db_column='esBeneficiario', blank=True, null=True)  # Field name made lowercase.
    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)
    celular = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)
    referidonombre = models.CharField(db_column='referidoNombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    referidocorreo = models.CharField(db_column='referidoCorreo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    referidocelular = models.CharField(db_column='referidoCelular', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ingresonoboa = models.DateField(db_column='ingresoNoboa', blank=True, null=True)  # Field name made lowercase.
    agenteasignado = models.ForeignKey('empleado', models.DO_NOTHING, db_column='agenteAsignado', blank=True, null=True)  # Field name made lowercase.
    idpreexistencia = models.ForeignKey('preexistencia', models.DO_NOTHING, db_column='idPreexistencia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'cliente'


class Clientedependiente(models.Model):
    idclientedependiente = models.AutoField(db_column='idClienteDependiente', primary_key=True)  # Field name made lowercase.
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='idCliente')  # Field name made lowercase.
    iddependiente = models.ForeignKey('dependiente', models.DO_NOTHING, db_column='idDependiente')  # Field name made lowercase.
    parentescocontitular = models.CharField(db_column='parentescoConTitular', max_length=45, blank=True, null=True)  # Field name made lowercase.
    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'clientedependiente'


class Compania(models.Model):
    idcompania = models.AutoField(db_column='idCompania', primary_key=True)  # Field name made lowercase.
    nombrecompania = models.CharField(db_column='nombreCompania', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ruc = models.CharField(max_length=45, blank=True, null=True)
    nombrecoordinador = models.CharField(db_column='nombreCoordinador', max_length=45, blank=True, null=True)  # Field name made lowercase.
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
        
        db_table = 'compania'


class Contactoprospecto(models.Model):
    idcontactoprospecto = models.AutoField(db_column='idContactoProspecto', primary_key=True)  # Field name made lowercase.
    contenido = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    idprospecto = models.ForeignKey('prospecto', models.DO_NOTHING, db_column='idProspecto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'contactoprospecto'


class Cotizacion(models.Model):
    idcotizacion = models.AutoField(db_column='idCotizacion', primary_key=True)  # Field name made lowercase.
    idprospecto = models.ForeignKey('prospecto', models.DO_NOTHING, db_column='idProspecto', blank=True, null=True)  # Field name made lowercase.
    idplan = models.ForeignKey('plan', models.DO_NOTHING, db_column='idPlan')  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    motivocierre = models.TextField(blank=True, null=True)
    modificado = models.DateTimeField(db_column='Modificado')  # Field name made lowercase.
    creado = models.DateTimeField(db_column='Creado')  # Field name made lowercase.
    filepath = models.TextField(blank=True, null=True)

    class Meta:
        
        db_table = 'cotizacion'


class Datosfinancieros(models.Model):
    iddatosfinancieros = models.AutoField(db_column='idDatosFinancieros', primary_key=True)  # Field name made lowercase.
    tipoactividadeconomica = models.CharField(db_column='tipoActividadEconomica', max_length=45, blank=True, null=True)  # Field name made lowercase.
    actividadeconomicaprincipal = models.CharField(db_column='actividadEconomicaPrincipal', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tiempoempleo = models.IntegerField(db_column='tiempoEmpleo', blank=True, null=True)  # Field name made lowercase.
    cargo = models.CharField(max_length=45, blank=True, null=True)
    ingresomensual = models.FloatField(db_column='ingresoMensual', blank=True, null=True)  # Field name made lowercase.
    ingresoextra = models.FloatField(db_column='ingresoExtra', blank=True, null=True)  # Field name made lowercase.
    actividadextra = models.CharField(db_column='actividadExtra', max_length=255, blank=True, null=True)  # Field name made lowercase.
    totalingresos = models.FloatField(db_column='totalIngresos', blank=True, null=True)  # Field name made lowercase.
    totalactivos = models.FloatField(db_column='totalActivos', blank=True, null=True)  # Field name made lowercase.
    totalegresos = models.FloatField(db_column='totalEgresos', blank=True, null=True)  # Field name made lowercase.
    totalpasivos = models.FloatField(db_column='totalPasivos', blank=True, null=True)  # Field name made lowercase.
    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='idCliente', blank=True, null=True)  # Field name made lowercase.
    razonsocial = models.CharField(db_column='razonSocial', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'datosfinancieros'


class Deducible(models.Model):
    iddeducible = models.AutoField(db_column='idDeducible', primary_key=True)  # Field name made lowercase.
    idplan = models.ForeignKey('plan', models.DO_NOTHING, db_column='idPlan')  # Field name made lowercase.
    tipodeducible = models.CharField(db_column='tipoDeducible', max_length=45, blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'deducible'


class Dependiente(models.Model):
    iddependiente = models.AutoField(db_column='idDependiente', primary_key=True)  # Field name made lowercase.
    peso = models.FloatField(blank=True, null=True)
    nombres = models.CharField(max_length=45, blank=True, null=True)
    apellidos = models.CharField(max_length=45, blank=True, null=True)
    tipodeidentificacion = models.CharField(db_column='tipoDeIdentificacion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    numeroidentificacion = models.CharField(db_column='numeroIdentificacion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    celular = models.CharField(max_length=45, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='idCliente', blank=True, null=True)  # Field name made lowercase.
    talla = models.FloatField(blank=True, null=True)
    parentesco = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)
    idpreexistencia = models.ForeignKey('preexistencia', models.DO_NOTHING, db_column='idPreexistencia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'dependiente'


class Direccion(models.Model):
    iddireccion = models.AutoField(db_column='idDireccion', primary_key=True)  # Field name made lowercase.
    idpersona = models.ForeignKey('persona', models.DO_NOTHING, db_column='idPersona', blank=True, null=True)  # Field name made lowercase.
    tipodireccion = models.CharField(db_column='tipoDireccion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pais = models.CharField(max_length=45, blank=True, null=True)
    provincia = models.CharField(max_length=45, blank=True, null=True)
    ciudad = models.CharField(max_length=45, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)
    datodireccion = models.CharField(db_column='datoDireccion', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'direccion'


class Documentodependiente(models.Model):
    iddocumento = models.AutoField(db_column='idDocumento', primary_key=True)  # Field name made lowercase.
    iddependiente = models.ForeignKey(Dependiente, models.DO_NOTHING, db_column='idDependiente')  # Field name made lowercase.
    urlarchivo = models.CharField(db_column='urlArchivo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tipodocumento = models.CharField(db_column='tipoDocumento', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descripciondocumento = models.CharField(db_column='descripcionDocumento', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'documentodependiente'


class Documentoempleado(models.Model):
    iddocumento = models.AutoField(db_column='idDocumento', primary_key=True)  # Field name made lowercase.
    idempleado = models.ForeignKey('empleado', models.DO_NOTHING, db_column='idEmpleado')  # Field name made lowercase.
    urlarchivo = models.CharField(db_column='urlArchivo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tipodocumento = models.CharField(db_column='tipoDocumento', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descripciondocumento = models.CharField(db_column='descripcionDocumento', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'documentoempleado'


class Documentofinanciero(models.Model):
    iddocumento = models.AutoField(db_column='idDocumento', primary_key=True)  # Field name made lowercase.
    urlarchivo = models.CharField(db_column='urlArchivo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tipodocumento = models.CharField(db_column='tipoDocumento', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descripciondocumento = models.CharField(db_column='descripcionDocumento', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='idCliente', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'documentofinanciero'


class Empleado(models.Model):
    idempleado = models.AutoField(db_column='idEmpleado', primary_key=True)  # Field name made lowercase.
    idpersona = models.ForeignKey('persona', models.DO_NOTHING, db_column='idPersona')  # Field name made lowercase.
    fechaingresonoboa = models.DateField(db_column='fechaIngresoNoboa', blank=True, null=True)  # Field name made lowercase.
    idcargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='idCargo', blank=True, null=True)  # Field name made lowercase.
    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)
    celular = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        
        db_table = 'empleado'


class Notificacionventas(models.Model):
    idnotificacion = models.AutoField(db_column='idNotificacion', primary_key=True)  # Field name made lowercase.
    idsupervisor = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='idSupervisor', blank=True, null=True)  # Field name made lowercase.
    titulo = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    contenido = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    creado = models.DateTimeField()

    class Meta:
        
        db_table = 'notificacionventas'


class Notificacionventasremitentes(models.Model):
    idnotificacion = models.OneToOneField(Notificacionventas, models.DO_NOTHING, db_column='idNotificacion', primary_key=True)  # Field name made lowercase.
    idagente = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='idAgente')  # Field name made lowercase.
    visto = models.IntegerField()

    class Meta:
        
        db_table = 'notificacionventasremitentes'
        unique_together = (('idnotificacion', 'idagente'),)


class Persona(models.Model):
    idpersona = models.AutoField(db_column='idPersona', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellido = models.CharField(max_length=45, blank=True, null=True)
    tipodeidentificacion = models.CharField(db_column='tipoDeIdentificacion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    numeroidentificacion = models.CharField(db_column='numeroIdentificacion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fechanacimiento = models.DateField(db_column='fechaNacimiento', blank=True, null=True)  # Field name made lowercase.
    edad = models.IntegerField(blank=True, null=True)
    sexo = models.CharField(max_length=45, blank=True, null=True)
    tipopersona = models.CharField(db_column='tipoPersona', max_length=45, blank=True, null=True)  # Field name made lowercase.
    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)
    estadocivil = models.CharField(db_column='estadoCivil', max_length=45, blank=True, null=True)  # Field name made lowercase.
    idusuario = models.ForeignKey('usuario', models.DO_NOTHING, db_column='idUsuario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'persona'


class Plan(models.Model):
    idplan = models.AutoField(db_column='idPlan', primary_key=True)  # Field name made lowercase.
    idcompania = models.ForeignKey(Compania, models.DO_NOTHING, db_column='idCompania', blank=True, null=True)  # Field name made lowercase.
    tipodeplan = models.CharField(db_column='tipoDePlan', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tipodeseguro = models.CharField(db_column='tipoDeSeguro', max_length=45, blank=True, null=True)  # Field name made lowercase.
    nombreplan = models.CharField(db_column='nombrePlan', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tienelimite = models.IntegerField(db_column='tieneLimite', blank=True, null=True)  # Field name made lowercase.
    cobertura = models.FloatField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)
    detalle = models.TextField(blank=True, null=True)

    #campos adicionales
    genero= models.CharField(max_length=50, blank=True, null=True)
    edad_minima= models.CharField(max_length=50, blank=True, null=True)
    edad_maxima= models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'plan'


class Prospecto(models.Model):
    idprospecto = models.AutoField(db_column='idProspecto', primary_key=True)  # Field name made lowercase.
    idagente = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='idAgente', blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellido = models.CharField(max_length=45, blank=True, null=True)
    genero = models.CharField(max_length=45, blank=True, null=True)
    edad = models.CharField(max_length=45, blank=True, null=True)
    categoria = models.IntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=45, blank=True, null=True)
    proyectadoactual = models.FloatField(db_column='proyectadoActual', blank=True, null=True)  # Field name made lowercase.
    urlarchivo = models.CharField(db_column='urlArchivo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    creado = models.DateTimeField()

    class Meta:
        
        db_table = 'prospecto'


class Prospectosesion(models.Model):
    idprospectosesion = models.AutoField(db_column='idProspectoSesion', primary_key=True)  # Field name made lowercase.
    idprospecto = models.ForeignKey(Prospecto, models.DO_NOTHING, db_column='idProspecto', blank=True, null=True)  # Field name made lowercase.
    inicio = models.DateTimeField(blank=True, null=True)
    fin = models.DateTimeField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    detalle = models.TextField(blank=True, null=True)
    idcontactoprospecto = models.ForeignKey(Contactoprospecto, models.DO_NOTHING, db_column='idContactoProspecto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'prospectosesion'


class Usuario(models.Model):
    idusuario = models.AutoField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    idpersona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='idPersona', blank=True, null=True)  # Field name made lowercase.
    nombreusuario = models.CharField(db_column='nombreUsuario', max_length=45, blank=True, null=True)  # Field name made lowercase.
    claveusuario = models.CharField(max_length=255, blank=True, null=True)
    token = models.CharField(max_length=45, blank=True, null=True)
    fotousuario = models.CharField(db_column='fotoUsuario', max_length=45, blank=True, null=True)  # Field name made lowercase.
    correo = models.CharField(max_length=45, blank=True, null=True)  # Field name made lowercase.
    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'usuario'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Contrato(models.Model):
    idcontrato = models.AutoField(db_column='idContrato', primary_key=True)  # Field name made lowercase.
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='idCliente', blank=True, null=True)  # Field name made lowercase.
    idplan = models.ForeignKey(Plan, models.DO_NOTHING, db_column='idPlan', blank=True, null=True)  # Field name made lowercase.
    codigocontrato = models.CharField(db_column='codigoContrato', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idagente = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='idAgente', blank=True, null=True)  # Field name made lowercase.
    comisionagente = models.FloatField(db_column='comisionAgente', blank=True, null=True)  # Field name made lowercase.
    porcentajecomisionagente = models.FloatField(db_column='porcentajeComisionAgente', blank=True, null=True)  # Field name made lowercase.
    fechaingreso = models.DateField(db_column='fechaIngreso', blank=True, null=True)  # Field name made lowercase.
    fechavigencia = models.DateField(db_column='fechaVigencia', blank=True, null=True)  # Field name made lowercase.
    fechaprimercuota = models.DateField(db_column='fechaPrimerCuota', blank=True, null=True)  # Field name made lowercase.
    valorprimeracuota = models.FloatField(db_column='valorPrimeraCuota', blank=True, null=True)  # Field name made lowercase.
    valorpagoanual = models.FloatField(db_column='valorPagoAnual', blank=True, null=True)  # Field name made lowercase.
    primaanioactual = models.FloatField(db_column='primaAnioActual', blank=True, null=True)  # Field name made lowercase.
    modalidadprima = models.CharField(db_column='modalidadPrima', max_length=45, blank=True, null=True)  # Field name made lowercase.
    valorcuotaprima = models.FloatField(db_column='valorCuotaPrima', blank=True, null=True)  # Field name made lowercase.
    primaanioseiguiente = models.FloatField(db_column='primaAnioSeiguiente', blank=True, null=True)  # Field name made lowercase.
    aumentoprima = models.FloatField(db_column='aumentoPrima', blank=True, null=True)  # Field name made lowercase.
    porcentajeaumentoprima = models.FloatField(db_column='porcentajeAumentoPrima', blank=True, null=True)  # Field name made lowercase.
    estadocontratofirma = models.IntegerField(db_column='estadoContratoFirma', blank=True, null=True)  # Field name made lowercase.
    diafirma = models.DateField(db_column='diaFirma', blank=True, null=True)  # Field name made lowercase.
    fechafirmacontrato = models.DateField(db_column='fechaFirmaContrato', blank=True, null=True)  # Field name made lowercase.
    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'contrato'


class Datosfacturacion(models.Model):
    iddatosfacturacion = models.AutoField(db_column='idDatosFacturacion', primary_key=True)  # Field name made lowercase.
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='idCliente')  # Field name made lowercase.
    tipodeidentificacion = models.CharField(db_column='tipoDeIdentificacion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    numeroidentificacion = models.CharField(db_column='numeroIdentificacion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellido = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)
    celular = models.CharField(max_length=45, blank=True, null=True)
    tipoformadepago = models.CharField(db_column='tipoFormadePago', max_length=45, blank=True, null=True)  # Field name made lowercase.
    nombretarjeta = models.CharField(db_column='nombreTarjeta', max_length=45, blank=True, null=True)  # Field name made lowercase.
    nombreinstitucionbancaria = models.CharField(db_column='nombreInstitucionBancaria', max_length=45, blank=True, null=True)  # Field name made lowercase.
    numerocuenta = models.CharField(db_column='numeroCuenta', max_length=45, blank=True, null=True)  # Field name made lowercase.
    contactonombre = models.CharField(db_column='contactoNombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    contactocorreo = models.CharField(db_column='contactoCorreo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    contactocelular = models.CharField(db_column='contactoCelular', max_length=45, blank=True, null=True)  # Field name made lowercase.
    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'datosFacturacion'


class Dependientescontrato(models.Model):
    iddependientescontrato = models.AutoField(db_column='idDependientesContrato', primary_key=True)  # Field name made lowercase.
    iddependiente = models.ForeignKey(Dependiente, models.DO_NOTHING, db_column='idDependiente')  # Field name made lowercase.
    idcontrato = models.ForeignKey(Contrato, models.DO_NOTHING, db_column='idContrato')  # Field name made lowercase.
    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'dependientesContrato'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Preexistencia(models.Model):
    idpreexistencia = models.AutoField(db_column='idPreexistencia', primary_key=True)  # Field name made lowercase.
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='idCliente', blank=True, null=True)  # Field name made lowercase.
    iddependiente = models.ForeignKey(Dependiente, models.DO_NOTHING, db_column='idDependiente', blank=True, null=True)  # Field name made lowercase.
    estitular = models.IntegerField(db_column='esTitular', blank=True, null=True)  # Field name made lowercase.
    diagnosticodetalle = models.CharField(db_column='diagnosticoDetalle', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    inicioenfermedad = models.DateField(db_column='inicioEnfermedad', blank=True, null=True)  # Field name made lowercase.
    continuaenfermedad = models.IntegerField(db_column='continuaEnfermedad', blank=True, null=True)  # Field name made lowercase.
    tratamientoresultados = models.CharField(db_column='tratamientoResultados', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    descripcionestadoactual = models.CharField(db_column='descripcionEstadoActual', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    is_active = models.IntegerField(blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    creado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    creado_id_usuario = models.IntegerField(blank=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    modificado_por_usuario = models.CharField(max_length=45, blank=True, null=True)
    modificado_id_usuario = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'preexistencia'


#nuevos modelos
class Formulario_Contactenos(models.Model):
    nombres= models.CharField(max_length=100, blank=True, null=True)
    apellidos= models.CharField(max_length=100, blank=True, null=True)
    correo= models.CharField(max_length=100, blank=True, null=True)
    celular= models.CharField(max_length=50, blank=True, null=True)
    genero=models.CharField(max_length=50, blank=True, null=True)
    edad= models.CharField(max_length=50, blank=True, null=True)
    comentarios= models.CharField(max_length=200, blank=True, null=True)
    
    #campos para visualizar en el admin de django
    def __str__(self):
        return self.nombres
  

#modelo ofertas vinculado con los planes
class Ofertas(models.Model):
    
    idplan = models.ForeignKey('plan', models.DO_NOTHING, db_column='idPlan')  # Field name made lowercase.
    
    fecha_desde= models.CharField(max_length=100, blank=True, null=True)
    fecha_hasta= models.CharField(max_length=100, blank=True, null=True)
    precio_antes= models.CharField(max_length=100, blank=True, null=True)
    precio_despues= models.CharField(max_length=100, blank=True, null=True)
    cobertura_accidentes= models.CharField(max_length=100, blank=True, null=True)
    
    
class Mis_planes(models.Model):
    idPersona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='idPersona', blank=True, null=True)  # Field name made lowercase.
    idplan = models.ForeignKey(Plan, models.DO_NOTHING, db_column='idPlan', blank=True, null=True)  # Field name made lowercase.
    