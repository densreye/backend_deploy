-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: MedicalBrokers.mysql.pythonanywhere-services.com    Database: MedicalBrokers$brokers
-- ------------------------------------------------------
-- Server version	5.7.34-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `MedicalBrokers$brokers`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `MedicalBrokers$brokers` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `MedicalBrokers$brokers`;

--
-- Table structure for table `Cargo`
--

DROP TABLE IF EXISTS `Cargo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Cargo` (
  `idCargo` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(255) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT '1',
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`idCargo`)
) ENGINE=InnoDB AUTO_INCREMENT=304 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cargo`
--

LOCK TABLES `Cargo` WRITE;
/*!40000 ALTER TABLE `Cargo` DISABLE KEYS */;
INSERT INTO `Cargo` VALUES (1,'Agente',1,'2022-09-29',NULL,NULL,NULL,NULL,NULL),(301,'supervisor área de ventas',1,NULL,NULL,NULL,NULL,NULL,NULL),(302,'agente área de ventas',1,NULL,NULL,NULL,NULL,NULL,NULL),(303,'marketing área de ventas',1,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `Cargo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Cliente`
--

DROP TABLE IF EXISTS `Cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Cliente` (
  `idCliente` int(11) NOT NULL AUTO_INCREMENT,
  `idPersona` int(11) NOT NULL,
  `idDatosFacturacion` int(11) DEFAULT NULL,
  `idDatosFinancieros` int(11) DEFAULT NULL,
  `idDatosPreexistencia` int(11) DEFAULT NULL,
  `idSolicitud` tinyint(1) DEFAULT NULL,
  `talla` varchar(45) DEFAULT NULL,
  `peso` float DEFAULT NULL,
  `esBeneficiario` tinyint(1) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT '1',
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  `celular` varchar(45) DEFAULT NULL,
  `correo` varchar(45) DEFAULT NULL,
  `referidoNombre` varchar(45) DEFAULT NULL,
  `referidoCorreo` varchar(45) DEFAULT NULL,
  `referidoCelular` varchar(45) DEFAULT NULL,
  `ingresoNoboa` date DEFAULT NULL,
  `agenteAsignado` int(11) DEFAULT NULL,
  PRIMARY KEY (`idCliente`),
  KEY `idPersona` (`idPersona`),
  KEY `agenteAsignado` (`agenteAsignado`),
  CONSTRAINT `Cliente_ibfk_2` FOREIGN KEY (`idPersona`) REFERENCES `Persona` (`idPersona`),
  CONSTRAINT `Cliente_ibfk_3` FOREIGN KEY (`agenteAsignado`) REFERENCES `Empleado` (`idEmpleado`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cliente`
--

