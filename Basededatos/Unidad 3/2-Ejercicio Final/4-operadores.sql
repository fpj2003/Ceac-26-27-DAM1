SELECT 
    nombre,
    apellidos,
    goles,
    goles >= 1 AS 'Goleador'
FROM jugadores;


SELECT 
    nombre, 
    apellidos, 
    posicion,
    goles,
    goles > 10 AND posicion = 'Delantero' AS 'Killer del area'
FROM jugadores;


SELECT 
    nombre, 
    apellidos, 
    posicion,
    goles,
    goles >= 1 AND posicion = 'Defensa' AS 'Defensa con gol'
FROM jugadores;


SELECT 
nombre AS 'Equipo',
victorias,
empates,
derrotas,
(victorias * 3) + empates AS 'Puntos Totales'
FROM club
