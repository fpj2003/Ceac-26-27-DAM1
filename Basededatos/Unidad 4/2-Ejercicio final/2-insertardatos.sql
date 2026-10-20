
INSERT INTO piloto (nombre, apellidos, fecha_de_nacimiento, email) 
VALUES 
('Fernando', 'Alonso Díaz', '1981-07-29', 'fernando.alonso@ejemplo.com'),
('Carlos', 'Sainz Vázquez de Castro', '1994-09-01', 'carlos.sainz@ejemplo.com'),
('Pedro', 'Martínez de la Rosa', '1971-02-24', 'pedro.delarosa@ejemplo.com'),
('Marc', 'Gené Guerrero', '1974-03-29', 'marc.gene@ejemplo.com'),
('Jaime', 'Alguersuari Escudero', '1990-03-23', 'jaime.alguersuari@ejemplo.com');

INSERT INTO sesion (id_piloto, fecha) 
VALUES 
(1, '2023-10-01'), 
(2, '2023-10-01'), 
(3, '2023-10-02'), 
(4, '2023-10-02'), 
(5, '2023-10-03'); 

INSERT INTO vuelta (id_sesion, numero_vuelta, tiempo_vuelta) VALUES 
(1, 1, 90.250),
(1, 2, 89.800),
(1, 3, 89.500),
(1, 4, 90.100),
(1, 5, 89.900),
(2, 1, 91.000),
(2, 2, 90.500),
(2, 3, 89.900),
(2, 4, 90.200),
(2, 5, 89.700),
(3, 1, 90.800),
(3, 2, 90.100),
(3, 3, 90.400),
(3, 4, 89.900),
(3, 5, 89.600),
(4, 1, 91.200),
(4, 2, 90.700),
(4, 3, 90.300),
(4, 4, 91.500),
(4, 5, 89.800),
(5, 1, 90.500),
(5, 2, 90.000),
(5, 3, 89.400),
(5, 4, 89.800),
(5, 5, 90.100);