LOCK TABLES `Cliente` WRITE;
/*!40000 ALTER TABLE `Cliente` DISABLE KEYS */;
INSERT INTO `Cliente` VALUES (5,12,8,10,NULL,NULL,'123',85,1,1,NULL,NULL,NULL,NULL,NULL,NULL,'0952654655','correo@gmail.com','Juan Perez','j@mail.com','0999999999','1996-05-21',2),(6,18,2,3,NULL,NULL,'22',55,1,1,NULL,NULL,NULL,NULL,NULL,NULL,'0914221411','lwev@gmail.com','amigolevi','amilev@gmai.com','098599999','2005-06-07',2),(7,19,3,5,NULL,NULL,'170',77,1,1,NULL,NULL,NULL,NULL,NULL,NULL,'0980062737','juancarlos.carrillovalencia@gmail.com','Johanna Carrillo','Carrillo@gmailc.com','0982927929','2022-02-01',1),(8,21,NULL,NULL,NULL,NULL,'52',25,1,1,NULL,NULL,NULL,NULL,NULL,NULL,'5222222555','mail@mil.com','YUN LIN','123@mail.com','0986655656','1994-02-03',2);
/*!40000 ALTER TABLE `Cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ClienteDependiente`
--

DROP TABLE IF EXISTS `ClienteDependiente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ClienteDependiente` (
  `idClienteDependiente` int(11) NOT NULL AUTO_INCREMENT,
  `idCliente` int(11) NOT NULL,
  `idDependiente` int(11) NOT NULL,
  `parentescoConTitular` varchar(45) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT '1',
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`idClienteDependiente`),
  KEY `idCliente` (`idCliente`),
  KEY `idDependiente` (`idDependiente`),
  CONSTRAINT `ClienteDependiente_ibfk_1` FOREIGN KEY (`idCliente`) REFERENCES `Cliente` (`idCliente`),
  CONSTRAINT `ClienteDependiente_ibfk_2` FOREIGN KEY (`idDependiente`) REFERENCES `Dependiente` (`idDependiente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ClienteDependiente`
--

LOCK TABLES `ClienteDependiente` WRITE;
/*!40000 ALTER TABLE `ClienteDependiente` DISABLE KEYS */;
/*!40000 ALTER TABLE `ClienteDependiente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Compania`
--

DROP TABLE IF EXISTS `Compania`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Compania` (
  `idCompania` int(11) NOT NULL AUTO_INCREMENT,
  `nombreCompania` varchar(45) DEFAULT NULL,
  `ruc` varchar(45) DEFAULT NULL,
  `nombreCoordinador` varchar(45) DEFAULT NULL,
  `celular` varchar(45) DEFAULT NULL,
  `correo` varchar(45) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT '1',
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`idCompania`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Compania`
--

LOCK TABLES `Compania` WRITE;
/*!40000 ALTER TABLE `Compania` DISABLE KEYS */;
INSERT INTO `Compania` VALUES (2,'BMI','1798285937001','Juan Anthony Gonzales M.','0959864257','juan@gmail.com',1,NULL,NULL,NULL,NULL,NULL,NULL),(3,'ASISKENW','1796169937051','Diego Pedro Lo','0959864111','nathi@es.com',1,NULL,NULL,NULL,NULL,NULL,NULL),(4,'PLAN VITAL','1796169937001','Carlos Claro Rosado','0954444251','abc@espol.edu',1,NULL,NULL,NULL,NULL,NULL,NULL),(5,'ZZZ VITAL','9796169937178','Goku Claro Rosado','0954444251','asd@espol.edu',0,NULL,NULL,NULL,NULL,NULL,NULL),(8,'HOPE','1796169934444','Maria del Consuelo Cruz','0956851254','mar1990@live.com',0,NULL,NULL,NULL,NULL,NULL,NULL),(9,'SEPROAMERICA','1487285932401','Pedro España Venezuela','0958652477','guayaquil@djanbu.us',0,NULL,NULL,NULL,NULL,NULL,NULL),(23,'DEADVITAL','10000010011','RR HH','09587458745','23@mail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL),(26,'BAD VITAL','1234567890018','Matias Lugarte','0945612371','lkdddd@mail.com',1,NULL,NULL,NULL,NULL,NULL,NULL),(29,'XXX','1114567890001','xxx xxx xxx xxx','0924587896','xxx@gmail.com',0,NULL,NULL,NULL,NULL,NULL,NULL),(30,'PRUEBA2','1798259937424','JUAN','0959865622','ja@esp.cos',0,NULL,NULL,NULL,NULL,NULL,NULL),(31,'ELIMINAR2','1798259937874','GABRIELA','0959874521','gab@hotmail.com',0,NULL,NULL,NULL,NULL,NULL,NULL),(32,'DELETE21','1798214537475','Rut Martinez','0954871234','ruc@gmail.com',1,NULL,NULL,NULL,NULL,NULL,NULL),(33,'Seguro Humana','0993218545001','Juan Carlos Carrillo Valencia','0980062280','juancarlos.carrillovalenciares@gmail.com',0,NULL,NULL,NULL,NULL,NULL,NULL),(34,'MEDICAL','1111111111001','Hector Lavoe','0922222542','lv@mail.com',1,NULL,NULL,NULL,NULL,NULL,NULL),(38,'Super Compañia','1555555555555','Brayan Betancourt','0952222222','brayan@hotrm.com',1,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `Compania` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ContactoProspecto`
--

DROP TABLE IF EXISTS `ContactoProspecto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ContactoProspecto` (
  `idContactoProspecto` int(11) NOT NULL AUTO_INCREMENT,
  `contenido` varchar(255) DEFAULT NULL,
  `tipo` int(11) DEFAULT NULL,
  `idProspecto` int(11) DEFAULT NULL,
  PRIMARY KEY (`idContactoProspecto`),
  KEY `FK_contactoprospecto_prospecto` (`idProspecto`),
  CONSTRAINT `FK_contactoprospecto_prospecto` FOREIGN KEY (`idProspecto`) REFERENCES `Prospecto` (`idProspecto`) ON DELETE SET NULL ON UPDATE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ContactoProspecto`
--

LOCK TABLES `ContactoProspecto` WRITE;
/*!40000 ALTER TABLE `ContactoProspecto` DISABLE KEYS */;
/*!40000 ALTER TABLE `ContactoProspecto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Contrato`
--

DROP TABLE IF EXISTS `Contrato`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Contrato` (
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
  `is_active` tinyint(1) DEFAULT '1',
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
  CONSTRAINT `Contrato_ibfk_1` FOREIGN KEY (`idCliente`) REFERENCES `Cliente` (`idCliente`),
  CONSTRAINT `Contrato_ibfk_2` FOREIGN KEY (`idPlan`) REFERENCES `Plan` (`idPlan`),
  CONSTRAINT `Contrato_ibfk_3` FOREIGN KEY (`idAgenteAsignado`) REFERENCES `Empleado` (`idEmpleado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Contrato`
--

LOCK TABLES `Contrato` WRITE;
/*!40000 ALTER TABLE `Contrato` DISABLE KEYS */;
/*!40000 ALTER TABLE `Contrato` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Cotizacion`
--

DROP TABLE IF EXISTS `Cotizacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Cotizacion` (
  `idCotizacion` int(11) NOT NULL AUTO_INCREMENT,
  `idProspecto` int(11) DEFAULT NULL,
  `idPlan` int(11) NOT NULL,
  `Estado` int(11) DEFAULT NULL,
  `Modificado` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Creado` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idCotizacion`) USING BTREE,
  KEY `FK_cotizacion_prospecto` (`idProspecto`),
  KEY `FK_cotizacion_plan` (`idPlan`),
  CONSTRAINT `FK_cotizacion_plan` FOREIGN KEY (`idPlan`) REFERENCES `Plan` (`idPlan`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_cotizacion_prospecto` FOREIGN KEY (`idProspecto`) REFERENCES `Prospecto` (`idProspecto`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cotizacion`
--

LOCK TABLES `Cotizacion` WRITE;
/*!40000 ALTER TABLE `Cotizacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `Cotizacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DatosFinancieros`
--

DROP TABLE IF EXISTS `DatosFinancieros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DatosFinancieros` (
  `idDatosFinancieros` int(11) NOT NULL AUTO_INCREMENT,
  `tipoActividadEconomica` varchar(45) DEFAULT NULL,
  `actividadEconomicaPrincipal` varchar(255) DEFAULT NULL,
  `tiempoEmpleo` int(11) DEFAULT NULL,
  `cargo` varchar(45) DEFAULT NULL,
  `ingresoMensual` float DEFAULT NULL,
  `ingresoExtra` float DEFAULT NULL,
  `actividadExtra` varchar(255) DEFAULT NULL,
  `totalIngresos` float DEFAULT NULL,
  `totalActivos` float DEFAULT NULL,
  `totalEgresos` float DEFAULT NULL,
  `totalPasivos` float DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT '1',
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  `idCliente` int(11) DEFAULT NULL,
  `razonSocial` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idDatosFinancieros`),
  KEY `idCliente` (`idCliente`),
  CONSTRAINT `DatosFinancieros_ibfk_1` FOREIGN KEY (`idCliente`) REFERENCES `Cliente` (`idCliente`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DatosFinancieros`
--

LOCK TABLES `DatosFinancieros` WRITE;
/*!40000 ALTER TABLE `DatosFinancieros` DISABLE KEYS */;
INSERT INTO `DatosFinancieros` VALUES (1,'Pollo','POLLO',2,'Cocinero',1000,0,'Ninguna',1000,100000,500,1255,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(2,'Natural','Ventas',2,'Jefe',800,500,'Cobrador',1300,25000,1000,5000,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(3,'Nuevo','POLLO',2,'Cocinero',1000,0,'Ninguna',1000,100000,500,1255,1,NULL,NULL,NULL,NULL,NULL,NULL,6,'Baterias'),(4,'Sistemas','Sistemas',20,'Gerente de Sistemas',240,345,'Consultor',685,234,345,231,1,NULL,NULL,NULL,NULL,NULL,NULL,7,'Hangaroa'),(5,'Sistemas','Sistemas',20,'Gerente de Sistemas',240,345,'Consultor',685,234,345,231,1,NULL,NULL,NULL,NULL,NULL,NULL,7,'Hangaroa'),(6,'Pollo','POLLO',2,'Cocinero',1000,0,'Ninguna',1000,100000,500,1255,1,NULL,NULL,NULL,NULL,NULL,NULL,5,'KFC'),(7,'Poll','POLLO',2,'Cocinero',1000,0,'Ninguna',1000,100000,500,1255,1,NULL,NULL,NULL,NULL,NULL,NULL,5,'KFC'),(8,'Poll','POLLO',2,'Cocin',1000,0,'Ninguna',1000,100000,500,1255,1,NULL,NULL,NULL,NULL,NULL,NULL,5,'KFC'),(9,'Poll','POLLO',2,'Cocin',1000,0,'Ninguna',1000,100000,500,1255,1,NULL,NULL,NULL,NULL,NULL,NULL,5,'KFC'),(10,'Poll','POLLO',2,'Cocin',1000,0,'Ninguna',1000,100000,500,1255,1,NULL,NULL,NULL,NULL,NULL,NULL,5,'KFC');
/*!40000 ALTER TABLE `DatosFinancieros` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Deducible`
--

DROP TABLE IF EXISTS `Deducible`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Deducible` (
  `idDeducible` int(11) NOT NULL AUTO_INCREMENT,
  `idPlan` int(11) NOT NULL,
  `tipoDeducible` varchar(45) DEFAULT NULL,
  `valor` float DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT '1',
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`idDeducible`),
  KEY `idPlan` (`idPlan`),
  CONSTRAINT `Deducible_ibfk_1` FOREIGN KEY (`idPlan`) REFERENCES `Plan` (`idPlan`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Deducible`
--

LOCK TABLES `Deducible` WRITE;
/*!40000 ALTER TABLE `Deducible` DISABLE KEYS */;
INSERT INTO `Deducible` VALUES (1,1,'Deducible Por Incapacidad',250,1,NULL,NULL,NULL,NULL,NULL,NULL),(2,1,'Deducible Por Año Contrato',250,1,NULL,NULL,NULL,NULL,NULL,NULL),(3,1,'Deducible Por Año Contrato',500,1,NULL,NULL,NULL,NULL,NULL,NULL),(4,1,'Deducible Por Año Contrato',1000,1,NULL,NULL,NULL,NULL,NULL,NULL),(5,2,'Deducible Por Incapacidad',4000,1,NULL,NULL,NULL,NULL,NULL,NULL),(6,3,'Deducible Por Incapacidad',4000,0,NULL,NULL,NULL,NULL,NULL,NULL),(7,13,'Deducible por año de contrato',1233,0,NULL,NULL,NULL,NULL,NULL,NULL),(8,13,'Deducible por incapacidad',23444,0,NULL,NULL,NULL,NULL,NULL,NULL),(9,12,'Deducible por incapacidad',1233,1,NULL,NULL,NULL,NULL,NULL,NULL),(10,14,'Deducible por incapacidad',1233,0,NULL,NULL,NULL,NULL,NULL,NULL),(11,14,'Deducible por incapacidad',2000,1,NULL,NULL,NULL,NULL,NULL,NULL),(12,13,'Deducible por año de contrato',1000,0,NULL,NULL,NULL,NULL,NULL,NULL),(13,13,'Deducible por año de contrato',1000,0,NULL,NULL,NULL,NULL,NULL,NULL),(14,13,'Deducible por año de contrato',2000,0,NULL,NULL,NULL,NULL,NULL,NULL),(15,13,'Deducible por año de contrato',1000,0,NULL,NULL,NULL,NULL,NULL,NULL),(16,13,'Deducible por incapacidad',23,0,NULL,NULL,NULL,NULL,NULL,NULL),(17,13,'Deducible por incapacidad',23,0,NULL,NULL,NULL,NULL,NULL,NULL),(18,13,'Deducible por incapacidad',2344,0,NULL,NULL,NULL,NULL,NULL,NULL),(19,13,'Deducible por incapacidad',3455,0,NULL,NULL,NULL,NULL,NULL,NULL),(20,13,'Deducible por incapacidad',3455,0,NULL,NULL,NULL,NULL,NULL,NULL),(21,13,'Deducible por año de contrato',3455,1,NULL,NULL,NULL,NULL,NULL,NULL),(22,13,'Deducible por incapacidad',23444,0,NULL,NULL,NULL,NULL,NULL,NULL),(23,5,'Deducible por año de contrato',23444,1,NULL,NULL,NULL,NULL,NULL,NULL),(24,5,'',23,0,NULL,NULL,NULL,NULL,NULL,NULL),(25,3,'Deducible por año de contrato',500,0,NULL,NULL,NULL,NULL,NULL,NULL),(26,3,'Deducible por incapacidad',5000,0,NULL,NULL,NULL,NULL,NULL,NULL),(27,3,'Deducible por año de contrato',5000,1,NULL,NULL,NULL,NULL,NULL,NULL),(28,3,'Deducible por incapacidad',23333,0,NULL,NULL,NULL,NULL,NULL,NULL),(29,16,'Deducible por incapacidad',34000,1,NULL,NULL,NULL,NULL,NULL,NULL),(30,12,'Deducible por año de contrato',12,1,NULL,NULL,NULL,NULL,NULL,NULL),(31,12,'Deducible por año de contrato',1223340,0,NULL,NULL,NULL,NULL,NULL,NULL),(32,3,'',12,0,NULL,NULL,NULL,NULL,NULL,NULL),(33,3,'',12232300,0,NULL,NULL,NULL,NULL,NULL,NULL),(34,13,'',233,0,NULL,NULL,NULL,NULL,NULL,NULL),(35,12,'',12,0,NULL,NULL,NULL,NULL,NULL,NULL),(36,16,'Deducible por año de contrato',1,1,NULL,NULL,NULL,NULL,NULL,NULL),(37,14,'Deducible por año de contrato',234,1,NULL,NULL,NULL,NULL,NULL,NULL),(38,3,'Deducible por incapacidad',784,0,NULL,NULL,NULL,NULL,NULL,NULL),(39,2,'Deducible por incapacidad',200,0,NULL,NULL,NULL,NULL,NULL,NULL),(40,2,'Deducible por incapacidad',200,1,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `Deducible` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Dependiente`
--

DROP TABLE IF EXISTS `Dependiente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Dependiente` (
  `idDependiente` int(11) NOT NULL AUTO_INCREMENT,
  `peso` float DEFAULT NULL,
  `nombres` varchar(45) DEFAULT NULL,
  `apellidos` varchar(45) DEFAULT NULL,
  `tipoDeIdentificacion` varchar(45) DEFAULT NULL,
  `numeroIdentificacion` varchar(45) DEFAULT NULL,
  `celular` varchar(45) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT '1',
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  `idCliente` int(11) DEFAULT NULL,
  `talla` float DEFAULT NULL,
  `parentesco` varchar(45) DEFAULT NULL,
  `correo` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idDependiente`),
  KEY `idCliente` (`idCliente`),
  CONSTRAINT `Dependiente_ibfk_1` FOREIGN KEY (`idCliente`) REFERENCES `Cliente` (`idCliente`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Dependiente`
--

LOCK TABLES `Dependiente` WRITE;
/*!40000 ALTER TABLE `Dependiente` DISABLE KEYS */;
INSERT INTO `Dependiente` VALUES (1,56,'MAria','Marino','pasaporte','0959862336','0955465545646',1,NULL,NULL,NULL,NULL,NULL,NULL,5,123,'madre','mail@mail.com');
/*!40000 ALTER TABLE `Dependiente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Direccion`
--

DROP TABLE IF EXISTS `Direccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Direccion` (
  `idDireccion` int(11) NOT NULL AUTO_INCREMENT,
  `idPersona` int(11) DEFAULT NULL,
  `tipoDireccion` varchar(45) DEFAULT NULL,
  `pais` varchar(45) DEFAULT NULL,
  `provincia` varchar(45) DEFAULT NULL,
  `ciudad` varchar(45) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT '1',
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  `datoDireccion` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idDireccion`),
  KEY `idPersona` (`idPersona`),
  CONSTRAINT `Direccion_ibfk_1` FOREIGN KEY (`idPersona`) REFERENCES `Persona` (`idPersona`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Direccion`
--

LOCK TABLES `Direccion` WRITE;
/*!40000 ALTER TABLE `Direccion` DISABLE KEYS */;
INSERT INTO `Direccion` VALUES (3,2,'Dirección de Trabajo','Ecuador','Guayas','Guayaquil',1,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(4,3,'Dirección de Trabajo','Cocos (Keeling) Islands','Valle del Cauca','Cartago',1,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(6,5,'Dirección de Trabajo','Ecuador','Guayas','Guayaquil',1,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(7,5,'Dirección de Trabajo','Colombia','Valle del Cauca','Cartago',1,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(9,7,'Dirección de Trabajo','Ecuador','Guayas','Guayaquil',1,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(10,7,'Dirección Domiciliaria','United States','California','Los Angeles',1,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(13,10,'Dirección de Trabajo','Ecuador','Imbabura','Atuntaqui',1,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(14,7,'Dirección de Trabajo','Paraguay','Boquerón Department','Colonia Neuland',1,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(16,1,'Dirección de Trabajo','Ecuador','Carchi','El Ángel',1,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(17,12,'Dirección de Trabajo','Dominica','Saint Luke Parish','Pointe Michel',1,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(19,18,'Dirección de Trabajo','Saint Lucia','Castries Quarter','Aurendel Hill',1,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(20,18,'Dirección Domiciliaria','Albania','Gjirokastër District','Bashkia Përmet',1,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `Direccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DocumentoContrato`
--

DROP TABLE IF EXISTS `DocumentoContrato`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DocumentoContrato` (
  `idDocumento` int(11) NOT NULL AUTO_INCREMENT,
  `idContrato` int(11) NOT NULL,
  `urlArchivo` varchar(45) DEFAULT NULL,
  `tipoDocumento` varchar(45) DEFAULT NULL,
  `descripcionDocumento` varchar(255) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT '1',
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`idDocumento`),
  KEY `idContrato` (`idContrato`),
  CONSTRAINT `DocumentoContrato_ibfk_1` FOREIGN KEY (`idContrato`) REFERENCES `Contrato` (`idContrato`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DocumentoContrato`
--

LOCK TABLES `DocumentoContrato` WRITE;
/*!40000 ALTER TABLE `DocumentoContrato` DISABLE KEYS */;
/*!40000 ALTER TABLE `DocumentoContrato` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DocumentoDependiente`
--

DROP TABLE IF EXISTS `DocumentoDependiente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DocumentoDependiente` (
  `idDocumento` int(11) NOT NULL AUTO_INCREMENT,
  `idDependiente` int(11) NOT NULL,
  `urlArchivo` varchar(45) DEFAULT NULL,
  `tipoDocumento` varchar(45) DEFAULT NULL,
  `descripcionDocumento` varchar(255) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT '1',
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`idDocumento`),
  KEY `idDependiente` (`idDependiente`),
  CONSTRAINT `DocumentoDependiente_ibfk_1` FOREIGN KEY (`idDependiente`) REFERENCES `Dependiente` (`idDependiente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DocumentoDependiente`
--

LOCK TABLES `DocumentoDependiente` WRITE;
/*!40000 ALTER TABLE `DocumentoDependiente` DISABLE KEYS */;
/*!40000 ALTER TABLE `DocumentoDependiente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DocumentoEmpleado`
--

DROP TABLE IF EXISTS `DocumentoEmpleado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DocumentoEmpleado` (
  `idDocumento` int(11) NOT NULL AUTO_INCREMENT,
  `idEmpleado` int(11) NOT NULL,
  `urlArchivo` varchar(255) DEFAULT NULL,
  `tipoDocumento` varchar(45) DEFAULT NULL,
  `descripcionDocumento` varchar(255) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT '1',
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`idDocumento`),
  KEY `idEmpleado` (`idEmpleado`),
  CONSTRAINT `DocumentoEmpleado_ibfk_1` FOREIGN KEY (`idEmpleado`) REFERENCES `Empleado` (`idEmpleado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DocumentoEmpleado`
--

LOCK TABLES `DocumentoEmpleado` WRITE;
/*!40000 ALTER TABLE `DocumentoEmpleado` DISABLE KEYS */;
/*!40000 ALTER TABLE `DocumentoEmpleado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DocumentoFinanciero`
--

DROP TABLE IF EXISTS `DocumentoFinanciero`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DocumentoFinanciero` (
  `idDocumento` int(11) NOT NULL AUTO_INCREMENT,
  `idDatosFinancieros` int(11) NOT NULL,
  `urlArchivo` varchar(255) DEFAULT NULL,
  `tipoDocumento` varchar(45) DEFAULT NULL,
  `descripcionDocumento` varchar(255) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT '1',
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`idDocumento`),
  KEY `idDatosFinancieros` (`idDatosFinancieros`),
  CONSTRAINT `DocumentoFinanciero_ibfk_1` FOREIGN KEY (`idDatosFinancieros`) REFERENCES `DatosFinancieros` (`idDatosFinancieros`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DocumentoFinanciero`
--

LOCK TABLES `DocumentoFinanciero` WRITE;
/*!40000 ALTER TABLE `DocumentoFinanciero` DISABLE KEYS */;
/*!40000 ALTER TABLE `DocumentoFinanciero` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Empleado`
--

DROP TABLE IF EXISTS `Empleado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Empleado` (
  `idEmpleado` int(11) NOT NULL AUTO_INCREMENT,
  `idPersona` int(11) NOT NULL,
  `fechaIngresoNoboa` date DEFAULT NULL,
  `idCargo` int(11) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT '1',
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  `celular` varchar(45) DEFAULT NULL,
  `correo` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idEmpleado`),
  KEY `idPersona` (`idPersona`),
  KEY `idCargo` (`idCargo`),
  CONSTRAINT `Empleado_ibfk_1` FOREIGN KEY (`idPersona`) REFERENCES `Persona` (`idPersona`),
  CONSTRAINT `Empleado_ibfk_2` FOREIGN KEY (`idCargo`) REFERENCES `Cargo` (`idCargo`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Empleado`
--

LOCK TABLES `Empleado` WRITE;
/*!40000 ALTER TABLE `Empleado` DISABLE KEYS */;
INSERT INTO `Empleado` VALUES (1,2,'2013-10-08',1,1,NULL,NULL,NULL,NULL,NULL,NULL,'0989555555','aa@as.com'),(2,3,'1998-11-10',1,1,NULL,NULL,NULL,NULL,NULL,NULL,'1444444444','basbd@asdas.com'),(4,22,NULL,301,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(5,23,NULL,302,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(6,24,NULL,302,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `Empleado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `NotificacionVentas`
--

DROP TABLE IF EXISTS `NotificacionVentas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `NotificacionVentas` (
  `idNotificacion` int(11) NOT NULL AUTO_INCREMENT,
  `idSupervisor` int(11) DEFAULT NULL,
  `titulo` varchar(255) DEFAULT NULL,
  `tipo` int(11) DEFAULT NULL,
  `contenido` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
  `creado` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idNotificacion`),
  KEY `FK_notificacionventas_empleado` (`idSupervisor`),
  CONSTRAINT `FK_notificacionventas_empleado` FOREIGN KEY (`idSupervisor`) REFERENCES `Empleado` (`idEmpleado`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `NotificacionVentas`
--

LOCK TABLES `NotificacionVentas` WRITE;
/*!40000 ALTER TABLE `NotificacionVentas` DISABLE KEYS */;
/*!40000 ALTER TABLE `NotificacionVentas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `NotificacionVentasRemitentes`
--

DROP TABLE IF EXISTS `NotificacionVentasRemitentes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `NotificacionVentasRemitentes` (
  `idNotificacion` int(11) NOT NULL,
  `idAgente` int(11) NOT NULL,
  `visto` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`idNotificacion`,`idAgente`),
  KEY `FK_notificacionventasremitentes_empleado` (`idAgente`),
  CONSTRAINT `FK_notificacionventasremitentes_empleado` FOREIGN KEY (`idAgente`) REFERENCES `Empleado` (`idEmpleado`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_notificacionventasremitentes_notificacionventas` FOREIGN KEY (`idNotificacion`) REFERENCES `NotificacionVentas` (`idNotificacion`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `NotificacionVentasRemitentes`
--

LOCK TABLES `NotificacionVentasRemitentes` WRITE;
/*!40000 ALTER TABLE `NotificacionVentasRemitentes` DISABLE KEYS */;
/*!40000 ALTER TABLE `NotificacionVentasRemitentes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Persona`
--

DROP TABLE IF EXISTS `Persona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Persona` (
  `idPersona` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `apellido` varchar(45) DEFAULT NULL,
  `tipoDeIdentificacion` varchar(45) DEFAULT NULL,
  `numeroIdentificacion` varchar(45) DEFAULT NULL,
  `fechaNacimiento` date DEFAULT NULL,
  `edad` int(11) DEFAULT NULL,
  `sexo` varchar(45) DEFAULT NULL,
  `tipoPersona` varchar(45) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT '1',
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  `estadoCivil` varchar(45) DEFAULT NULL,
  `idUsuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`idPersona`),
  KEY `idUsuario` (`idUsuario`),
  CONSTRAINT `Persona_ibfk_1` FOREIGN KEY (`idUsuario`) REFERENCES `Usuario` (`idUsuario`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Persona`
--

LOCK TABLES `Persona` WRITE;
/*!40000 ALTER TABLE `Persona` DISABLE KEYS */;
INSERT INTO `Persona` VALUES (1,'Brayan','Betancourt Ramirez','Cédula','2222224444','1996-04-25',26,'Masculino','cliente',1,NULL,NULL,NULL,NULL,NULL,NULL,'Soltero/a',NULL),(2,'Julio','Agente','Pasaporte','2222222222222','2015-12-11',25,'Femenino','empleado',1,NULL,NULL,NULL,NULL,NULL,NULL,'Casado/a',NULL),(3,'Anthony','Betancourt','Pasaporte','222222222222','1994-11-10',24,'Femenino','empleado',1,NULL,NULL,NULL,NULL,NULL,NULL,'Divorciado/a',NULL),(5,'Monica','Sanchez','Cédula','1111111111','1988-07-14',34,'Femenino','cliente',1,NULL,NULL,NULL,NULL,NULL,NULL,'Casado/a',NULL),(7,'Chun','De la Mar','Pasaporte','aas5555','2001-12-14',21,'Femenino','cliente',1,NULL,NULL,NULL,NULL,NULL,NULL,'Divorciado/a',NULL),(10,'Maria','Manriquez','Cédula','1239412904','1999-06-08',23,'Femenino','cliente',1,NULL,NULL,NULL,NULL,NULL,NULL,'Divorciado/a',NULL),(12,'Lee','Min','Cédula','0927854102','1991-10-15',31,'Femenino','cliente',1,NULL,NULL,NULL,NULL,NULL,NULL,'Casado/a',NULL),(14,'brayan','b','Pasaporte','2222222222','1997-07-10',25,'Femenino','cliente',1,NULL,NULL,NULL,NULL,NULL,NULL,'Casado/a',NULL),(15,'Geng','ASdd','Pasaporte','2222222','2000-10-10',22,'Femenino','cliente',1,NULL,NULL,NULL,NULL,NULL,NULL,'Casado/a',NULL),(16,'CliBrayan','CliBetancourt','Pasaporte','22222222222','1996-07-11',26,'Femenino','cliente',1,NULL,NULL,NULL,NULL,NULL,NULL,'Casado/a',NULL),(17,'brayan','betancourt','Pasaporte','444444444','2000-10-10',22,'Masculino','cliente',1,'2022-10-10',NULL,NULL,NULL,NULL,NULL,'Soltero/a',NULL),(18,'Levi','Solorzano','Pasaporte','Ec24445455454','1996-11-14',26,'Femenino','cliente',1,NULL,NULL,NULL,NULL,NULL,NULL,'Casado/a',NULL),(19,'Juan Carlos','Carrillo','Cédula','0917828282','2005-01-01',NULL,'Masculino','cliente',1,NULL,NULL,NULL,NULL,NULL,NULL,'Soltero/a',NULL),(21,'Lee','Won','Cédula','5464654564','1982-02-11',NULL,'Femenino','cliente',1,NULL,NULL,NULL,NULL,NULL,NULL,'Soltero/a',NULL),(22,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,8),(23,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,9),(24,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,10);
/*!40000 ALTER TABLE `Persona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Plan`
--

DROP TABLE IF EXISTS `Plan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Plan` (
  `idPlan` int(11) NOT NULL AUTO_INCREMENT,
  `idCompania` int(11) DEFAULT NULL,
  `tipoDePlan` varchar(45) DEFAULT NULL,
  `tipoDeSeguro` varchar(45) DEFAULT NULL,
  `nombrePlan` varchar(45) DEFAULT NULL,
  `tieneLimite` tinyint(1) DEFAULT NULL,
  `cobertura` float DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT '1',
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`idPlan`),
  KEY `idCompania` (`idCompania`),
  CONSTRAINT `Plan_ibfk_1` FOREIGN KEY (`idCompania`) REFERENCES `Compania` (`idCompania`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Plan`
--

LOCK TABLES `Plan` WRITE;
/*!40000 ALTER TABLE `Plan` DISABLE KEYS */;
INSERT INTO `Plan` VALUES (1,2,'Individual','Medico','INFINITY',1,500000,1,NULL,NULL,NULL,NULL,NULL,NULL),(2,3,'Corporativo','Medico','EPSYLONC',0,5000,1,NULL,NULL,NULL,NULL,NULL,NULL),(3,4,'Corporativo','Medico','DELTA',1,31000,1,NULL,NULL,NULL,NULL,NULL,NULL),(5,3,'Individual','Medico','MEGA',0,5000,1,NULL,NULL,NULL,NULL,NULL,NULL),(6,3,'Individual','Vehicular','FREE',0,14500,0,NULL,NULL,NULL,NULL,NULL,NULL),(10,26,'II','Salud','SU PLAN',0,35000,0,NULL,NULL,NULL,NULL,NULL,NULL),(11,26,'Individual','Salud','TRES',1,15400,0,NULL,NULL,NULL,NULL,NULL,NULL),(12,2,'Individual','Vehicular','GRATIS VITAL',0,1000000,1,NULL,NULL,NULL,NULL,NULL,NULL),(13,2,'Individual','Medico','DentalPlus',0,10000,1,NULL,NULL,NULL,NULL,NULL,NULL),(14,2,'Individual','Medico','HIPERMEGAOMEGA',1,50000,1,NULL,NULL,NULL,NULL,NULL,NULL),(15,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(16,32,'Individual','Vehicular','PLAN21',1,52000,1,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `Plan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Prospecto`
--

DROP TABLE IF EXISTS `Prospecto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Prospecto` (
  `idProspecto` int(11) NOT NULL AUTO_INCREMENT,
  `idAgente` int(11) DEFAULT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `apellido` varchar(45) DEFAULT NULL,
  `genero` varchar(45) DEFAULT NULL,
  `edad` varchar(45) DEFAULT NULL,
  `categoria` int(11) DEFAULT NULL,
  `direccion` varchar(45) DEFAULT NULL,
  `proyectadoActual` float DEFAULT NULL,
  `urlArchivo` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idProspecto`),
  KEY `FK_prospecto_empleado` (`idAgente`),
  CONSTRAINT `FK_prospecto_empleado` FOREIGN KEY (`idAgente`) REFERENCES `Empleado` (`idEmpleado`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Prospecto`
--

LOCK TABLES `Prospecto` WRITE;
/*!40000 ALTER TABLE `Prospecto` DISABLE KEYS */;
/*!40000 ALTER TABLE `Prospecto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ProspectoSesion`
--

DROP TABLE IF EXISTS `ProspectoSesion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ProspectoSesion` (
  `idProspectoSesion` int(11) NOT NULL AUTO_INCREMENT,
  `idProspecto` int(11) DEFAULT NULL,
  `inicio` datetime DEFAULT CURRENT_TIMESTAMP,
  `fin` datetime DEFAULT NULL,
  `estado` int(11) DEFAULT NULL,
  `tipo` int(11) DEFAULT NULL,
  `detalle` text,
  PRIMARY KEY (`idProspectoSesion`),
  KEY `FK_prospectosesion_prospecto` (`idProspecto`),
  CONSTRAINT `FK_prospectosesion_prospecto` FOREIGN KEY (`idProspecto`) REFERENCES `Prospecto` (`idProspecto`) ON DELETE SET NULL ON UPDATE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ProspectoSesion`
--

LOCK TABLES `ProspectoSesion` WRITE;
/*!40000 ALTER TABLE `ProspectoSesion` DISABLE KEYS */;
/*!40000 ALTER TABLE `ProspectoSesion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Usuario`
--

DROP TABLE IF EXISTS `Usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Usuario` (
  `idUsuario` int(11) NOT NULL AUTO_INCREMENT,
  `idPersona` int(11) DEFAULT NULL,
  `nombreUsuario` varchar(45) DEFAULT NULL,
  `claveusuario` varchar(255) DEFAULT NULL,
  `token` varchar(45) DEFAULT NULL,
  `fotoUsuario` varchar(45) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT '1',
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`idUsuario`),
  KEY `idPersona` (`idPersona`),
  CONSTRAINT `Usuario_ibfk_1` FOREIGN KEY (`idPersona`) REFERENCES `Persona` (`idPersona`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Usuario`
--

LOCK TABLES `Usuario` WRITE;
/*!40000 ALTER TABLE `Usuario` DISABLE KEYS */;
INSERT INTO `Usuario` VALUES (1,NULL,'supervisor','pbkdf2_sha256$390000$b0BQSoTx09xI6lrsiTWjhc$c',NULL,NULL,1,NULL,NULL,NULL,NULL,NULL,NULL),(2,NULL,'supervisor2','pbkdf2_sha256$390000$nYlAAp6JCOGhDjM953tBY8$X',NULL,NULL,1,NULL,NULL,NULL,NULL,NULL,NULL),(3,NULL,'agente1','pbkdf2_sha256$390000$NeQ3GvF3JB4cXZhfGJ53Cs$o',NULL,NULL,1,NULL,NULL,NULL,NULL,NULL,NULL),(4,NULL,'agente2','pbkdf2_sha256$390000$xt5ZLxitSE5SHU5rAZCtBv$L',NULL,NULL,1,NULL,NULL,NULL,NULL,NULL,NULL),(5,NULL,'agente3','pbkdf2_sha256$390000$3q9WmdN8LLfnbF6eQx1aZZ$5',NULL,NULL,1,NULL,NULL,NULL,NULL,NULL,NULL),(6,NULL,'agente4','pbkdf2_sha256$390000$qTxU7GouHErWlEVFoI9369$I',NULL,NULL,1,NULL,NULL,NULL,NULL,NULL,NULL),(7,NULL,'test','pbkdf2_sha256$390000$CJCJzRqIHSusz6Rjy1RFEd$sLxttW6ZHlIRLjPGLsPrdTwl1jskh38kdH1WEXqzi6E=',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(8,NULL,'supervisor1','pbkdf2_sha256$390000$G8QVBAzNNQffxk3Vlwdutc$IOlIJ6BYTY7j1vdWvU/WvPrRsC6JFsyMeHMHxLYEIhg=',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(9,NULL,'vendedor1','pbkdf2_sha256$390000$SjfciCHGl4cTvpmJQRazSU$EoyO6kGh3FPZrmNCvTgUZi8Msij/35Q3rhflVJhR0u0=',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(10,NULL,'vendedor2','pbkdf2_sha256$390000$Li1dVicTxPZW8fQpq3Sqyi$leDXdgG9etoDr1pUedYVVbNwQbbfYf8p6vXbnk7Ygfk=',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `Usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=357 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add compania',7,'add_compania'),(26,'Can change compania',7,'change_compania'),(27,'Can delete compania',7,'delete_compania'),(28,'Can view compania',7,'view_compania'),(29,'Can add Token',14,'add_token'),(30,'Can change Token',14,'change_token'),(31,'Can delete Token',14,'delete_token'),(32,'Can view Token',14,'view_token'),(33,'Can add token',15,'add_tokenproxy'),(34,'Can change token',15,'change_tokenproxy'),(35,'Can delete token',15,'delete_tokenproxy'),(36,'Can view token',15,'view_tokenproxy'),(37,'Can add cargo',16,'add_cargo'),(38,'Can change cargo',16,'change_cargo'),(39,'Can delete cargo',16,'delete_cargo'),(40,'Can view cargo',16,'view_cargo'),(41,'Can add cliente',17,'add_cliente'),(42,'Can change cliente',17,'change_cliente'),(43,'Can delete cliente',17,'delete_cliente'),(44,'Can view cliente',17,'view_cliente'),(45,'Can add clientedependiente',18,'add_clientedependiente'),(46,'Can change clientedependiente',18,'change_clientedependiente'),(47,'Can delete clientedependiente',18,'delete_clientedependiente'),(48,'Can view clientedependiente',18,'view_clientedependiente'),(49,'Can add compania',19,'add_compania'),(50,'Can change compania',19,'change_compania'),(51,'Can delete compania',19,'delete_compania'),(52,'Can view compania',19,'view_compania'),(53,'Can add contactoprospecto',20,'add_contactoprospecto'),(54,'Can change contactoprospecto',20,'change_contactoprospecto'),(55,'Can delete contactoprospecto',20,'delete_contactoprospecto'),(56,'Can view contactoprospecto',20,'view_contactoprospecto'),(57,'Can add contrato',21,'add_contrato'),(58,'Can change contrato',21,'change_contrato'),(59,'Can delete contrato',21,'delete_contrato'),(60,'Can view contrato',21,'view_contrato'),(61,'Can add cotizacion',22,'add_cotizacion'),(62,'Can change cotizacion',22,'change_cotizacion'),(63,'Can delete cotizacion',22,'delete_cotizacion'),(64,'Can view cotizacion',22,'view_cotizacion'),(65,'Can add datosfinancieros',23,'add_datosfinancieros'),(66,'Can change datosfinancieros',23,'change_datosfinancieros'),(67,'Can delete datosfinancieros',23,'delete_datosfinancieros'),(68,'Can view datosfinancieros',23,'view_datosfinancieros'),(69,'Can add deducible',24,'add_deducible'),(70,'Can change deducible',24,'change_deducible'),(71,'Can delete deducible',24,'delete_deducible'),(72,'Can view deducible',24,'view_deducible'),(73,'Can add dependiente',25,'add_dependiente'),(74,'Can change dependiente',25,'change_dependiente'),(75,'Can delete dependiente',25,'delete_dependiente'),(76,'Can view dependiente',25,'view_dependiente'),(77,'Can add direccion',26,'add_direccion'),(78,'Can change direccion',26,'change_direccion'),(79,'Can delete direccion',26,'delete_direccion'),(80,'Can view direccion',26,'view_direccion'),(81,'Can add documentocontrato',27,'add_documentocontrato'),(82,'Can change documentocontrato',27,'change_documentocontrato'),(83,'Can delete documentocontrato',27,'delete_documentocontrato'),(84,'Can view documentocontrato',27,'view_documentocontrato'),(85,'Can add documentodependiente',28,'add_documentodependiente'),(86,'Can change documentodependiente',28,'change_documentodependiente'),(87,'Can delete documentodependiente',28,'delete_documentodependiente'),(88,'Can view documentodependiente',28,'view_documentodependiente'),(89,'Can add documentoempleado',29,'add_documentoempleado'),(90,'Can change documentoempleado',29,'change_documentoempleado'),(91,'Can delete documentoempleado',29,'delete_documentoempleado'),(92,'Can view documentoempleado',29,'view_documentoempleado'),(93,'Can add documentofinanciero',30,'add_documentofinanciero'),(94,'Can change documentofinanciero',30,'change_documentofinanciero'),(95,'Can delete documentofinanciero',30,'delete_documentofinanciero'),(96,'Can view documentofinanciero',30,'view_documentofinanciero'),(97,'Can add empleado',31,'add_empleado'),(98,'Can change empleado',31,'change_empleado'),(99,'Can delete empleado',31,'delete_empleado'),(100,'Can view empleado',31,'view_empleado'),(101,'Can add notificacionventas',32,'add_notificacionventas'),(102,'Can change notificacionventas',32,'change_notificacionventas'),(103,'Can delete notificacionventas',32,'delete_notificacionventas'),(104,'Can view notificacionventas',32,'view_notificacionventas'),(105,'Can add notificacionventasremitentes',33,'add_notificacionventasremitentes'),(106,'Can change notificacionventasremitentes',33,'change_notificacionventasremitentes'),(107,'Can delete notificacionventasremitentes',33,'delete_notificacionventasremitentes'),(108,'Can view notificacionventasremitentes',33,'view_notificacionventasremitentes'),(109,'Can add persona',34,'add_persona'),(110,'Can change persona',34,'change_persona'),(111,'Can delete persona',34,'delete_persona'),(112,'Can view persona',34,'view_persona'),(113,'Can add plan',35,'add_plan'),(114,'Can change plan',35,'change_plan'),(115,'Can delete plan',35,'delete_plan'),(116,'Can view plan',35,'view_plan'),(117,'Can add prospecto',36,'add_prospecto'),(118,'Can change prospecto',36,'change_prospecto'),(119,'Can delete prospecto',36,'delete_prospecto'),(120,'Can view prospecto',36,'view_prospecto'),(121,'Can add prospectosesion',37,'add_prospectosesion'),(122,'Can change prospectosesion',37,'change_prospectosesion'),(123,'Can delete prospectosesion',37,'delete_prospectosesion'),(124,'Can view prospectosesion',37,'view_prospectosesion'),(125,'Can add usuario',38,'add_usuario'),(126,'Can change usuario',38,'change_usuario'),(127,'Can delete usuario',38,'delete_usuario'),(128,'Can view usuario',38,'view_usuario'),(129,'Can add auth group',39,'add_authgroup'),(130,'Can change auth group',39,'change_authgroup'),(131,'Can delete auth group',39,'delete_authgroup'),(132,'Can view auth group',39,'view_authgroup'),(133,'Can add auth group permissions',40,'add_authgrouppermissions'),(134,'Can change auth group permissions',40,'change_authgrouppermissions'),(135,'Can delete auth group permissions',40,'delete_authgrouppermissions'),(136,'Can view auth group permissions',40,'view_authgrouppermissions'),(137,'Can add auth permission',41,'add_authpermission'),(138,'Can change auth permission',41,'change_authpermission'),(139,'Can delete auth permission',41,'delete_authpermission'),(140,'Can view auth permission',41,'view_authpermission'),(141,'Can add auth user',42,'add_authuser'),(142,'Can change auth user',42,'change_authuser'),(143,'Can delete auth user',42,'delete_authuser'),(144,'Can view auth user',42,'view_authuser'),(145,'Can add auth user groups',43,'add_authusergroups'),(146,'Can change auth user groups',43,'change_authusergroups'),(147,'Can delete auth user groups',43,'delete_authusergroups'),(148,'Can view auth user groups',43,'view_authusergroups'),(149,'Can add auth user user permissions',44,'add_authuseruserpermissions'),(150,'Can change auth user user permissions',44,'change_authuseruserpermissions'),(151,'Can delete auth user user permissions',44,'delete_authuseruserpermissions'),(152,'Can view auth user user permissions',44,'view_authuseruserpermissions'),(153,'Can add datosfacturacion',45,'add_datosfacturacion'),(154,'Can change datosfacturacion',45,'change_datosfacturacion'),(155,'Can delete datosfacturacion',45,'delete_datosfacturacion'),(156,'Can view datosfacturacion',45,'view_datosfacturacion'),(157,'Can add django admin log',46,'add_djangoadminlog'),(158,'Can change django admin log',46,'change_djangoadminlog'),(159,'Can delete django admin log',46,'delete_djangoadminlog'),(160,'Can view django admin log',46,'view_djangoadminlog'),(161,'Can add django content type',47,'add_djangocontenttype'),(162,'Can change django content type',47,'change_djangocontenttype'),(163,'Can delete django content type',47,'delete_djangocontenttype'),(164,'Can view django content type',47,'view_djangocontenttype'),(165,'Can add django migrations',48,'add_djangomigrations'),(166,'Can change django migrations',48,'change_djangomigrations'),(167,'Can delete django migrations',48,'delete_djangomigrations'),(168,'Can view django migrations',48,'view_djangomigrations'),(169,'Can add django session',49,'add_djangosession'),(170,'Can change django session',49,'change_djangosession'),(171,'Can delete django session',49,'delete_djangosession'),(172,'Can view django session',49,'view_djangosession'),(173,'Can add plan',8,'add_plan'),(174,'Can change plan',8,'change_plan'),(175,'Can delete plan',8,'delete_plan'),(176,'Can view plan',8,'view_plan'),(177,'Can add deducible',9,'add_deducible'),(178,'Can change deducible',9,'change_deducible'),(179,'Can delete deducible',9,'delete_deducible'),(180,'Can view deducible',9,'view_deducible'),(181,'Can add persona',13,'add_persona'),(182,'Can change persona',13,'change_persona'),(183,'Can delete persona',13,'delete_persona'),(184,'Can view persona',13,'view_persona'),(185,'Can add direccion',50,'add_direccion'),(186,'Can change direccion',50,'change_direccion'),(187,'Can delete direccion',50,'delete_direccion'),(188,'Can view direccion',50,'view_direccion'),(189,'Can add usuario',51,'add_usuario'),(190,'Can change usuario',51,'change_usuario'),(191,'Can delete usuario',51,'delete_usuario'),(192,'Can view usuario',51,'view_usuario'),(193,'Can add cargo',10,'add_cargo'),(194,'Can change cargo',10,'change_cargo'),(195,'Can delete cargo',10,'delete_cargo'),(196,'Can view cargo',10,'view_cargo'),(197,'Can add empleado',52,'add_empleado'),(198,'Can change empleado',52,'change_empleado'),(199,'Can delete empleado',52,'delete_empleado'),(200,'Can view empleado',52,'view_empleado'),(201,'Can add documento empleado',53,'add_documentoempleado'),(202,'Can change documento empleado',53,'change_documentoempleado'),(203,'Can delete documento empleado',53,'delete_documentoempleado'),(204,'Can view documento empleado',53,'view_documentoempleado'),(205,'Can add datos financieros',54,'add_datosfinancieros'),(206,'Can change datos financieros',54,'change_datosfinancieros'),(207,'Can delete datos financieros',54,'delete_datosfinancieros'),(208,'Can view datos financieros',54,'view_datosfinancieros'),(209,'Can add cliente',12,'add_cliente'),(210,'Can change cliente',12,'change_cliente'),(211,'Can delete cliente',12,'delete_cliente'),(212,'Can view cliente',12,'view_cliente'),(213,'Can add dependiente',11,'add_dependiente'),(214,'Can change dependiente',11,'change_dependiente'),(215,'Can delete dependiente',11,'delete_dependiente'),(216,'Can view dependiente',11,'view_dependiente'),(217,'Can add documento financiero',55,'add_documentofinanciero'),(218,'Can change documento financiero',55,'change_documentofinanciero'),(219,'Can delete documento financiero',55,'delete_documentofinanciero'),(220,'Can view documento financiero',55,'view_documentofinanciero'),(221,'Can add datos facturacion',56,'add_datosfacturacion'),(222,'Can change datos facturacion',56,'change_datosfacturacion'),(223,'Can delete datos facturacion',56,'delete_datosfacturacion'),(224,'Can view datos facturacion',56,'view_datosfacturacion'),(225,'Can add auth group',57,'add_authgroup'),(226,'Can change auth group',57,'change_authgroup'),(227,'Can delete auth group',57,'delete_authgroup'),(228,'Can view auth group',57,'view_authgroup'),(229,'Can add auth group permissions',58,'add_authgrouppermissions'),(230,'Can change auth group permissions',58,'change_authgrouppermissions'),(231,'Can delete auth group permissions',58,'delete_authgrouppermissions'),(232,'Can view auth group permissions',58,'view_authgrouppermissions'),(233,'Can add auth permission',59,'add_authpermission'),(234,'Can change auth permission',59,'change_authpermission'),(235,'Can delete auth permission',59,'delete_authpermission'),(236,'Can view auth permission',59,'view_authpermission'),(237,'Can add auth user',60,'add_authuser'),(238,'Can change auth user',60,'change_authuser'),(239,'Can delete auth user',60,'delete_authuser'),(240,'Can view auth user',60,'view_authuser'),(241,'Can add auth user groups',61,'add_authusergroups'),(242,'Can change auth user groups',61,'change_authusergroups'),(243,'Can delete auth user groups',61,'delete_authusergroups'),(244,'Can view auth user groups',61,'view_authusergroups'),(245,'Can add auth user user permissions',62,'add_authuseruserpermissions'),(246,'Can change auth user user permissions',62,'change_authuseruserpermissions'),(247,'Can delete auth user user permissions',62,'delete_authuseruserpermissions'),(248,'Can view auth user user permissions',62,'view_authuseruserpermissions'),(249,'Can add authtoken token',63,'add_authtokentoken'),(250,'Can change authtoken token',63,'change_authtokentoken'),(251,'Can delete authtoken token',63,'delete_authtokentoken'),(252,'Can view authtoken token',63,'view_authtokentoken'),(253,'Can add cargo',64,'add_cargo'),(254,'Can change cargo',64,'change_cargo'),(255,'Can delete cargo',64,'delete_cargo'),(256,'Can view cargo',64,'view_cargo'),(257,'Can add cliente',65,'add_cliente'),(258,'Can change cliente',65,'change_cliente'),(259,'Can delete cliente',65,'delete_cliente'),(260,'Can view cliente',65,'view_cliente'),(261,'Can add clientedependiente',66,'add_clientedependiente'),(262,'Can change clientedependiente',66,'change_clientedependiente'),(263,'Can delete clientedependiente',66,'delete_clientedependiente'),(264,'Can view clientedependiente',66,'view_clientedependiente'),(265,'Can add compania',67,'add_compania'),(266,'Can change compania',67,'change_compania'),(267,'Can delete compania',67,'delete_compania'),(268,'Can view compania',67,'view_compania'),(269,'Can add contactoprospecto',68,'add_contactoprospecto'),(270,'Can change contactoprospecto',68,'change_contactoprospecto'),(271,'Can delete contactoprospecto',68,'delete_contactoprospecto'),(272,'Can view contactoprospecto',68,'view_contactoprospecto'),(273,'Can add contrato',69,'add_contrato'),(274,'Can change contrato',69,'change_contrato'),(275,'Can delete contrato',69,'delete_contrato'),(276,'Can view contrato',69,'view_contrato'),(277,'Can add cotizacion',70,'add_cotizacion'),(278,'Can change cotizacion',70,'change_cotizacion'),(279,'Can delete cotizacion',70,'delete_cotizacion'),(280,'Can view cotizacion',70,'view_cotizacion'),(281,'Can add deducible',71,'add_deducible'),(282,'Can change deducible',71,'change_deducible'),(283,'Can delete deducible',71,'delete_deducible'),(284,'Can view deducible',71,'view_deducible'),(285,'Can add dependiente',72,'add_dependiente'),(286,'Can change dependiente',72,'change_dependiente'),(287,'Can delete dependiente',72,'delete_dependiente'),(288,'Can view dependiente',72,'view_dependiente'),(289,'Can add direccion',73,'add_direccion'),(290,'Can change direccion',73,'change_direccion'),(291,'Can delete direccion',73,'delete_direccion'),(292,'Can view direccion',73,'view_direccion'),(293,'Can add django admin log',74,'add_djangoadminlog'),(294,'Can change django admin log',74,'change_djangoadminlog'),(295,'Can delete django admin log',74,'delete_djangoadminlog'),(296,'Can view django admin log',74,'view_djangoadminlog'),(297,'Can add django content type',75,'add_djangocontenttype'),(298,'Can change django content type',75,'change_djangocontenttype'),(299,'Can delete django content type',75,'delete_djangocontenttype'),(300,'Can view django content type',75,'view_djangocontenttype'),(301,'Can add django migrations',76,'add_djangomigrations'),(302,'Can change django migrations',76,'change_djangomigrations'),(303,'Can delete django migrations',76,'delete_djangomigrations'),(304,'Can view django migrations',76,'view_djangomigrations'),(305,'Can add django session',77,'add_djangosession'),(306,'Can change django session',77,'change_djangosession'),(307,'Can delete django session',77,'delete_djangosession'),(308,'Can view django session',77,'view_djangosession'),(309,'Can add documentocontrato',78,'add_documentocontrato'),(310,'Can change documentocontrato',78,'change_documentocontrato'),(311,'Can delete documentocontrato',78,'delete_documentocontrato'),(312,'Can view documentocontrato',78,'view_documentocontrato'),(313,'Can add documentodependiente',79,'add_documentodependiente'),(314,'Can change documentodependiente',79,'change_documentodependiente'),(315,'Can delete documentodependiente',79,'delete_documentodependiente'),(316,'Can view documentodependiente',79,'view_documentodependiente'),(317,'Can add documentoempleado',80,'add_documentoempleado'),(318,'Can change documentoempleado',80,'change_documentoempleado'),(319,'Can delete documentoempleado',80,'delete_documentoempleado'),(320,'Can view documentoempleado',80,'view_documentoempleado'),(321,'Can add empleado',81,'add_empleado'),(322,'Can change empleado',81,'change_empleado'),(323,'Can delete empleado',81,'delete_empleado'),(324,'Can view empleado',81,'view_empleado'),(325,'Can add notificacionventas',82,'add_notificacionventas'),(326,'Can change notificacionventas',82,'change_notificacionventas'),(327,'Can delete notificacionventas',82,'delete_notificacionventas'),(328,'Can view notificacionventas',82,'view_notificacionventas'),(329,'Can add notificacionventasremitentes',83,'add_notificacionventasremitentes'),(330,'Can change notificacionventasremitentes',83,'change_notificacionventasremitentes'),(331,'Can delete notificacionventasremitentes',83,'delete_notificacionventasremitentes'),(332,'Can view notificacionventasremitentes',83,'view_notificacionventasremitentes'),(333,'Can add persona',84,'add_persona'),(334,'Can change persona',84,'change_persona'),(335,'Can delete persona',84,'delete_persona'),(336,'Can view persona',84,'view_persona'),(337,'Can add plan',85,'add_plan'),(338,'Can change plan',85,'change_plan'),(339,'Can delete plan',85,'delete_plan'),(340,'Can view plan',85,'view_plan'),(341,'Can add prospecto',86,'add_prospecto'),(342,'Can change prospecto',86,'change_prospecto'),(343,'Can delete prospecto',86,'delete_prospecto'),(344,'Can view prospecto',86,'view_prospecto'),(345,'Can add prospectosesion',87,'add_prospectosesion'),(346,'Can change prospectosesion',87,'change_prospectosesion'),(347,'Can delete prospectosesion',87,'delete_prospectosesion'),(348,'Can view prospectosesion',87,'view_prospectosesion'),(349,'Can add referido',88,'add_referido'),(350,'Can change referido',88,'change_referido'),(351,'Can delete referido',88,'delete_referido'),(352,'Can view referido',88,'view_referido'),(353,'Can add usuario',89,'add_usuario'),(354,'Can change usuario',89,'change_usuario'),(355,'Can delete usuario',89,'delete_usuario'),(356,'Can view usuario',89,'view_usuario');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
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
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$390000$b0BQSoTx09xI6lrsiTWjhc$cFDcjFAYA7nJKwQJcx9kuG0RCQyi7N/clsZsJLGlOvU=',NULL,0,'supervisor','','','',0,1,'2022-08-29 20:14:28.267643'),(2,'pbkdf2_sha256$390000$nYlAAp6JCOGhDjM953tBY8$XJpSZbi48PDconrzmhdxeorJag5aX8KaRLo/ZC2zci8=',NULL,0,'supervisor2','','','',0,1,'2022-08-29 20:14:36.820012'),(3,'pbkdf2_sha256$390000$NeQ3GvF3JB4cXZhfGJ53Cs$oE36z2Y11iumCWdu6IR2vpV2HSDpfbicuztjefwzeNg=',NULL,0,'agente1','','','',0,1,'2022-08-29 20:14:51.829039'),(4,'pbkdf2_sha256$390000$xt5ZLxitSE5SHU5rAZCtBv$LHpARRyosVF7rv5Nl2HKB4YJN+Npp1xqkqjV9BpMyD0=',NULL,0,'agente2','','','',0,1,'2022-08-29 20:15:06.027633'),(5,'pbkdf2_sha256$390000$3q9WmdN8LLfnbF6eQx1aZZ$5+Zj1fSg3eJZXIX0B6kmmfyQvdXD08UVgKc06Yfqugw=',NULL,0,'agente3','','','',0,1,'2022-08-29 20:15:11.812508'),(6,'pbkdf2_sha256$390000$qTxU7GouHErWlEVFoI9369$ITn06k5EBDKnpQR0sj/L1y9vCCsumYchlLUG3oQ8GR0=',NULL,0,'agente4','','','',0,1,'2022-08-29 20:15:17.007355'),(7,'pbkdf2_sha256$390000$CJCJzRqIHSusz6Rjy1RFEd$sLxttW6ZHlIRLjPGLsPrdTwl1jskh38kdH1WEXqzi6E=',NULL,0,'test','','','',0,1,'2022-10-21 18:46:11.308792'),(8,'pbkdf2_sha256$390000$G8QVBAzNNQffxk3Vlwdutc$IOlIJ6BYTY7j1vdWvU/WvPrRsC6JFsyMeHMHxLYEIhg=',NULL,0,'supervisor1','','','',0,1,'2022-10-21 18:51:18.588002'),(9,'pbkdf2_sha256$390000$SjfciCHGl4cTvpmJQRazSU$EoyO6kGh3FPZrmNCvTgUZi8Msij/35Q3rhflVJhR0u0=',NULL,0,'vendedor1','','','',0,1,'2022-10-21 18:51:56.504836'),(10,'pbkdf2_sha256$390000$Li1dVicTxPZW8fQpq3Sqyi$leDXdgG9etoDr1pUedYVVbNwQbbfYf8p6vXbnk7Ygfk=',NULL,0,'vendedor2','','','',0,1,'2022-10-21 18:52:04.520062');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authtoken_token`
--

DROP TABLE IF EXISTS `authtoken_token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authtoken_token`
--

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;
INSERT INTO `authtoken_token` VALUES ('28768d67edec9bc3ac2e41b6caa02a2247ecbbf8','2022-10-21 18:05:43.545259',1),('7480a90b5e94cd464c3a404d27dab868e18a2248','2022-10-21 18:47:30.729882',7),('c86c6765fa2949af2e4aeb0b1608872b248e9bf2','2022-10-21 18:52:21.372514',8);
/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `datosFacturacion`
--

DROP TABLE IF EXISTS `datosFacturacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `datosFacturacion` (
  `idDatosFacturacion` int(11) NOT NULL AUTO_INCREMENT,
  `idCliente` int(11) NOT NULL,
  `tipoDeIdentificacion` varchar(45) DEFAULT NULL,
  `numeroIdentificacion` varchar(45) DEFAULT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `apellido` varchar(45) DEFAULT NULL,
  `correo` varchar(45) DEFAULT NULL,
  `celular` varchar(45) DEFAULT NULL,
  `tipoFormadePago` varchar(45) DEFAULT NULL,
  `nombreTarjeta` varchar(45) DEFAULT NULL,
  `nombreInstitucionBancaria` varchar(45) DEFAULT NULL,
  `numeroCuenta` varchar(45) DEFAULT NULL,
  `contactoNombre` varchar(45) DEFAULT NULL,
  `contactoCorreo` varchar(45) DEFAULT NULL,
  `contactoCelular` varchar(45) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT '1',
  `fecha_creado` date DEFAULT NULL,
  `creado_por_usuario` varchar(45) DEFAULT NULL,
  `creado_id_usuario` int(11) DEFAULT NULL,
  `fecha_modificado` date DEFAULT NULL,
  `modificado_por_usuario` varchar(45) DEFAULT NULL,
  `modificado_id_usuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`idDatosFacturacion`),
  KEY `idCliente` (`idCliente`),
  CONSTRAINT `datosFacturacion_ibfk_1` FOREIGN KEY (`idCliente`) REFERENCES `Cliente` (`idCliente`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `datosFacturacion`
--

LOCK TABLES `datosFacturacion` WRITE;
/*!40000 ALTER TABLE `datosFacturacion` DISABLE KEYS */;
INSERT INTO `datosFacturacion` VALUES (1,5,'Cédula','0927854102','juliana','martinez','correo@gmail.com','0952654655','Cuenta Corriente','asd','asd','999999','asdasd','asd@asds.com','059899999',1,NULL,NULL,NULL,NULL,NULL,NULL),(2,6,'Cédula','0927854102','juliana','martinez','correo@gmail.com','0952654655','Cuenta Corriente','asd','asd','999999','asdasd','asd@asds.com','059899999',1,NULL,NULL,NULL,NULL,NULL,NULL),(3,7,'Cédula','0927854102','juliana','martinez','correo@gmail.com','0952654655','Cuenta Corriente','asd','asd','999999','asdasd','asd@asds.com','059899999',1,NULL,NULL,NULL,NULL,NULL,NULL),(4,5,'Cédula','0927854102','Carla','Morena','correo@gmail.com','0952654655','Cuenta Corriente','asd','asd','999999','asdasd','asd@asds.com','059899999',1,NULL,NULL,NULL,NULL,NULL,NULL),(5,5,'Cédula','0927854102','Carla','Morena','correo@gmail.com','0952654655','Cuenta Corriente','asd','asd','999999','asdasd','asd@asds.com','059899999',1,NULL,NULL,NULL,NULL,NULL,NULL),(6,5,'Cédula','0927854102','Carla','Morena','correo@gmail.com','0952654655','Cuenta Corriente','asd','asd','999999','asdasd','asd@asds.com','059899999',1,NULL,NULL,NULL,NULL,NULL,NULL),(7,5,'Cédula','0927854102','Carla','Morena','correo@gmail.com','0952654655','Cuenta Corriente','asd','asd','999999','asdasd','asd@asds.com','059899999',1,NULL,NULL,NULL,NULL,NULL,NULL),(8,5,'Cédula','0927854102','Carla','Morena','correo@gmail.com','0952654655','Tarjeta de Credito','asd','asd','999999','asdasd','asd@asds.com','059899999',1,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `datosFacturacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=90 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(14,'authtoken','token'),(15,'authtoken','tokenproxy'),(57,'auth_manage','authgroup'),(58,'auth_manage','authgrouppermissions'),(59,'auth_manage','authpermission'),(63,'auth_manage','authtokentoken'),(60,'auth_manage','authuser'),(61,'auth_manage','authusergroups'),(62,'auth_manage','authuseruserpermissions'),(64,'auth_manage','cargo'),(65,'auth_manage','cliente'),(66,'auth_manage','clientedependiente'),(67,'auth_manage','compania'),(68,'auth_manage','contactoprospecto'),(69,'auth_manage','contrato'),(70,'auth_manage','cotizacion'),(71,'auth_manage','deducible'),(72,'auth_manage','dependiente'),(73,'auth_manage','direccion'),(74,'auth_manage','djangoadminlog'),(75,'auth_manage','djangocontenttype'),(76,'auth_manage','djangomigrations'),(77,'auth_manage','djangosession'),(78,'auth_manage','documentocontrato'),(79,'auth_manage','documentodependiente'),(80,'auth_manage','documentoempleado'),(81,'auth_manage','empleado'),(82,'auth_manage','notificacionventas'),(83,'auth_manage','notificacionventasremitentes'),(84,'auth_manage','persona'),(85,'auth_manage','plan'),(86,'auth_manage','prospecto'),(87,'auth_manage','prospectosesion'),(88,'auth_manage','referido'),(89,'auth_manage','usuario'),(5,'contenttypes','contenttype'),(39,'crm','authgroup'),(40,'crm','authgrouppermissions'),(41,'crm','authpermission'),(42,'crm','authuser'),(43,'crm','authusergroups'),(44,'crm','authuseruserpermissions'),(16,'crm','cargo'),(17,'crm','cliente'),(18,'crm','clientedependiente'),(19,'crm','compania'),(20,'crm','contactoprospecto'),(21,'crm','contrato'),(22,'crm','cotizacion'),(45,'crm','datosfacturacion'),(23,'crm','datosfinancieros'),(24,'crm','deducible'),(25,'crm','dependiente'),(26,'crm','direccion'),(46,'crm','djangoadminlog'),(47,'crm','djangocontenttype'),(48,'crm','djangomigrations'),(49,'crm','djangosession'),(27,'crm','documentocontrato'),(28,'crm','documentodependiente'),(29,'crm','documentoempleado'),(30,'crm','documentofinanciero'),(31,'crm','empleado'),(32,'crm','notificacionventas'),(33,'crm','notificacionventasremitentes'),(34,'crm','persona'),(35,'crm','plan'),(36,'crm','prospecto'),(37,'crm','prospectosesion'),(38,'crm','usuario'),(6,'sessions','session'),(10,'web','cargo'),(12,'web','cliente'),(7,'web','compania'),(56,'web','datosfacturacion'),(54,'web','datosfinancieros'),(9,'web','deducible'),(11,'web','dependiente'),(50,'web','direccion'),(53,'web','documentoempleado'),(55,'web','documentofinanciero'),(52,'web','empleado'),(13,'web','persona'),(8,'web','plan'),(51,'web','usuario');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-08-22 02:41:40.699711'),(2,'auth','0001_initial','2022-08-22 02:41:43.336691'),(3,'admin','0001_initial','2022-08-22 02:41:43.892632'),(4,'admin','0002_logentry_remove_auto_add','2022-08-22 02:41:43.932717'),(5,'admin','0003_logentry_add_action_flag_choices','2022-08-22 02:41:43.956654'),(6,'contenttypes','0002_remove_content_type_name','2022-08-22 02:41:44.488678'),(7,'auth','0002_alter_permission_name_max_length','2022-08-22 02:41:44.720641'),(8,'auth','0003_alter_user_email_max_length','2022-08-22 02:41:44.929966'),(9,'auth','0004_alter_user_username_opts','2022-08-22 02:41:44.955587'),(10,'auth','0005_alter_user_last_login_null','2022-08-22 02:41:45.160735'),(11,'auth','0006_require_contenttypes_0002','2022-08-22 02:41:45.180592'),(12,'auth','0007_alter_validators_add_error_messages','2022-08-22 02:41:45.198716'),(13,'auth','0008_alter_user_username_max_length','2022-08-22 02:41:45.368753'),(14,'auth','0009_alter_user_last_name_max_length','2022-08-22 02:41:45.592900'),(15,'auth','0010_alter_group_name_max_length','2022-08-22 02:41:45.841422'),(16,'auth','0011_update_proxy_permissions','2022-08-22 02:41:45.884777'),(17,'auth','0012_alter_user_first_name_max_length','2022-08-22 02:41:46.092691'),(18,'sessions','0001_initial','2022-08-22 02:41:46.336752'),(19,'web','0001_initial','2022-08-22 02:41:46.360749'),(20,'web','0002_alter_compania_table','2022-08-26 03:37:36.020251'),(21,'authtoken','0001_initial','2022-10-21 18:04:50.726369'),(22,'authtoken','0002_auto_20160226_1747','2022-10-21 18:04:50.787237'),(23,'authtoken','0003_tokenproxy','2022-10-21 18:04:50.811333');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('3i13cdmzhcg97sarlhc3i73matgmfami','.eJxVjE0OwiAYBe_C2hBA_uLSvWcgDz6QqqFJaVfGu0uTLnQ7M--9WcC21rD1vISJ2IVJdvplEemZ2y7ogXafeZrbukyR7wk_bOe3mfLrerR_BxW9jjUihHaGpDQEoCik4qG18cYXn11UUMqeUxxYANLm0SdH2maXpAD7fAEIqjjO:1olfoy:cBpNVKFrClQ2lDVZD0ll_3HNJ0oc5V_EhETKWpOuVvk','2022-11-04 00:23:32.751702'),('a0m8zt6bfc0iauly1kvgukw398meywxw','.eJxVjE0OwiAYBe_C2hBA_uLSvWcgDz6QqqFJaVfGu0uTLnQ7M--9WcC21rD1vISJ2IVJdvplEemZ2y7ogXafeZrbukyR7wk_bOe3mfLrerR_BxW9jjUihHaGpDQEoCik4qG18cYXn11UUMqeUxxYANLm0SdH2maXpAD7fAEIqjjO:1oj6LC:z77iSJmH5WIw1SWkjIqIr82pl33KicjfWmxgR1ggkhM','2022-10-27 22:06:10.782492'),('f8t1wzd3gul01gsg5ffjhjb06hl9gj2b','.eJxVjE0OwiAYBe_C2hBA_uLSvWcgDz6QqqFJaVfGu0uTLnQ7M--9WcC21rD1vISJ2IVJdvplEemZ2y7ogXafeZrbukyR7wk_bOe3mfLrerR_BxW9jjUihHaGpDQEoCik4qG18cYXn11UUMqeUxxYANLm0SdH2maXpAD7fAEIqjjO:1oPxQY:5i6AGQAxQbd2DmGPvI-hF8k5pRtTLl7j50PpY24brDQ','2022-09-05 02:44:34.608694'),('onbqo7bjc1n9u59qd9z33mpzap7pgcym','.eJxVjE0OwiAYBe_C2hBA_uLSvWcgDz6QqqFJaVfGu0uTLnQ7M--9WcC21rD1vISJ2IVJdvplEemZ2y7ogXafeZrbukyR7wk_bOe3mfLrerR_BxW9jjUihHaGpDQEoCik4qG18cYXn11UUMqeUxxYANLm0SdH2maXpAD7fAEIqjjO:1odruE:kNbyaMdRl3xncS_X-eSQNd6qKAQqqsW6sAL84OI_QAw','2022-10-13 11:40:42.280149');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-21 20:08:54
