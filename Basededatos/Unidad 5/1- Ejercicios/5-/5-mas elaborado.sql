SELECT
    nombre,
    apellidos,
    IF(ciudad = 'Bilbao', ciudad, NULL) AS ciudad,
    IF(ciudad = 'Bilbao', telefono, NULL) AS telefono
FROM clientes;
