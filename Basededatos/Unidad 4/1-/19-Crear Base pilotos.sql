CREATE DATABASE formula1 ;

USE formula1;

CREATE TABLE piloto(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(100),
  	apellidos VARCHAR(100),
  	pais VARCHAR(100),
  	escuderia VARCHAR(100),
  	numero INT
  
);

DESCRIBE piloto;

SELECT * FROM piloto;
