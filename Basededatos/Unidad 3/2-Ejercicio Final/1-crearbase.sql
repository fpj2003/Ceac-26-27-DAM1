CREATE DATABASE futbol2;
USE futbol2;
SHOW TABLES;

CREATE TABLE jugadores (
    id_jugador INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    apellidos VARCHAR(100),
    fecha_de_nacimiento DATE,
    posicion VARCHAR(100),
    dorsal INT,
    id_club INT,
    goles INT
);
SHOW TABLES;
DESCRIBE jugadores;


CREATE TABLE club (
    id_club INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100),
    ciudad VARCHAR(100),
    estadio VARCHAR(100),
    fecha_de_fundacion DATE,
    victorias INT,
    empates INT,
    derrotas INT
);
SHOW TABLES;
DESCRIBE club;