DELIMITER //

CREATE TRIGGER borrar_direccion
BEFORE UPDATE ON clientes
FOR EACH ROW
BEGIN
    IF NOT (OLD.telefono <=> NEW.telefono) THEN
        SET NEW.direccion = NULL;
    END IF;
END //

DELIMITER ;
