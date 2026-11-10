4 bloques:
1.-1 párrafo con una introducción: comenta qué es lo que vas a presentar, por qué, para qué, a quién sirve, para qué sirve, etc

2.-1-2 párrafos para explicar qué has hecho, qué ha decidido hacer, para qué sirve al mundo lo que has decidido hacer (pero con mas profunidad que en la introducción), resumen del stack tecnológico que has usado, y por qué)

3.-1-2 párrafos explicando los detalles tecnológicos de qué has hecho, que tipo de tecnologías has usado, como se combinan, incluso qué instrucciones has usado

4.-1 párrafo: Conclusión, finalización, resumen, cierre, una despedida, un resumen de lo que se ha presentado para "cerar bonito"


Este es un programa que a traves de una IA ,puede generar páginas web según los prompts que tu le des.

Este programa integra una IA local , de manera que se ejecuta desde el propio equipo ,y el usuario pueda pedirle que le haga una paǵina web en html, sobre lo que el quiera, y el programa te la crea y te la muestra 

Para la realización del programa , he usado distintas tecnologías ,en primer lugar, la parte visible ,esta hecha con html y css , donde el usuario le pide lo que quiere a la IA, una el usuario realiza esa petición, esta es recibida por python a través de flask y la guarda.Una vez guardada , desde el propio pyhton pasa esa petición a la IA , esta le devuelve el codigo de esa petición, y una vez recibido lo guarda en una base de datos SQL. En cuanto se guarda ,se recorre ahora el mismo camino pero a la inversa , para mostrar ese codigo guardado en la base de datos ,y se muestre en html, y el usuario pueda ver ya su web que ha pedido.

A través de 



