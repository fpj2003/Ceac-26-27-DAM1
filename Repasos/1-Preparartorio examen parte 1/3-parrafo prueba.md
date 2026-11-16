Cuando un programador este diseñando un programa ,el momento de pensar las consultas a su bases de datos ,a veces se pueden complicar un poco y que se emplee deemasiado tiempo en ello, pero con este progrmama te puede ahorrar timepo 


El programa consiste en un chat con IA en el que le puedes pedir que te haga consultas sql para tu base de datos y este te saca la sentencia y el resultado de ella sobre tu base de datos, de manera que no haga falta que copies la sentencia y la ejecutes en tu programa de base de datos y puedas ver si esa sentencia es la que necesitas para tu tarea

El programa consta de una interfaz web ,creada con html , y su estilo visual, creado con css, la cual recoge la peticion del usuario a traves del chat. Una vez recogida esta peticion , llega a python mediante la libreria flask ,que se encarga de conectar con el documento html, y se la pasa una IA local. La IA usada es duckdb-nsql, una IA especializada en sql.Cuando la IA finaliza su pensamiento , su respuesta es recogida por python y conecta con la base de datos y aplica este sentencia ,recogeidno el resultado de esta , y se la lanza al documento html para mostrarsela al usuario

Por lo tanto , si quieres poder realizar consultas sql de una manera rapida y eficiente ,este chat puede ser una gran solución
