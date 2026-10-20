SELECT * FROM piloto

--Selecionar la fecha de la sesión junto al nombre y apellidso del piloto
SELECT 
p.nombre, 
p.apellidos, 
s.fecha AS 'Fecha de la sesion' 
FROM piloto p
LEFT JOIN sesion s ON p.id_piloto = s.id_piloto;

--Seleccionar el nombre y apellido del piloto junto a sus vueltas de la sesión
SELECT 
p.nombre AS 'Nombre',
p.apellidos AS 'Apellidos',
v.numero_vuelta AS  'Numero de vuelta',
v.tiempo_vuelta AS 'Timepo de la vuelta'
FROM piloto p
LEFT JOIN sesion s ON p.id_piloto = s.id_piloto
LEFT JOIN vuelta v ON s.id_sesion = v.id_sesion
ORDER BY p.nombre ASC, v.numero_vuelta ASC;


--Ordenar a los pilotos por el tiempo de media de sus vueltas
SELECT 
p.nombre, 
p.apellidos, 
AVG(v.tiempo_vuelta) AS Tiempo_de_vuelta_medio
FROM piloto p
LEFT JOIN sesion s ON p.id_piloto = s.id_piloto
LEFT JOIN vuelta v ON s.id_sesion = v.id_sesion
GROUP BY p.id_piloto
ORDER BY Tiempo_de_vuelta_medio ASC;