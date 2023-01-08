-------------------------------
-- Schema broker
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `broker` ;
USE `broker` ;

-- -----------------------------------------------------
-- Table `Persona`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Persona` (
  `idPersona` INT NOT NULL AUTO_INCREMENT,
  
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `tipoDeIdentificacion` VARCHAR(45) NULL,
  `numeroIdentificacion` VARCHAR(45) NULL,
  `fechaNacimiento` DATE NULL,
  `edad` INT NULL,
  `sexo` VARCHAR(45) NULL,
  `estadoCivil` VARCHAR(45) NULL,
  `tipoPersona` VARCHAR(45) NULL,
  `idUsuario` int null,
  `celular` VARCHAR(45) NULL,
  `correo` VARCHAR(45) NULL,

  `is_active` TINYINT(1) default 1,
  `fecha_creado` DATE,
  `creado_por_usuario` VARCHAR(45),
  `creado_id_usuario` int,
  `fecha_modificado` DATE,
  `modificado_por_usuario` VARCHAR(45),
  `modificado_id_usuario` int,
  
  PRIMARY KEY (`idPersona`),
	FOREIGN KEY (`idUsuario`)
    REFERENCES `auth_user` (`id`)),
;
  ;



-- -----------------------------------------------------
-- Table `Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Usuario` (
  `idUsuario` INT NOT NULL AUTO_INCREMENT,
  `idPersona` INT NULL,
  `nombreUsuario` VARCHAR(45) NULL,
  `claveUsuario` VARCHAR(255) NOT NULL,
  `token` VARCHAR(45) NULL,
  `fotoUsuario` VARCHAR(45) NULL,
  
  `is_active` TINYINT(1) default 1,
  `fecha_creado` DATE,
  `creado_por_usuario` VARCHAR(45),
  `creado_id_usuario` int,
  `fecha_modificado` DATE,
  `modificado_por_usuario` VARCHAR(45),
  `modificado_id_usuario` int,
  
  PRIMARY KEY (`idUsuario`),
  
    FOREIGN KEY (`idPersona`)
    REFERENCES `Persona` (`idPersona`)
);



-- -----------------------------------------------------
-- Table `Referido`
-- -----------------------------------------------------



-- -----------------------------------------------------
-- Table `Cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Cliente` (
  `idCliente` INT NOT NULL AUTO_INCREMENT,
  `idPersona` INT NOT NULL,
  
  
  `idDatosFacturacion` INT NULL,
  `idDatosFinancieros` INT NULL,
  `idDatosPreexistencia` INT NULL,
  `idSolicitud` TINYINT(1) NULL,
  
  `talla` VARCHAR(45) NULL,
  `peso` FLOAT NULL,
  `esBeneficiario` TINYINT(1) NULL,


  `referidoNombre` VARCHAR(45) NULL,
  `referidoCorreo` VARCHAR(45) NULL,
  `referidoCelular` VARCHAR(45) NULL,

  `ingresoNoboa` date NULL,

  `is_active` TINYINT(1) default 1,
  `fecha_creado` DATE,
  `creado_por_usuario` VARCHAR(45),
  `creado_id_usuario` int,
  `fecha_modificado` DATE,
  `modificado_por_usuario` VARCHAR(45),
  `modificado_id_usuario` int,
  
  
  PRIMARY KEY (`idCliente`),

FOREIGN KEY (`idPersona`)
REFERENCES `Persona` (`idPersona`)
);


-- -----------------------------------------------------
-- Table `Cargo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Cargo` (
  `idCargo` INT NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(255) NULL,
    
  `is_active` TINYINT(1) default 1,
  `fecha_creado` DATE,
  `creado_por_usuario` VARCHAR(45),
  `creado_id_usuario` int,
  `fecha_modificado` DATE,
  `modificado_por_usuario` VARCHAR(45),
  `modificado_id_usuario` int,
  
  PRIMARY KEY (`idCargo`));


-- -----------------------------------------------------
-- Table `Empleado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Empleado` (
  `idEmpleado` INT NOT NULL AUTO_INCREMENT,
  `idPersona` INT NOT NULL,
  `fechaIngresoNoboa` DATE NULL,
  `idCargo` INT NULL,
    
  `is_active` TINYINT(1) default 1,
  `fecha_creado` DATE,
  `creado_por_usuario` VARCHAR(45),
  `creado_id_usuario` int,
  `fecha_modificado` DATE,
  `modificado_por_usuario` VARCHAR(45),
  `modificado_id_usuario` int,
  
  `celular` VARCHAR(45) NULL,
  `correo` VARCHAR(45) NULL ,

  PRIMARY KEY (`idEmpleado`),  
    FOREIGN KEY (`idPersona`)
    REFERENCES `Persona` (`idPersona`),

    FOREIGN KEY (`idCargo`)
    REFERENCES `Cargo` (`idCargo`)
    );

-- -----------------------------------------------------
-- Table `DocumentoEmpleado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DocumentoEmpleado` (
  `idDocumento` INT NOT NULL AUTO_INCREMENT,
  `idEmpleado` INT NOT NULL,
  `urlArchivo` VARCHAR(255) NULL,
  `tipoDocumento` VARCHAR(45) NULL,
  `descripcionDocumento` VARCHAR(255) NULL,
    
  `is_active` TINYINT(1) default 1,
  `fecha_creado` DATE,
  `creado_por_usuario` VARCHAR(45),
  `creado_id_usuario` int,
  `fecha_modificado` DATE,
  `modificado_por_usuario` VARCHAR(45),
  `modificado_id_usuario` int,
  
  PRIMARY KEY (`idDocumento`),
    FOREIGN KEY (`idEmpleado`)
    REFERENCES `Empleado` (`idEmpleado`));


-- -----------------------------------------------------
-- Table `Direccion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Direccion` (
  `idDireccion` INT NOT NULL AUTO_INCREMENT,
  `idPersona` INT NULL,
  `tipoDireccion` VARCHAR(45) NULL,
  `pais` VARCHAR(45) NULL,
  `provincia` VARCHAR(45) NULL,
  `ciudad` VARCHAR(45) NULL,
    
  `is_active` TINYINT(1) default 1,
  `fecha_creado` DATE,
  `creado_por_usuario` VARCHAR(45),
  `creado_id_usuario` int,
  `fecha_modificado` DATE,
  `modificado_por_usuario` VARCHAR(45),
  `modificado_id_usuario` int,
  
  PRIMARY KEY (`idDireccion`),  
    FOREIGN KEY (`idPersona`)
    REFERENCES `Persona` (`idPersona`));


-- -----------------------------------------------------
-- Table `Dependiente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Dependiente` (
  `idDependiente` INT NOT NULL AUTO_INCREMENT,
  `talla` FLOAT NULL,
  `peso` FLOAT NULL,
  `nombres` VARCHAR(45) NULL,
  `apellidos` VARCHAR(45) NULL,
  `tipoDeIdentificacion` VARCHAR(45) NULL,
  `numeroIdentificacion` VARCHAR(45) NULL,
  `celular` VARCHAR(45) NULL,

  `parentesco` VARCHAR(45) NULL,

  `correo` VARCHAR(45) NULL ;


  `is_active` TINYINT(1) default 1,
  `fecha_creado` DATE,
  `creado_por_usuario` VARCHAR(45),
  `creado_id_usuario` int,
  `fecha_modificado` DATE,
  `modificado_por_usuario` VARCHAR(45),
  `modificado_id_usuario` int,
  
  PRIMARY KEY (`idDependiente`));


-- -----------------------------------------------------
-- Table `ClienteDependiente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ClienteDependiente` (
  `idClienteDependiente` INT NOT NULL AUTO_INCREMENT,
  `idCliente` INT NOT NULL,
  `idDependiente` INT NOT NULL,
  `parentescoConTitular` VARCHAR(45) NULL,
    
  `is_active` TINYINT(1) default 1,
  `fecha_creado` DATE,
  `creado_por_usuario` VARCHAR(45),
  `creado_id_usuario` int,
  `fecha_modificado` DATE,
  `modificado_por_usuario` VARCHAR(45),
  `modificado_id_usuario` int,
  
  PRIMARY KEY (`idClienteDependiente`),  
    FOREIGN KEY (`idCliente`)
    REFERENCES `Cliente` (`idCliente`),
  
    FOREIGN KEY (`idDependiente`)
    REFERENCES `Dependiente` (`idDependiente`));


-- -----------------------------------------------------
-- Table `DocumentoDependiente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DocumentoDependiente` (
  `idDocumento` INT NOT NULL AUTO_INCREMENT,
  `idDependiente` INT NOT NULL,
  `urlArchivo` VARCHAR(45) NULL,
  `tipoDocumento` VARCHAR(45) NULL,
  `descripcionDocumento` VARCHAR(255) NULL,
    
  `is_active` TINYINT(1) default 1,
  `fecha_creado` DATE,
  `creado_por_usuario` VARCHAR(45),
  `creado_id_usuario` int,
  `fecha_modificado` DATE,
  `modificado_por_usuario` VARCHAR(45),
  `modificado_id_usuario` int,
  
  PRIMARY KEY (`idDocumento`),  
    FOREIGN KEY (`idDependiente`)
    REFERENCES `Dependiente` (`idDependiente`));


-- -----------------------------------------------------
-- Table `Compania`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Compania` (
  `idCompania` INT NOT NULL AUTO_INCREMENT,
  `nombreCompania` VARCHAR(45) NULL,
  `ruc` VARCHAR(45) ,
  `nombreCoordinador` VARCHAR(45) NULL,
  `celular` VARCHAR(45) NULL,
  `correo` VARCHAR(45) NULL,
    
  `is_active` TINYINT(1) default 1,
  `fecha_creado` DATE,
  `creado_por_usuario` VARCHAR(45),
  `creado_id_usuario` int,
  `fecha_modificado` DATE,
  `modificado_por_usuario` VARCHAR(45),
  `modificado_id_usuario` int,
  
  PRIMARY KEY (`idCompania`));


