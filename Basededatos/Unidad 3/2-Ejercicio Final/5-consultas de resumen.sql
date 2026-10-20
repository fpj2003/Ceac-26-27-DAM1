SELECT COUNT(id_jugador) AS 'Total de jugadores' 
FROM jugadores;

SELECT SUM(goles) AS 'Total de goles' 
FROM jugadores;


SELECT 
MAX(goles) AS 'Goles del Pichichi ', 
MIN(goles) AS 'Mínimo de goles' 
FROM jugadores;

SELECT AVG(goles) AS 'Promedio de goles ' 
FROM jugadores;
