-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.24-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.0.0.6468
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para broker
CREATE DATABASE IF NOT EXISTS `broker` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `broker`;

-- Volcando estructura para tabla broker.authtoken_token
CREATE TABLE IF NOT EXISTS `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla broker.auth_group
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla broker.auth_group_permissions
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla broker.auth_permission
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=301 DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla broker.auth_user
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla broker.auth_user_groups
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla broker.auth_user_user_permissions
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla broker.cargo
CREATE TABLE IF NOT EXISTS `cargo` (
  `idCargo` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(255) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT 1,
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`idCargo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla broker.cliente
CREATE TABLE IF NOT EXISTS `cliente` (
  `idCliente` int(11) NOT NULL AUTO_INCREMENT,
  `idPersona` int(11) NOT NULL,
  `idReferido` int(11) DEFAULT NULL,
  
  `idDatosFacturacion` int(11) DEFAULT NULL,
  `idDatosFinancieros` int(11) DEFAULT NULL,
  `idDatosPreexistencia` int(11) DEFAULT NULL,
  `idSolicitud` tinyint(1) DEFAULT NULL,
  `contacto` int(11) DEFAULT NULL,
  `talla` varchar(45) DEFAULT NULL,
  `peso` float DEFAULT NULL,
  `esBeneficiario` tinyint(1) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT 1,
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`idCliente`),
  KEY `idReferido` (`idReferido`),
  KEY `idPersona` (`idPersona`),
  CONSTRAINT `cliente_ibfk_1` FOREIGN KEY (`idReferido`) REFERENCES `referido` (`idReferido`),
  CONSTRAINT `cliente_ibfk_2` FOREIGN KEY (`idPersona`) REFERENCES `persona` (`idPersona`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla broker.clientedependiente
CREATE TABLE IF NOT EXISTS `clientedependiente` (
  `idClienteDependiente` int(11) NOT NULL AUTO_INCREMENT,
  `idCliente` int(11) NOT NULL,
  `idDependiente` int(11) NOT NULL,
  `parentescoConTitular` varchar(45) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT 1,
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`idClienteDependiente`),
  KEY `idCliente` (`idCliente`),
  KEY `idDependiente` (`idDependiente`),
  CONSTRAINT `clientedependiente_ibfk_1` FOREIGN KEY (`idCliente`) REFERENCES `cliente` (`idCliente`),
  CONSTRAINT `clientedependiente_ibfk_2` FOREIGN KEY (`idDependiente`) REFERENCES `dependiente` (`idDependiente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla broker.compania
CREATE TABLE IF NOT EXISTS `compania` (
  `idCompania` int(11) NOT NULL AUTO_INCREMENT,
  `nombreCompania` varchar(45) DEFAULT NULL,
  `ruc` varchar(45) DEFAULT NULL,
  `nombreCoordinador` varchar(45) DEFAULT NULL,
  `celular` varchar(45) DEFAULT NULL,
  `correo` varchar(45) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT 1,
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`idCompania`),
  UNIQUE KEY `ruc` (`ruc`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla broker.contrato
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
  `is_active` tinyint(1) DEFAULT 1,
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`idContrato`),
  KEY `idCliente` (`idCliente`),
  KEY `idPlan` (`idPlan`),
  KEY `idAgenteAsignado` (`idAgenteAsignado`),
  CONSTRAINT `contrato_ibfk_1` FOREIGN KEY (`idCliente`) REFERENCES `cliente` (`idCliente`),
  CONSTRAINT `contrato_ibfk_2` FOREIGN KEY (`idPlan`) REFERENCES `plan` (`idPlan`),
  CONSTRAINT `contrato_ibfk_3` FOREIGN KEY (`idAgenteAsignado`) REFERENCES `empleado` (`idEmpleado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla broker.deducible
CREATE TABLE IF NOT EXISTS `deducible` (
  `idDeducible` int(11) NOT NULL AUTO_INCREMENT,
  `idPlan` int(11) NOT NULL,
  `tipoDeducible` varchar(45) DEFAULT NULL,
  `valor` float DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT 1,
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`idDeducible`),
  KEY `idPlan` (`idPlan`),
  CONSTRAINT `deducible_ibfk_1` FOREIGN KEY (`idPlan`) REFERENCES `plan` (`idPlan`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla broker.dependiente
CREATE TABLE IF NOT EXISTS `dependiente` (
  `idDependiente` int(11) NOT NULL AUTO_INCREMENT,
  `talla` varchar(45) DEFAULT NULL,
  `peso` float DEFAULT NULL,
  `nombres` varchar(45) DEFAULT NULL,
  `apellidos` varchar(45) DEFAULT NULL,
  `tipoDeIdentificacion` varchar(45) DEFAULT NULL,
  `numeroIdentificacion` varchar(45) DEFAULT NULL,
  `celular` varchar(45) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT 1,
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`idDependiente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla broker.direccion
CREATE TABLE IF NOT EXISTS `direccion` (
  `idDireccion` int(11) NOT NULL AUTO_INCREMENT,
  `idPersona` int(11) DEFAULT NULL,
  `tipoDireccion` varchar(45) DEFAULT NULL,
  `pais` varchar(45) DEFAULT NULL,
  `provincia` varchar(45) DEFAULT NULL,
  `ciudad` varchar(45) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT 1,
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`idDireccion`),
  KEY `idPersona` (`idPersona`),
  CONSTRAINT `direccion_ibfk_1` FOREIGN KEY (`idPersona`) REFERENCES `persona` (`idPersona`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla broker.django_admin_log
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla broker.django_content_type
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla broker.django_migrations
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla broker.django_session
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla broker.documentocontrato
CREATE TABLE IF NOT EXISTS `documentocontrato` (
  `idDocumento` int(11) NOT NULL AUTO_INCREMENT,
  `idContrato` int(11) NOT NULL,
  `urlArchivo` varchar(45) DEFAULT NULL,
  `tipoDocumento` varchar(45) DEFAULT NULL,
  `descripcionDocumento` varchar(255) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT 1,
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`idDocumento`),
  KEY `idContrato` (`idContrato`),
  CONSTRAINT `documentocontrato_ibfk_1` FOREIGN KEY (`idContrato`) REFERENCES `contrato` (`idContrato`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla broker.documentodependiente
CREATE TABLE IF NOT EXISTS `documentodependiente` (
  `idDocumento` int(11) NOT NULL AUTO_INCREMENT,
  `idDependiente` int(11) NOT NULL,
  `urlArchivo` varchar(45) DEFAULT NULL,
  `tipoDocumento` varchar(45) DEFAULT NULL,
  `descripcionDocumento` varchar(255) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT 1,
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`idDocumento`),
  KEY `idDependiente` (`idDependiente`),
  CONSTRAINT `documentodependiente_ibfk_1` FOREIGN KEY (`idDependiente`) REFERENCES `dependiente` (`idDependiente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla broker.documentoempleado
CREATE TABLE IF NOT EXISTS `documentoempleado` (
  `idDocumento` int(11) NOT NULL AUTO_INCREMENT,
  `idEmpleado` int(11) NOT NULL,
  `urlArchivo` varchar(45) DEFAULT NULL,
  `tipoDocumento` varchar(45) DEFAULT NULL,
  `descripcionDocumento` varchar(255) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT 1,
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`idDocumento`),
  KEY `idEmpleado` (`idEmpleado`),
  CONSTRAINT `documentoempleado_ibfk_1` FOREIGN KEY (`idEmpleado`) REFERENCES `empleado` (`idEmpleado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla broker.empleado
CREATE TABLE IF NOT EXISTS `empleado` (
  `idEmpleado` int(11) NOT NULL AUTO_INCREMENT,
  `idPersona` int(11) NOT NULL,
  `fechaIngresoNoboa` date DEFAULT NULL,
  `idCargo` int(11) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT 1,
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`idEmpleado`),
  KEY `idPersona` (`idPersona`),
  KEY `idCargo` (`idCargo`),
  CONSTRAINT `empleado_ibfk_1` FOREIGN KEY (`idPersona`) REFERENCES `persona` (`idPersona`),
  CONSTRAINT `empleado_ibfk_2` FOREIGN KEY (`idCargo`) REFERENCES `cargo` (`idCargo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla broker.persona
CREATE TABLE IF NOT EXISTS `persona` (
  `idPersona` int(11) NOT NULL AUTO_INCREMENT,
  `idUsuario` int(11) DEFAULT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `apellido` varchar(45) DEFAULT NULL,
  `tipoDeIdentificacion` varchar(45) DEFAULT NULL,
  `numeroIdentificacion` varchar(45) DEFAULT NULL,
  `fechaNacimiento` date DEFAULT NULL,
  `edad` int(11) DEFAULT NULL,
  `sexo` varchar(45) DEFAULT NULL,
  `estadCivil` varchar(45) DEFAULT NULL,
  `tipoPersona` varchar(45) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT 1,
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`idPersona`),
  KEY `FK_persona_usuario` (`idUsuario`),
  CONSTRAINT `FK_persona_usuario` FOREIGN KEY (`idUsuario`) REFERENCES `usuario` (`idUsuario`) ON DELETE SET NULL ON UPDATE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla broker.plan
CREATE TABLE IF NOT EXISTS `plan` (
  `idPlan` int(11) NOT NULL AUTO_INCREMENT,
  `idCompania` int(11) DEFAULT NULL,
  `tipoDePlan` varchar(45) DEFAULT NULL,
  `tipoDeSeguro` varchar(45) DEFAULT NULL,
  `nombrePlan` varchar(45) DEFAULT NULL,
  `tieneLimite` tinyint(1) DEFAULT NULL,
  `cobertura` float DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT 1,
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`idPlan`),
  KEY `idCompania` (`idCompania`),
  CONSTRAINT `plan_ibfk_1` FOREIGN KEY (`idCompania`) REFERENCES `compania` (`idCompania`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla broker.referido
CREATE TABLE IF NOT EXISTS `referido` (
  `idReferido` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `celular` varchar(45) DEFAULT NULL,
  `correo` varchar(45) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT 1,
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`idReferido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla broker.usuario
CREATE TABLE IF NOT EXISTS `usuario` (
  `idUsuario` int(11) NOT NULL AUTO_INCREMENT,
  `nombreUsuario` varchar(45) DEFAULT NULL,
  `claveUsuario` varchar(45) NOT NULL,
  `token` varchar(45) DEFAULT NULL,
  `fotoUsuario` varchar(45) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT 1,
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`idUsuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
