SELECT 
    posicion, 
    COUNT(id_jugador) AS 'Número de jugadores por posición'
FROM jugadores
GROUP BY posicion;

SELECT 
    posicion, 
    SUM(goles) AS 'Goles marcados por posición'
FROM jugadores
GROUP BY posicion;