-- -----------------------------------------------------
-- Table `Plan`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Plan` (
  `idPlan` INT NOT NULL AUTO_INCREMENT,
  `idCompania` INT NULL,
  `tipoDePlan` VARCHAR(45) NULL,
  `tipoDeSeguro` VARCHAR(45) NULL,
  `nombrePlan` VARCHAR(45) NULL,
  `tieneLimite` TINYINT(1) NULL,
  `cobertura` FLOAT NULL,
    
  `is_active` TINYINT(1) default 1,
  `fecha_creado` DATE,
  `creado_por_usuario` VARCHAR(45),
  `creado_id_usuario` int,
  `fecha_modificado` DATE,
  `modificado_por_usuario` VARCHAR(45),
  `modificado_id_usuario` int,
  
  PRIMARY KEY (`idPlan`),  
    FOREIGN KEY (`idCompania`)
    REFERENCES `Compania` (`idCompania`));


-- -----------------------------------------------------
-- Table `Deducible`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Deducible` (
  `idDeducible` INT NOT NULL AUTO_INCREMENT,
  `idPlan` INT NOT NULL,
  `tipoDeducible` VARCHAR(45) NULL,
  `valor` FLOAT NULL,
    
  `is_active` TINYINT(1) default 1,
  `fecha_creado` DATE,
  `creado_por_usuario` VARCHAR(45),
  `creado_id_usuario` int,
  `fecha_modificado` DATE,
  `modificado_por_usuario` VARCHAR(45),
  `modificado_id_usuario` int,
  
  PRIMARY KEY (`idDeducible`),  
    FOREIGN KEY (`idPlan`)
    REFERENCES `Plan` (`idPlan`));


