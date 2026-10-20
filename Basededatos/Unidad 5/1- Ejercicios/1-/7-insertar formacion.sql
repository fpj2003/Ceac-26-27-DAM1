CREATE TABLE formacion(
	id INT PRIMARY KEY AUTO_INCREMENT,
	id_usuario INT,
	centro VARCHAR(100),
	descripcion TEXT,
	titulo VARCHAR(100),
	inicio VARCHAR(100),
	final VARCHAR(100)
);

INSERT INTO formacion VALUES (
	NULL,
	1,
	'Universitat de València',
	'Estudios sin finalizar',
	'Ingeniería Telemática',
	'Septiembre 2021',
	'Junio 2026'
);

INSERT INTO formacion VALUES(
	NULL,
	1,
	'Juniors Escola d Animadors (JEA)',
	NULL,
	'Monitor de Actividades de Tiempo Libre(MAT)',
	'Febrero 2022',
	'Enero 2025'
);

INSERT INTO formacion VALUES(
	NULL,
	1,
	'Colegio El Armelar',
	NULL,
	'Bachillerato',
	'Septiembre 2019',
	'Junio 2021'
);

INSERT INTO formacion VALUES (
	NULL,
	1,
	'Colegio El Armelar',
	NULL,
	'ESO',
	'Septiembre 2015',
	'Junio 2019'
);

SELECT * FROM formacion;
