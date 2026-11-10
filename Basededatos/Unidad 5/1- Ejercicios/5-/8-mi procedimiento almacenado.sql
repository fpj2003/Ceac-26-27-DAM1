SELECT * FROM clientes;

SELECT * FROM clientes
WHERE codigo_postal < 30000;

def dameCodig(codigo):
	SELECT * FROM clientes
	WHERE codigo_postal < codigo;
  
DELIMITER //

CREATE PROCEDURE dameCodigo(IN codigo INT)
BEGIN
    SELECT *
    FROM clientes
    WHERE codigo_postal < codigo;
END //

DELIMITER ;
