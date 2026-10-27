CREATE DATABASE blogceacdam2627;
USE blogceacdam2627;

CREATE TABLE articulos(
id INT AUTO_INCREMENT PRIMARY KEY,
titulo VARCHAR(100),
fecha DATE,
contenido TEXT
);


INSERT INTO articulos (titulo, fecha, contenido) VALUES 
('Programa 1: Calculadora de Viajes', '2026-01-15', 'Un programa muy útil que he escrito en Python. El usuario introduce el origen, el destino y el consumo de su coche, y el script calcula la distancia y estima el coste total del viaje en gasolina, incluyendo posibles peajes.'),
('Programa 2: Generador de Contraseñas Seguras', '2026-01-28', 'He desarrollado un pequeño script en JavaScript que genera contraseñas aleatorias de 16 caracteres. Mezcla mayúsculas, minúsculas, números y símbolos especiales, asegurando que tus cuentas estén protegidas contra ataques de fuerza bruta.'),
('Programa 3: Temporizador Pomodoro', '2026-02-10', 'Una aplicación web sencilla que sirve para mejorar la productividad. El temporizador alterna automáticamente bloques de 25 minutos de trabajo concentrado con pausas de 5 minutos, emitiendo un pequeño pitido al terminar cada ciclo.'),
('Programa 4: Calculadora de Índice de Masa Corporal (IMC)', '2026-02-22', 'Un formulario interactivo donde introduces tu peso en kilos y tu altura en metros. El programa realiza la operación matemática del IMC y te muestra un mensaje indicando si estás en un rango de peso saludable según los estándares médicos.'),
('Programa 5: Juego "Adivina el Número"', '2026-03-05', 'He programado un minijuego clásico para jugar desde la consola. El ordenador escoge un número aleatorio del 1 al 100 y tienes cinco intentos para adivinarlo. Después de cada intento, el programa te da pistas diciendo si es "mayor" o "menor".'),
('Programa 6: Gestor de Tareas (To-Do List)', '2026-03-20', 'Una lista de tareas minimalista que he montado con HTML y JS. Puedes añadir quehaceres diarios, marcarlos como completados o borrarlos. Lo mejor es que utiliza el almacenamiento local del navegador para no perder los datos al recargar la página.'),
('Programa 7: Contador de Palabras y Caracteres', '2026-04-02', 'Una herramienta ideal para escritores y estudiantes. Pegas un texto en la caja de texto y el programa actualiza en tiempo real cuántas palabras, caracteres (con y sin espacios) y párrafos tiene el documento.'),
('Programa 8: Generador de Paletas de Colores', '2026-04-18', 'Al pulsar la barra espaciadora en esta página, mi nuevo algoritmo genera de forma aleatoria cinco códigos de colores en formato Hexadecimal que combinan bien entre sí. Es perfecto para buscar inspiración al diseñar páginas web.'),
('Programa 9: Simulador de Tirada de Dados para Rol', '2026-05-01', 'Un simulador de dados virtuales pensado para jugar a Dungeons & Dragons. El programa permite seleccionar dados de 4, 6, 8, 10, 12 y 20 caras, tira varios a la vez y suma automáticamente todos los resultados y modificadores.'),
('Programa 10: Conversor a Código Morse', '2026-05-15', 'Un divertido script de traducción. Tú escribes una frase normal y el programa convierte el texto a la clásica secuencia de puntos y rayas del código Morse. Además, he añadido un botón para que reproduzca el sonido correspondiente.'),
('Programa 11: Calculadora de Propinas', '2026-06-03', 'Una utilidad muy práctica para cuando sales a cenar con amigos. Pones el total de la cuenta, eliges el porcentaje de propina que quieres dejar, le dices cuántas personas sois y el programa te dice exactamente cuánto debe pagar cada uno.'),
('Programa 12: Generador de Códigos QR', '2026-06-20', 'Usando una librería externa, he creado una herramienta donde pegas cualquier enlace web o texto plano y automáticamente dibuja un Código QR. Después puedes hacer clic en un botón para descargarlo como imagen PNG en tu ordenador.'),
('Programa 13: Rastreador de Consumo de Agua', '2026-07-08', 'Una sencilla aplicación visual para mantenerte hidratado. Muestra un vaso de agua en la pantalla y cada vez que bebes y haces clic, el nivel sube, ayudándote a llevar la cuenta hasta llegar al objetivo de dos litros diarios.'),
('Programa 14: Reloj Mundial Multizona', '2026-07-22', 'Un panel que sincroniza diferentes zonas horarias. El programa muestra cuatro relojes digitales actualizándose al segundo: uno para València, otro para Nueva York, otro para Tokio y un último para Sídney, calculando los desfases horarios automáticamente.'),
('Programa 15: Generador de Excusas Aleatorias', '2026-08-10', 'Un proyecto hecho por pura diversión. El programa tiene tres listas de palabras y frases distintas. Al pulsar un botón, selecciona un elemento de cada lista al azar y forma una excusa absurda pero gramaticalmente correcta por si llegas tarde a algún sitio.'),
('Programa 16: Conversor de Markdown a HTML', '2026-08-25', 'He programado un editor web dividido en dos columnas. Escribes texto utilizando formato Markdown a la izquierda (como asteriscos para negritas o almohadillas para títulos) y el programa renderiza el código HTML formateado en tiempo real a la derecha.'),
('Programa 17: Extraedor de Colores de Imágenes', '2026-09-05', 'Una aplicación de procesamiento de imágenes básica. Subes una fotografía desde tu disco duro, y el algoritmo lee los píxeles utilizando un Canvas de HTML5 para devolverte una paleta con los tres colores que más se repiten en esa imagen.'),
('Programa 18: Cronómetro y Vuelta a Vuelta', '2026-09-18', 'Un cronómetro digital preciso hasta los milisegundos. Además del botón de iniciar, pausar y reiniciar, el programa tiene una función de "Lap" (Vuelta) que permite registrar los tiempos parciales en una lista abajo sin detener la cuenta principal.'),
('Programa 19: Mezclador de Sonidos de Concentración', '2026-10-02', 'Una interfaz con tres controles deslizantes que manejan el volumen de diferentes audios: lluvia, crepitar de una chimenea y viento. El programa te permite mezclar los tres sonidos a tu gusto para crear el ruido blanco perfecto para estudiar o programar.'),
('Programa 20: Conversor de Monedas Básico', '2026-10-26', 'He cerrado el mes programando un conversor de divisas. Tiene valores de conversión fijos en el código (euros a dólares y libras). Introduces una cantidad en una caja, seleccionas la moneda en un menú desplegable y te devuelve el equivalente calculado instantáneamente.');



CREATE USER 'blogceacdam2627'@'localhost' IDENTIFIED BY 'Ceac123$';


GRANT USAGE ON *.* TO 'blogceacdam2627'@'localhost';


ALTER USER 'blogceacdam2627'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;



GRANT ALL PRIVILEGES ON blogceacdam2627.* 
TO 'blogceacdam2627'@'localhost';

FLUSH PRIVILEGES;

