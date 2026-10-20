SELECT 
nombre,
apellidos,
goles,
goles > (
    SELECT AVG(goles) FROM jugadores
    ) AS 'Superior a la media '
FROM jugadores;