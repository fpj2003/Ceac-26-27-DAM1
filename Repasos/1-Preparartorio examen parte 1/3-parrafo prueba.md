Cuando un programador este diseñando un programa ,el momento de pensar las consultas a su bases de datos ,a veces se pueden complicar un poco y que se emplee demasiado tiempo en ello, pero este programa te puede ahorrar tiempo


El programa consiste en un chat con IA en el que le puedes pedir que te haga consultas SQL para tu base de datos y este te saca la sentencia y el resultado de ella sobre tu base de datos, de manera que no haga falta que copies la sentencia y la ejecutes en tu programa de base de datos y puedas ver si esa sentencia es la que necesitas para tu tarea.

El programa consta de una interfaz web ,creada con HTML , y su estilo visual, creado con CSS, la cual recoge la petición del usuario a través del chat. Para lanzar el documento HTML y recibir la información ,he usado python con la librería flask. Para poder conectarme a la base de datos sobre la cual se quiere trabajar y aplicar la sentencia que devuelva la IA ,he usado la librería sqlite3.

Respecto a la IA implementada, he integrado localmente la IA duckdb-nsql, porque esta especializada en lenguaje SQL y se ajusta a la memoria RAM que tengo. Para que esta solo me devuelva la sentencia SQL , le doy una serie de prompts indicándole que solo quiero la sentencia sin nada más y además le doy la estructura de las tablas de la base de datos , para que sepa como esta desarrollada.


Por lo tanto , si quieres poder realizar consultas SQL de una manera rápida y eficiente ,este chat puede ser una gran solución.