-- -----------------------------------------------------
-- Table `Contrato`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Contrato` (
  `idContrato` INT NOT NULL AUTO_INCREMENT,
  `idCliente` INT NOT NULL,
  `idPlan` INT NULL,
  `idAgenteAsignado` INT NULL,
  `primaAnioActual` FLOAT NULL,
  `modalidadPrma` VARCHAR(45) NULL,
  `valorCuotaPrima` FLOAT NULL,
  `primaAnioSiguiente` FLOAT NULL,
  `aumentoPrima` FLOAT NULL,
  `porcentajeAumento` FLOAT NULL,
  `estadoFirmaContrato` TINYINT(1) NULL,
  `diaDeFirma` DATE NULL,
  `firmado` DATE NULL,
  `fechaIngreso` DATE NULL,
  `fechaVigencia` DATE NULL,
  `fechaPagoPrimerCuota` DATE NULL,
  `observaciones` VARCHAR(255) NULL,
  `comisionAgente` FLOAT NULL,
  `porcentajeComision` FLOAT NULL,
  `Contratocol` VARCHAR(45) NULL,
  `idCotizacion` INT NULL,
  `sumaAsegurada` FLOAT NULL,
  `endoso` TINYINT(1) NULL,
  `placa` VARCHAR(45) NULL,
  `modelo` VARCHAR(45) NULL,
  `marca` VARCHAR(45) NULL,
  `anioModelo` DATE NULL,
  `pasajeros` INT NULL,
    
  `is_active` TINYINT(1) default 1,
  `fecha_creado` DATE,
  `creado_por_usuario` VARCHAR(45),
  `creado_id_usuario` int,
  `fecha_modificado` DATE,
  `modificado_por_usuario` VARCHAR(45),
  `modificado_id_usuario` int,
  
  PRIMARY KEY (`idContrato`),  
    FOREIGN KEY (`idCliente`)
    REFERENCES `Cliente` (`idCliente`),
    FOREIGN KEY (`idPlan`)
    REFERENCES `Plan` (`idPlan`),
    FOREIGN KEY (`idAgenteAsignado`)
    REFERENCES `Empleado` (`idEmpleado`));


-- -----------------------------------------------------
-- Table `DocumentoContrato`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DocumentoContrato` (
  `idDocumento` INT NOT NULL AUTO_INCREMENT,
  `idContrato` INT NOT NULL,
  `urlArchivo` VARCHAR(45) NULL,
  `tipoDocumento` VARCHAR(45) NULL,
  `descripcionDocumento` VARCHAR(255) NULL,
    
  `is_active` TINYINT(1) default 1,
  `fecha_creado` DATE,
  `creado_por_usuario` VARCHAR(45),
  `creado_id_usuario` int,
  `fecha_modificado` DATE,
  `modificado_por_usuario` VARCHAR(45),
  `modificado_id_usuario` int,
  
  PRIMARY KEY (`idDocumento`),
    FOREIGN KEY (`idContrato`)
    REFERENCES `Contrato` (`idContrato`)
);

ALTER TABLE Persona
ADD idUsuario int;

ALTER TABLE Persona
ADD FOREIGN KEY (idUsuario) REFERENCES Usuario (idUsuario);


ALTER TABLE Cliente
ADD  `agenteAsignado` int NULL;

ALTER TABLE Cliente
ADD FOREIGN KEY (agenteAsignado) REFERENCES Empleado(idEmpleado);

ALTER TABLE Dependiente
ADD  `idCliente` int NULL;

ALTER TABLE Dependiente
ADD FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente);
