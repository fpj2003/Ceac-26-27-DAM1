CREATE DATABASE karts;

USE karts;

CREATE TABLE piloto(
	id_piloto INT PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(100),
  	apellidos VARCHAR(100),
  	fecha_de_nacimiento DATE,
  	email VARCHAR(100)
);

CREATE TABLE vuelta(
	id_vuelta INT PRIMARY KEY AUTO_INCREMENT,
	id_sesion INT,
	numero_vuelta INT,
	tiempo_vuelta DECIMAL(6,3)
);

CREATE TABLE sesion(
	id_sesion INT PRIMARY KEY AUTO_INCREMENT,
	id_piloto INT,
	fecha DATE

);

