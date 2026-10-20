SELECT 
j.id_jugador,
j.nombre,
j.apellidos,
j.fecha_de_nacimiento,
j.posicion,
j.dorsal,
c.nombre AS nombre_del_club
FROM jugadores j
LEFT JOIN club c ON j.id_club = c.id_club;