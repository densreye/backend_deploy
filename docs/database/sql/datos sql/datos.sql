/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE DATABASE IF NOT EXISTS `broker` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `broker`;

CREATE TABLE IF NOT EXISTS `cargo` (
  `idCargo` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idCargo`)
) ENGINE=InnoDB AUTO_INCREMENT=304 DEFAULT CHARSET=utf8mb4;

DELETE FROM `cargo`;
INSERT INTO `cargo` (`idCargo`, `descripcion`) VALUES
	(301, 'supervisor área de ventas'),
	(302, 'agente área de ventas'),
	(303, 'marketing área de ventas');

CREATE TABLE IF NOT EXISTS `cliente` (
  `idCliente` int(11) NOT NULL AUTO_INCREMENT,
  `idPersona` int(11) NOT NULL,
  `idReferido` int(11) DEFAULT NULL,
  `idDatosCliente` int(11) DEFAULT NULL,
  `idDatosFacturacion` int(11) DEFAULT NULL,
  `idDatosFinancieros` int(11) DEFAULT NULL,
  `idDatosPreexistencia` int(11) DEFAULT NULL,
  `idSolicitud` tinyint(1) DEFAULT NULL,
  `contacto` int(11) DEFAULT NULL,
  `talla` varchar(45) DEFAULT NULL,
  `peso` float DEFAULT NULL,
  `esBeneficiario` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`idCliente`),
  KEY `idReferido` (`idReferido`),
  KEY `idPersona` (`idPersona`),
  CONSTRAINT `cliente_ibfk_1` FOREIGN KEY (`idReferido`) REFERENCES `referido` (`idReferido`),
  CONSTRAINT `cliente_ibfk_2` FOREIGN KEY (`idPersona`) REFERENCES `persona` (`idPersona`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DELETE FROM `cliente`;

CREATE TABLE IF NOT EXISTS `clientedependiente` (
  `idClienteDependiente` int(11) NOT NULL AUTO_INCREMENT,
  `idCliente` int(11) NOT NULL,
  `idDependiente` int(11) NOT NULL,
  `parentescoConTitular` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idClienteDependiente`),
  KEY `idCliente` (`idCliente`),
  KEY `idDependiente` (`idDependiente`),
  CONSTRAINT `clientedependiente_ibfk_1` FOREIGN KEY (`idCliente`) REFERENCES `cliente` (`idCliente`),
  CONSTRAINT `clientedependiente_ibfk_2` FOREIGN KEY (`idDependiente`) REFERENCES `dependiente` (`idDependiente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DELETE FROM `clientedependiente`;

CREATE TABLE IF NOT EXISTS `compania` (
  `idCompania` int(11) NOT NULL AUTO_INCREMENT,
  `nombreCompania` varchar(45) DEFAULT NULL,
  `ruc` varchar(45) DEFAULT NULL,
  `nombreCoordinador` varchar(45) DEFAULT NULL,
  `celular` varchar(45) DEFAULT NULL,
  `correo` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idCompania`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DELETE FROM `compania`;

CREATE TABLE IF NOT EXISTS `contactoprospecto` (
  `idContactoProspecto` int(11) NOT NULL AUTO_INCREMENT,
  `contenido` varchar(255) DEFAULT NULL,
  `tipo` int(11) DEFAULT NULL,
  `idProspecto` int(11) DEFAULT NULL,
  PRIMARY KEY (`idContactoProspecto`),
  KEY `FK_contactoprospecto_prospecto` (`idProspecto`),
  CONSTRAINT `FK_contactoprospecto_prospecto` FOREIGN KEY (`idProspecto`) REFERENCES `prospecto` (`idProspecto`) ON DELETE SET NULL ON UPDATE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DELETE FROM `contactoprospecto`;

CREATE TABLE IF NOT EXISTS `contrato` (
  `idContrato` int(11) NOT NULL AUTO_INCREMENT,
  `idCliente` int(11) NOT NULL,
  `idPlan` int(11) DEFAULT NULL,
  `idAgenteAsignado` int(11) DEFAULT NULL,
  `primaAnioActual` float DEFAULT NULL,
  `modalidadPrma` varchar(45) DEFAULT NULL,
  `valorCuotaPrima` float DEFAULT NULL,
  `primaAnioSiguiente` float DEFAULT NULL,
  `aumentoPrima` float DEFAULT NULL,
  `porcentajeAumento` float DEFAULT NULL,
  `estadoFirmaContrato` tinyint(1) DEFAULT NULL,
  `diaDeFirma` date DEFAULT NULL,
  `firmado` date DEFAULT NULL,
  `fechaIngreso` date DEFAULT NULL,
  `fechaVigencia` date DEFAULT NULL,
  `fechaPagoPrimerCuota` date DEFAULT NULL,
  `observaciones` varchar(255) DEFAULT NULL,
  `comisionAgente` float DEFAULT NULL,
  `porcentajeComision` float DEFAULT NULL,
  `Contratocol` varchar(45) DEFAULT NULL,
  `idCotizacion` int(11) DEFAULT NULL,
  `sumaAsegurada` float DEFAULT NULL,
  `endoso` tinyint(1) DEFAULT NULL,
  `placa` varchar(45) DEFAULT NULL,
  `modelo` varchar(45) DEFAULT NULL,
  `marca` varchar(45) DEFAULT NULL,
  `anioModelo` date DEFAULT NULL,
  `pasajeros` int(11) DEFAULT NULL,
  PRIMARY KEY (`idContrato`),
  KEY `idCliente` (`idCliente`),
  KEY `idPlan` (`idPlan`),
  KEY `idAgenteAsignado` (`idAgenteAsignado`),
  CONSTRAINT `contrato_ibfk_1` FOREIGN KEY (`idCliente`) REFERENCES `cliente` (`idCliente`),
  CONSTRAINT `contrato_ibfk_2` FOREIGN KEY (`idPlan`) REFERENCES `plan` (`idPlan`),
  CONSTRAINT `contrato_ibfk_3` FOREIGN KEY (`idAgenteAsignado`) REFERENCES `empleado` (`idEmpleado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DELETE FROM `contrato`;

CREATE TABLE IF NOT EXISTS `cotizacion` (
  `idCotizacion` int(11) NOT NULL AUTO_INCREMENT,
  `idProspecto` int(11) DEFAULT NULL,
  `idPlan` int(11) NOT NULL,
  `Estado` int(11) DEFAULT NULL,
  `Modificado` datetime NOT NULL DEFAULT current_timestamp(),
  `Creado` datetime NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`idCotizacion`) USING BTREE,
  KEY `FK_cotizacion_prospecto` (`idProspecto`),
  KEY `FK_cotizacion_plan` (`idPlan`),
  CONSTRAINT `FK_cotizacion_plan` FOREIGN KEY (`idPlan`) REFERENCES `plan` (`idPlan`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_cotizacion_prospecto` FOREIGN KEY (`idProspecto`) REFERENCES `prospecto` (`idProspecto`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

DELETE FROM `cotizacion`;

CREATE TABLE IF NOT EXISTS `deducible` (
  `idDeducible` int(11) NOT NULL AUTO_INCREMENT,
  `idPlan` int(11) NOT NULL,
  `tipoDeducible` varchar(45) DEFAULT NULL,
  `valor` float DEFAULT NULL,
  PRIMARY KEY (`idDeducible`),
  KEY `idPlan` (`idPlan`),
  CONSTRAINT `deducible_ibfk_1` FOREIGN KEY (`idPlan`) REFERENCES `plan` (`idPlan`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DELETE FROM `deducible`;

CREATE TABLE IF NOT EXISTS `dependiente` (
  `idDependiente` int(11) NOT NULL AUTO_INCREMENT,
  `talla` varchar(45) DEFAULT NULL,
  `peso` float DEFAULT NULL,
  `nombres` varchar(45) DEFAULT NULL,
  `apellidos` varchar(45) DEFAULT NULL,
  `tipoDeIdentificacion` varchar(45) DEFAULT NULL,
  `numeroIdentificacion` varchar(45) DEFAULT NULL,
  `celular` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idDependiente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DELETE FROM `dependiente`;

CREATE TABLE IF NOT EXISTS `direccion` (
  `idDireccion` int(11) NOT NULL AUTO_INCREMENT,
  `idPersona` int(11) DEFAULT NULL,
  `tipoDireccion` varchar(45) DEFAULT NULL,
  `pais` varchar(45) DEFAULT NULL,
  `provincia` varchar(45) DEFAULT NULL,
  `ciudad` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idDireccion`),
  KEY `idPersona` (`idPersona`),
  CONSTRAINT `direccion_ibfk_1` FOREIGN KEY (`idPersona`) REFERENCES `persona` (`idPersona`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DELETE FROM `direccion`;

CREATE TABLE IF NOT EXISTS `documentocontrato` (
  `idDocumento` int(11) NOT NULL AUTO_INCREMENT,
  `idContrato` int(11) NOT NULL,
  `urlArchivo` varchar(45) DEFAULT NULL,
  `tipoDocumento` varchar(45) DEFAULT NULL,
  `descripcionDocumento` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idDocumento`),
  KEY `idContrato` (`idContrato`),
  CONSTRAINT `documentocontrato_ibfk_1` FOREIGN KEY (`idContrato`) REFERENCES `contrato` (`idContrato`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DELETE FROM `documentocontrato`;

CREATE TABLE IF NOT EXISTS `documentodependiente` (
  `idDocumento` int(11) NOT NULL AUTO_INCREMENT,
  `idDependiente` int(11) NOT NULL,
  `urlArchivo` varchar(45) DEFAULT NULL,
  `tipoDocumento` varchar(45) DEFAULT NULL,
  `descripcionDocumento` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idDocumento`),
  KEY `idDependiente` (`idDependiente`),
  CONSTRAINT `documentodependiente_ibfk_1` FOREIGN KEY (`idDependiente`) REFERENCES `dependiente` (`idDependiente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DELETE FROM `documentodependiente`;

CREATE TABLE IF NOT EXISTS `documentoempleado` (
  `idDocumento` int(11) NOT NULL AUTO_INCREMENT,
  `idEmpleado` int(11) NOT NULL,
  `urlArchivo` varchar(45) DEFAULT NULL,
  `tipoDocumento` varchar(45) DEFAULT NULL,
  `descripcionDocumento` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idDocumento`),
  KEY `idEmpleado` (`idEmpleado`),
  CONSTRAINT `documentoempleado_ibfk_1` FOREIGN KEY (`idEmpleado`) REFERENCES `empleado` (`idEmpleado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DELETE FROM `documentoempleado`;

CREATE TABLE IF NOT EXISTS `empleado` (
  `idEmpleado` int(11) NOT NULL AUTO_INCREMENT,
  `idPersona` int(11) NOT NULL,
  `fechaIngresoNoboa` date DEFAULT NULL,
  `idCargo` int(11) DEFAULT NULL,
  PRIMARY KEY (`idEmpleado`),
  KEY `idPersona` (`idPersona`),
  KEY `idCargo` (`idCargo`),
  CONSTRAINT `empleado_ibfk_1` FOREIGN KEY (`idPersona`) REFERENCES `persona` (`idPersona`),
  CONSTRAINT `empleado_ibfk_2` FOREIGN KEY (`idCargo`) REFERENCES `cargo` (`idCargo`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

DELETE FROM `empleado`;
INSERT INTO `empleado` (`idEmpleado`, `idPersona`, `fechaIngresoNoboa`, `idCargo`) VALUES
	(1, 1, NULL, 301),
	(2, 2, NULL, 301),
	(3, 3, NULL, 302),
	(4, 4, NULL, 302),
	(5, 5, NULL, 302),
	(6, 6, NULL, 302);

CREATE TABLE IF NOT EXISTS `notificacionventas` (
  `idNotificacion` int(11) NOT NULL AUTO_INCREMENT,
  `idSupervisor` int(11) DEFAULT NULL,
  `titulo` varchar(255) DEFAULT NULL,
  `tipo` int(11) DEFAULT NULL,
  `contenido` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`contenido`)),
  `creado` datetime NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`idNotificacion`),
  KEY `FK_notificacionventas_empleado` (`idSupervisor`),
  CONSTRAINT `FK_notificacionventas_empleado` FOREIGN KEY (`idSupervisor`) REFERENCES `empleado` (`idEmpleado`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DELETE FROM `notificacionventas`;

CREATE TABLE IF NOT EXISTS `notificacionventasremitentes` (
  `idNotificacion` int(11) NOT NULL,
  `idAgente` int(11) NOT NULL,
  `visto` tinyint(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`idNotificacion`,`idAgente`),
  KEY `FK_notificacionventasremitentes_empleado` (`idAgente`),
  CONSTRAINT `FK_notificacionventasremitentes_empleado` FOREIGN KEY (`idAgente`) REFERENCES `empleado` (`idEmpleado`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_notificacionventasremitentes_notificacionventas` FOREIGN KEY (`idNotificacion`) REFERENCES `notificacionventas` (`idNotificacion`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DELETE FROM `notificacionventasremitentes`;

CREATE TABLE IF NOT EXISTS `persona` (
  `idPersona` int(11) NOT NULL AUTO_INCREMENT,
  `idUsuario` int(11) NOT NULL DEFAULT 0,
  `nombre` varchar(45) DEFAULT NULL,
  `apellido` varchar(45) DEFAULT NULL,
  `tipoDeIdentificacion` varchar(45) DEFAULT NULL,
  `numeroIdentificacion` varchar(45) DEFAULT NULL,
  `fechaNacimiento` date DEFAULT NULL,
  `edad` int(11) DEFAULT NULL,
  `sexo` varchar(45) DEFAULT NULL,
  `estadCivil` varchar(45) DEFAULT NULL,
  `tipoPersona` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idPersona`),
  KEY `FK_persona_usuario` (`idUsuario`),
  CONSTRAINT `FK_persona_usuario` FOREIGN KEY (`idUsuario`) REFERENCES `usuario` (`idUsuario`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

DELETE FROM `persona`;
INSERT INTO `persona` (`idPersona`, `idUsuario`, `nombre`, `apellido`, `tipoDeIdentificacion`, `numeroIdentificacion`, `fechaNacimiento`, `edad`, `sexo`, `estadCivil`, `tipoPersona`) VALUES
	(1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(2, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(3, 3, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(4, 4, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(5, 5, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(6, 6, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

CREATE TABLE IF NOT EXISTS `plan` (
  `idPlan` int(11) NOT NULL AUTO_INCREMENT,
  `idCompania` int(11) DEFAULT NULL,
  `tipoDePlan` varchar(45) DEFAULT NULL,
  `tipoDeSeguro` varchar(45) DEFAULT NULL,
  `nombrePlan` varchar(45) DEFAULT NULL,
  `tieneLimite` tinyint(1) DEFAULT NULL,
  `cobertura` float DEFAULT NULL,
  PRIMARY KEY (`idPlan`),
  KEY `idCompania` (`idCompania`),
  CONSTRAINT `plan_ibfk_1` FOREIGN KEY (`idCompania`) REFERENCES `compania` (`idCompania`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DELETE FROM `plan`;

CREATE TABLE IF NOT EXISTS `prospecto` (
  `idProspecto` int(11) NOT NULL AUTO_INCREMENT,
  `idAgente` int(11) DEFAULT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `apellido` varchar(45) DEFAULT NULL,
  `genero` varchar(45) DEFAULT NULL,
  `edad` varchar(45) DEFAULT NULL,
  `categoria` int(11) DEFAULT NULL,
  `direccion` varchar(45) DEFAULT NULL,
  `proyectadoActual` int(11) DEFAULT NULL,
  `urlArchivo` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idProspecto`),
  KEY `FK_prospecto_empleado` (`idAgente`),
  CONSTRAINT `FK_prospecto_empleado` FOREIGN KEY (`idAgente`) REFERENCES `empleado` (`idEmpleado`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4;

DELETE FROM `prospecto`;
INSERT INTO `prospecto` (`idProspecto`, `idAgente`, `nombre`, `apellido`, `genero`, `edad`, `categoria`, `direccion`, `proyectadoActual`, `urlArchivo`) VALUES
	(7, 3, 'Jose Maria', 'Ramiréz Ferandez', 'M', '25', 1, 'Guayas - Guayaquil - Urdesa Central', 25000, NULL),
	(8, 3, 'Maria Jose', 'Ramirez Ferandez', 'F', '23', 2, 'Guayas - Guayaquil - 9 de Octubre y Pichincha', NULL, NULL),
	(9, 3, 'Andres', 'Caballero', 'M', '34', 1, 'Boulevard 9 de Octubre y Pichincha', 4000, NULL),
	(10, 3, 'Agente Bodegas Cookie', NULL, 'No Aplica', NULL, 2, NULL, NULL, NULL),
	(11, 4, 'Cristhian', 'Olvera Espinoza', 'M', '19', 3, 'Guayas - Duran - El Recreo', NULL, NULL),
	(12, 4, 'Hanna', 'Barbera', 'F', '80', 1, NULL, NULL, NULL),
	(13, NULL, 'Jose', 'Andrea', 'M', '25', 1, NULL, NULL, NULL);

CREATE TABLE IF NOT EXISTS `prospectosesion` (
  `idProspectoSesion` int(11) NOT NULL AUTO_INCREMENT,
  `idProspecto` int(11) DEFAULT NULL,
  `inicio` datetime DEFAULT current_timestamp(),
  `fin` datetime DEFAULT NULL,
  `estado` int(11) DEFAULT NULL,
  `tipo` int(11) DEFAULT NULL,
  `detalle` text DEFAULT NULL,
  PRIMARY KEY (`idProspectoSesion`),
  KEY `FK_prospectosesion_prospecto` (`idProspecto`),
  CONSTRAINT `FK_prospectosesion_prospecto` FOREIGN KEY (`idProspecto`) REFERENCES `prospecto` (`idProspecto`) ON DELETE SET NULL ON UPDATE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

DELETE FROM `prospectosesion`;
INSERT INTO `prospectosesion` (`idProspectoSesion`, `idProspecto`, `inicio`, `fin`, `estado`, `tipo`, `detalle`) VALUES
	(4, 7, '2022-09-01 21:14:41', NULL, 0, 1, 'La persona deseaba información de un plan medico, aparentemente sugerido por un conocido. Esta interesado pero es la primera vez que contrata un seguro y pidió que lo llamaran mañana para mas información'),
	(5, 8, '2022-09-01 21:21:02', NULL, 0, 1, 'Es hermana de otro prospecto, y llego como compañía, pidió información pero no desea contratar un producto por el momento; aún así nos otorgo un numero de teléfono'),
	(6, 7, '2022-09-02 12:17:51', NULL, 1, 1, 'El cliente accedió a reunirse para cotizar un producto, ofrece traer documentos para una consulta mas personalizada');

CREATE TABLE IF NOT EXISTS `referido` (
  `idReferido` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `celular` varchar(45) DEFAULT NULL,
  `correo` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idReferido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DELETE FROM `referido`;

CREATE TABLE IF NOT EXISTS `usuario` (
  `idUsuario` int(11) NOT NULL AUTO_INCREMENT,
  `nombreUsuario` varchar(45) NOT NULL,
  `claveUsuario` varchar(45) NOT NULL,
  `token` varchar(45) DEFAULT NULL,
  `fotoUsuario` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idUsuario`),
  UNIQUE KEY `nombreUsuario` (`nombreUsuario`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

DELETE FROM `usuario`;
INSERT INTO `usuario` (`idUsuario`, `nombreUsuario`, `claveUsuario`, `token`, `fotoUsuario`) VALUES
	(1, 'supervisor', 'pbkdf2_sha256$390000$b0BQSoTx09xI6lrsiTWjhc$c', NULL, NULL),
	(2, 'supervisor2', 'pbkdf2_sha256$390000$nYlAAp6JCOGhDjM953tBY8$X', NULL, NULL),
	(3, 'agente1', 'pbkdf2_sha256$390000$NeQ3GvF3JB4cXZhfGJ53Cs$o', NULL, NULL),
	(4, 'agente2', 'pbkdf2_sha256$390000$xt5ZLxitSE5SHU5rAZCtBv$L', NULL, NULL),
	(5, 'agente3', 'pbkdf2_sha256$390000$3q9WmdN8LLfnbF6eQx1aZZ$5', NULL, NULL),
	(6, 'agente4', 'pbkdf2_sha256$390000$qTxU7GouHErWlEVFoI9369$I', NULL, NULL);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
