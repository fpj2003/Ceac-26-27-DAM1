a) Se ha analizado el formato de almacenamiento de la información.
He analizado la información y he creado una base de datos con dos tablas para dividir la información entre jugadores y club.

b) Se han creado las tablas y las relaciones entre ellas.
He creado las dos tablas con CREATE TABLE y las he relacionado entre ellas a través de añadir id_club en la tabla jugadores como clave ajena.

c) Se han seleccionado los tipos de datos adecuados.
He usado para números enteros como dorsales un INT, para fechas, como la fecha de nacimiento en jugadores, DATE y para las demás filas que eran de cadena de texto como VARCHAR, dándoles una capacidad de 100.

d) Se han definido los campos clave en las tablas.
He creado en cada tabla una clave primaria como lo son id_jugador e id_club, y son una clave que se va incrementando automáticamente para cada registro, de manera que cada fila tenga una diferente y no se repita.

e) Se han implantado las restricciones reflejadas en el diseño lógico.
He añadido restricciones con el CHECK para el campo de email, de manera que se inserte un email válido.

f) Se han creado vistas.
He creado vistas a través de consultas JOIN, que unen datos de las dos tablas juntándose con el id_club.

g) Se han creado los usuarios y se les han asignado privilegios.
He creado un usuario llamado basefutbol, al cual le he asignado privilegios para poder acceder a la base de datos.

h) Se han utilizado asistentes, herramientas gráficas y los lenguajes de definición y control de datos.
He ido escribiendo el código sql en archivos en GEDIT y luego los he ejecutado en mySQL.