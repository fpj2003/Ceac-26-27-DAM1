DELETE FROM vuelta WHERE id_sesion = 5;

DELETE FROM sesion WHERE id_piloto = 5;

DELETE FROM piloto WHERE id_piloto = 5;


--Consulta pedida a la IA para eliminar pilotos cuya media sea superior a 90.5
DELETE FROM piloto 
WHERE id_piloto IN (
    SELECT id_piloto FROM (
        SELECT p.id_piloto
        FROM piloto p
        LEFT JOIN sesion s ON p.id_piloto = s.id_piloto
        LEFT JOIN vuelta v ON s.id_sesion = v.id_sesion
        GROUP BY p.id_piloto
        HAVING AVG(v.tiempo_vuelta) > 90.500
    ) AS pilotos_a_borrar
);