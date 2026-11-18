Si quieres crear una página web simple ,de una manera ŕapida y eficiente este programa te puede servir.

Esta aplicación consiste en una chat con IA, en el que tu le pides la página que quieras e indicaciones para su diseño ,y este te la crea de manera que te permite elegir si quieres ver el código , o la página ejecutada ,de manera que puedas ver como ha quedado.

El programa consta de una interfaz web HTML ,con su estilo CSS, que recoge la petición del usuario. Esta petición es recogida mediante python y la librería flask, que permite poder pasar la información del HTML a python. Desde python con esa información recogida se le pasa a la IA. Mediante el uso de una base de datos SQLite , la respuesta de la IA se almacena ,gracias a la librería sqlite3 que permite conectarse, y luego se lanzara a la página HTML.

Respecto a la IA , he implementado de manera local el modelo qwen2.5-coder:1.5b, que esta entrenado para programar y se ajusta a mi memoria RAM. Para que la IA haga lo que quiero , se le pasa el prompt del usuario ,y ademas se le pasan otros prompts en los que se dice que genere un HTML, y como quiero que me de el código para luego poder ejecutarlo correctamente.

En conclusión , si quieres hacer un pagina web simple rápidamente ,este programa te será de gran ayuda.
