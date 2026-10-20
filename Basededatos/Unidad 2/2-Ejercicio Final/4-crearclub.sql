CREATE TABLE club (
    id_club INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100),
    ciudad VARCHAR(100),
    estadio VARCHAR(100),
    fecha_de_fundacion DATE
);
SHOW TABLES;
DESCRIBE club;