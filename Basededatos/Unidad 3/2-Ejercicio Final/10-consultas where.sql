SELECT nombre, apellidos, posicion, goles 
FROM jugadores 
WHERE posicion = 'Delantero';

SELECT nombre AS 'Equipo', victorias 
FROM club 
WHERE victorias > 20;

SELECT 
club.nombre AS 'Equipo',
SUM(jugadores.goles) AS 'Goles totales de los delanteros'
FROM jugadores
LEFT JOIN club ON jugadores.id_club = club.id_club
WHERE jugadores.posicion = 'Delantero'
GROUP BY club.nombre
HAVING SUM(jugadores.goles) > 10
ORDER BY 'Goles totales de los delanteros';