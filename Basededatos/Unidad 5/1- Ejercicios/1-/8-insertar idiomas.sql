CREATE TABLE idiomas(
	id INT PRIMARY KEY AUTO_INCREMENT,
	id_usuario INT,
	idioma VARCHAR(100),
	titulo VARCHAR(100)
);

INSERT INTO idiomas VALUES (
	NULL,
	1,
	'Español',
	'Nativo'
);

INSERT INTO idiomas VALUES (
	NULL,
	1,
	'Inglés ',
	'B2'
);

SELECT * FROM idiomas;
