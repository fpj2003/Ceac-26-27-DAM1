
-- Crear base de datos
CREATE DATABASE IF NOT EXISTS empresa
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Seleccionar base de datos
USE empresa;

-- Crear tabla clientes
CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellidos VARCHAR(150) NOT NULL,
    email VARCHAR(150) UNIQUE,
    telefono VARCHAR(20),
    direccion VARCHAR(200),
    ciudad VARCHAR(100),
    provincia VARCHAR(100),
    codigo_postal VARCHAR(10),
    fecha_nacimiento DATE,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    activo BOOLEAN DEFAULT TRUE
);

-- Insertar datos de demostración
INSERT INTO clientes (
    nombre, apellidos, email, telefono,
    direccion, ciudad, provincia,
    codigo_postal, fecha_nacimiento, activo
) VALUES
('Juan', 'García López', 'juan.garcia@example.com',
 '612345678', 'Calle Mayor 15', 'Valencia',
 'Valencia', '46001', '1985-03-12', 1),

('María', 'Martínez Pérez', 'maria.martinez@example.com',
 '623456789', 'Avenida del Puerto 42', 'Valencia',
 'Valencia', '46021', '1990-07-25', 1),

('Pedro', 'Sánchez Ruiz', 'pedro.sanchez@example.com',
 '634567890', 'Calle Colón 8', 'Madrid',
 'Madrid', '28001', '1978-11-04', 1),

('Ana', 'Fernández Gómez', 'ana.fernandez@example.com',
 '645678901', 'Gran Vía 23', 'Madrid',
 'Madrid', '28013', '1995-01-18', 1),

('Carlos', 'Rodríguez Díaz', 'carlos.rodriguez@example.com',
 '656789012', 'Calle Aragón 56', 'Barcelona',
 'Barcelona', '08009', '1982-09-30', 1),

('Laura', 'López Hernández', 'laura.lopez@example.com',
 '667890123', 'Paseo de Gracia 101', 'Barcelona',
 'Barcelona', '08008', '1988-05-14', 1),

('Miguel', 'González Torres', 'miguel.gonzalez@example.com',
 '678901234', 'Calle Sierpes 12', 'Sevilla',
 'Sevilla', '41004', '1975-12-08', 1),

('Lucía', 'Pérez Navarro', 'lucia.perez@example.com',
 '689012345', 'Avenida Constitución 34', 'Sevilla',
 'Sevilla', '41001', '1998-04-22', 1),

('David', 'Romero Castillo', 'david.romero@example.com',
 '690123456', 'Calle Larios 7', 'Málaga',
 'Málaga', '29005', '1987-06-11', 1),

('Elena', 'Jiménez Morales', 'elena.jimenez@example.com',
 '601234567', 'Calle Nueva 19', 'Málaga',
 'Málaga', '29008', '1992-10-03', 1),

('Javier', 'Ruiz Ortega', 'javier.ruiz@example.com',
 '611223344', 'Calle Alfonso I 22', 'Zaragoza',
 'Zaragoza', '50003', '1980-02-17', 1),

('Carmen', 'Díaz Serrano', 'carmen.diaz@example.com',
 '622334455', 'Paseo Independencia 45', 'Zaragoza',
 'Zaragoza', '50001', '1993-08-09', 1),

('Sergio', 'Moreno Vega', 'sergio.moreno@example.com',
 '633445566', 'Calle San Vicente 14', 'Alicante',
 'Alicante', '03004', '1984-05-27', 1),

('Paula', 'Álvarez Molina', 'paula.alvarez@example.com',
 '644556677', 'Avenida Maisonnave 28', 'Alicante',
 'Alicante', '03003', '1997-12-15', 1),

('Raúl', 'Torres Campos', 'raul.torres@example.com',
 '655667788', 'Calle Trapería 9', 'Murcia',
 'Murcia', '30001', '1979-03-06', 1),

('Isabel', 'Vázquez Flores', 'isabel.vazquez@example.com',
 '666778899', 'Gran Vía 51', 'Murcia',
 'Murcia', '30004', '1991-09-21', 1),

('Alberto', 'Castro Medina', 'alberto.castro@example.com',
 '677889900', 'Calle Uría 33', 'Oviedo',
 'Asturias', '33003', '1986-07-13', 1),

('Natalia', 'Herrera León', 'natalia.herrera@example.com',
 '688990011', 'Calle Corrida 17', 'Gijón',
 'Asturias', '33206', '1994-11-29', 1),

('Fernando', 'Ramos Iglesias', 'fernando.ramos@example.com',
 '699001122', 'Calle Gran Vía 65', 'Bilbao',
 'Bizkaia', '48011', '1981-01-10', 0),

('Patricia', 'Gil Santos', 'patricia.gil@example.com',
 '600112233', 'Avenida Libertad 20', 'San Sebastián',
 'Gipuzkoa', '20004', '1996-06-02', 1);

-- Consultar todos los clientes
SELECT * FROM clientes;

-- Contar clientes
SELECT COUNT(*) AS total_clientes FROM clientes;

