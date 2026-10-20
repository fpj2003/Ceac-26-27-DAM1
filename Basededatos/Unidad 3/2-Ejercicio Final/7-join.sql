SELECT 
jugadores.nombre AS 'Nombre ',
jugadores.apellidos AS 'Apellidos',
club.nombre AS 'Equipo'
FROM jugadores
LEFT JOIN club ON jugadores.id_club = club.id_club;