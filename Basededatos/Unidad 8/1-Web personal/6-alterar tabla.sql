ALTER TABLE proyectos
ADD enlace VARCHAR(255);

UPDATE proyectos SET enlace = 'https://github.com/fpj2003/Ceac-26-27-DAM1/blob/main/Programacion/Unidad1/Proyecto/esteticaIA.py' WHERE id = 1;
UPDATE proyectos SET enlace = 'https://github.com/fpj2003/Ceac-26-27-DAM1/blob/main/Programacion/Unidad3/2-Ejercicio%20Final/8-assert.py' WHERE id = 2;
UPDATE proyectos SET enlace = 'https://github.com/fpj2003/Ceac-26-27-DAM1/blob/main/Programacion/unidad4/2-Ejercicio%20Final/6-comentarios.py' WHERE id = 3;
UPDATE proyectos SET enlace = 'https://github.com/fpj2003/Ceac-26-27-DAM1/blob/main/Programacion/Unidad5/2-Ejercicio%20Final/8-grid.py' WHERE id = 4;

     
