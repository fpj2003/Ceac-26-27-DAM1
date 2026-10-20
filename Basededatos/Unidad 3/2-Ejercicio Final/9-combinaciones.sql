SELECT 
club.nombre AS 'Nombre', 
SUM(jugadores.goles) AS 'Goles totales del equipo'
FROM jugadores
LEFT JOIN club ON jugadores.id_club = club.id_club
GROUP BY club.nombre;


SELECT 
jugadores.nombre AS 'Nombre',
jugadores.apellidos AS 'Apellidos',
club.nombre AS 'Equipo',
club.victorias AS 'Victorias'
FROM jugadores
LEFT JOIN club ON jugadores.id_club = club.id_club


SELECT 
jugadores.nombre AS 'Nombre del Jugador',
jugadores.apellidos AS 'Apellidos',
club.nombre AS 'Equipo',
club.victorias AS 'Victorias de su equipo'
FROM jugadores
LEFT JOIN club ON jugadores.id_club = club.id_club
ORDER BY club.victorias DESC;