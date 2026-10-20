CREATE TABLE experiencias_laborales(
	id INT PRIMARY KEY AUTO_INCREMENT,
	id_usuario INT,
	empresa VARCHAR(100),
	descripcion TEXT,
	cargo VARCHAR(100),
	inicio VARCHAR(100),
	final VARCHAR(100)
);

INSERT INTO experiencias_laborales VALUES(
	NULL,
	1,
	'Juniors Anawin M.D',
	'Planificación, diseño y ejecución de actividades lúdicas y educativas para grupos de niños y adolescentes.
	Trabajo en equipo y coordinación con otros monitores para la organización de eventos, excursiones y campamentos. ',
	'Voluntario como monitor de tiempo libre',
	'Septiembre 2021',
	'Actualidad'
);

SELECT * FROM experiencias_laborales;

