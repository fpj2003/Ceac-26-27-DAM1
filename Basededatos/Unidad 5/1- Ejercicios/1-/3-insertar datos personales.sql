CREATE TABLE datos_personales(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(100),
  	apellidos VARCHAR(100)
);
INSERT INTO datos_personales VALUES(
	NULL,
	'Fernando',
	'Puig Jorda'
);

SELECT * FROM datos_personales;

