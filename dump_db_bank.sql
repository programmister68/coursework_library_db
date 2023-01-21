-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: bank
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `currencies`
--

DROP TABLE IF EXISTS `currencies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `currencies` (
  `Currency_ID` int NOT NULL AUTO_INCREMENT,
  `Curr_Name` varchar(255) DEFAULT NULL,
  `Exchange_Rate` float(4,2) DEFAULT NULL,
  PRIMARY KEY (`Currency_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `currencies`
--

LOCK TABLES `currencies` WRITE;
/*!40000 ALTER TABLE `currencies` DISABLE KEYS */;
INSERT INTO `currencies` VALUES (1,'Рубль',0.00),(2,'Доллар',58.00),(3,'Евро',89.00),(5,'Тенге',0.11),(6,'Беларусский рубль',15.59),(7,'Гривна',1.78),(8,'Крона',2.22),(9,'Злотый',12.01);
/*!40000 ALTER TABLE `currencies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `depositors`
--

DROP TABLE IF EXISTS `depositors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `depositors` (
  `Depositor_ID` int NOT NULL AUTO_INCREMENT,
  `Depositor_Name` varchar(2000) DEFAULT NULL,
  `Depositor_Phone` varchar(255) DEFAULT NULL,
  `Depositor_Passport` varchar(255) DEFAULT NULL,
  `Dep_Sum` int DEFAULT NULL,
  `Refund_Sum` int DEFAULT NULL,
  `Dep_Date` varchar(255) DEFAULT NULL,
  `Refund_Date` varchar(255) DEFAULT NULL,
  `Refund_Status` varchar(255) DEFAULT NULL,
  `Employee_ID` int DEFAULT NULL,
  PRIMARY KEY (`Depositor_ID`),
  KEY `depositors_ibfk_1` (`Employee_ID`),
  CONSTRAINT `depositors_ibfk_1` FOREIGN KEY (`Employee_ID`) REFERENCES `employees` (`Employee_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `depositors`
--

LOCK TABLES `depositors` WRITE;
/*!40000 ALTER TABLE `depositors` DISABLE KEYS */;
INSERT INTO `depositors` VALUES (1,'Петров Михаил Сергеевич','8956678957','7865786544',50000,500,'2022-03-31','2022-04-02','выплачено',1),(5,'Иванов Сергей Михайлович','8956456446','6683446342',20000,4000,'2022-07-06','2022-07-08','не выплачено',1);
/*!40000 ALTER TABLE `depositors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deposits`
--

DROP TABLE IF EXISTS `deposits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `deposits` (
  `Deposit_ID` int NOT NULL AUTO_INCREMENT,
  `Dep_Name` varchar(255) DEFAULT NULL,
  `Percent_Rate` float(4,1) DEFAULT NULL,
  `Currency_ID` int DEFAULT NULL,
  `Depositor_ID` int DEFAULT NULL,
  PRIMARY KEY (`Deposit_ID`),
  KEY `deposits_ibfk_1` (`Currency_ID`),
  KEY `deposits_ibfk_2` (`Depositor_ID`),
  CONSTRAINT `deposits_ibfk_1` FOREIGN KEY (`Currency_ID`) REFERENCES `currencies` (`Currency_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `deposits_ibfk_2` FOREIGN KEY (`Depositor_ID`) REFERENCES `depositors` (`Depositor_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deposits`
--

LOCK TABLES `deposits` WRITE;
/*!40000 ALTER TABLE `deposits` DISABLE KEYS */;
INSERT INTO `deposits` VALUES (1,'Срочный',1.0,3,1),(4,'Накопительный',3.0,1,1),(8,'Сберегательный',1.0,1,1);
/*!40000 ALTER TABLE `deposits` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `Employee_ID` int NOT NULL AUTO_INCREMENT,
  `Emp_Name` varchar(2000) DEFAULT NULL,
  `Login` varchar(255) DEFAULT NULL,
  `Password` varchar(255) DEFAULT NULL,
  `Role` varchar(255) DEFAULT NULL,
  `Emp_Phone` varchar(255) DEFAULT NULL,
  `Emp_Passport` varchar(255) DEFAULT NULL,
  `Position_ID` int DEFAULT NULL,
  PRIMARY KEY (`Employee_ID`),
  KEY `employees_ibfk_1` (`Position_ID`),
  CONSTRAINT `employees_ibfk_1` FOREIGN KEY (`Position_ID`) REFERENCES `positions` (`Position_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1,'Иванов Иван Иванович','vanov2077','123abc','2','8924981548','7890879076',1),(2,'Иванов Пётр Рудольфович','rudolf9','123456','1','8934678904','6876784668',2),(6,'Фролов Игорь Антонович','123','123','1','8900674535','4567975556',1),(7,'Зоева Анна Евгениевна','abc','abc1','2','8976897457','6798456097',2);
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `positions`
--

DROP TABLE IF EXISTS `positions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `positions` (
  `Position_ID` int NOT NULL AUTO_INCREMENT,
  `Pos_Name` varchar(255) DEFAULT NULL,
  `Salary` int DEFAULT NULL,
  `Responsibility` mediumtext,
  `Requirement` mediumtext,
  PRIMARY KEY (`Position_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `positions`
--

LOCK TABLES `positions` WRITE;
/*!40000 ALTER TABLE `positions` DISABLE KEYS */;
INSERT INTO `positions` VALUES (1,' Бухгалтер в отделе кадров',45000,'Учёт банковских сотрудников','Ответственность, Опыт работы'),(2,'Операционист',56000,'Открытие и закрытие счетов клиентов по вкладам физических лиц','Способность к быстрому обучению.'),(4,'Охранник',38000,'Охранять банковское помещение','Хорошая физическая форма и внимательность');
/*!40000 ALTER TABLE `positions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-01  2:23:17
