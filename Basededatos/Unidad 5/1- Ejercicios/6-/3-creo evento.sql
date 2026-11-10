-- Activar el programador de eventos
SET GLOBAL event_scheduler = ON;

-- Eliminar el evento si ya existe
DROP EVENT IF EXISTS sincronizar_clientes;

-- Crear evento cada minuto
DELIMITER //

CREATE EVENT sincronizar_clientes
ON SCHEDULE EVERY 1 MINUTE
DO
BEGIN
    DELETE FROM clientescopia;

    INSERT INTO clientescopia
    SELECT * FROM clientes;
END //

DELIMITER ;
