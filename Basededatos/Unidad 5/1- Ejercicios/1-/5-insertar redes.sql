CREATE TABLE redes_sociales(
	id INT PRIMARY KEY AUTO_INCREMENT,
  	id_usuario INT,
 	linkedin VARCHAR(100),
	github VARCHAR(100)
);

INSERT INTO redes_sociales VALUES(
	NULL,
	1,
	'https://www.linkedin.com/in/fernando-puig-jorda-269384440/',
	'https://github.com/fpj2003'
);


SELECT * FROM redes_sociales;
