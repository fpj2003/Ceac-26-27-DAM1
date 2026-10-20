CREATE TABLE conocimientos(
	id INT PRIMARY KEY AUTO_INCREMENT,
	id_usuario INT,
	Lenguaje VARCHAR(100)
	
);


INSERT INTO conocimientos VALUES(
	NULL,	
	1,
	'C++'
	
);

INSERT INTO conocimientos VALUES(
	NULL,
	1, 
	'Java'
	
);

INSERT INTO conocimientos VALUES (
	NULL,
	1, 
	'SQL'
	
);

INSERT INTO conocimientos VALUES (
	NULL,	
	1, 
	'HTML'
	
);

INSERT INTO conocimientos VALUES (
	NULL,
	1,
	'Python'
	
);


SELECT * FROM conocimientos;
