CREATE DATABASE karts;

USE karts;

CREATE TABLE piloto(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(100),
  	apellidos VARCHAR(100),
  	fecha_de_nacimiento DATE,
  	email VARCHAR(100)
);
