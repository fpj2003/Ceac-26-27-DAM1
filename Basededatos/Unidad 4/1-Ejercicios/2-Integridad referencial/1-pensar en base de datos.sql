Base de datos para aplicación de registrar tiempos de karts

Tablas necesarias : PILOTO, CIRCUITO,VUELTA,SESION

PILOTO
idPiloto
Nombre
Apellidos
Fecha de nacimiento
Email

CIRCUITO
idCircuito
Nombre
Ubicacion
Pais

VUELTA
idVuelta
Tiempo de vuelta
Numero de vuelta

SESION
idSesion
Fecha de la sesion
Estado de la pista
Modelo kart


CREATE DATABASE karts;

USE karts;

CREATE TABLE piloto(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(100),
  	apellidos VARCHAR(100),
  	fecha_de_nacimiento DATE,
  	email VARCHAR(100)
);

CREATE TABLE circuito(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(100),
  	ubicacion VARCHAR(100),
  	pais VARCHAR(100)
);

CREATE TABLE vuelta(
	id INT PRIMARY KEY AUTO_INCREMENT,
	tiempo_de_vuelta VARCHAR(100;),
	numero_de_vuelta INT
);

CREATE TABLE sesion(
	id INT PRIMARY KEY AUTO_INCREMENT,
	fecha_sesion DATE,
  	estado_pista VARCHAR(100),
  	modelo_kart VARCHAR(100)
);






