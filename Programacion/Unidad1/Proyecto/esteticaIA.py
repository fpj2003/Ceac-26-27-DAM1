"""
Ejercicio Unidad 1
Calculadora de precio de un viaje
Fernando Puig *
"""
import os

# DEFINICIÓN DE COLORES (Códigos ANSI para terminal)
C_TITULO = '\033[1;95m'  # Magenta negrita
C_INFO = '\033[96m'      # Cian
C_PREGUNTA = '\033[93m'  # Amarillo
C_EXITO = '\033[1;92m'   # Verde negrita
C_LINEA = '\033[90m'     # Gris oscuro
C_RESET = '\033[0m'      # Resetear color

def separador():
    """Imprime una línea visual separadora"""
    print(f"{C_LINEA}═" * 65 + f"{C_RESET}")

# LIMPIEZA DE PANTALLA SEGÚN SISTEMA OPERATIVO
os.system('cls' if os.name == 'nt' else 'clear')

# BIENVENIDA AL PROGRAMA Y ENTRADA DE INFORMACIÓN
separador()
print(f"{C_TITULO}🚗 CALCULADORA DE GASTOS DE VIAJE 🚗{C_RESET}".center(75))
separador()
print(f"{C_INFO}Bienvenido. Por favor, introduzca los datos de su ruta:{C_RESET}\n")

# Se añaden iconos, colores y un símbolo " > " para dejar claro dónde escribir
kilometros = input(f" {C_PREGUNTA}[?] Kilómetros totales del viaje: {C_RESET}> ")
consumo = input(f" {C_PREGUNTA}[?] Consumo del vehículo (L/100 km): {C_RESET}> ")
precio = input(f" {C_PREGUNTA}[?] Precio por litro de combustible (€): {C_RESET}> ")
pasajeros = input(f" {C_PREGUNTA}[?] Número de pasajeros que viajan: {C_RESET}> ")
print()

# CONVERTIR LAS VARIABLES A LAS NECESARIAS PARA OPERAR
kilometros = int(kilometros)			
consumo = float(consumo)		
precio = float(precio)		
pasajeros = int(pasajeros)	

# OPERACIONES DE CÁLCULO
CIEN_KM = 100														
precio_final = (kilometros * consumo / CIEN_KM) * precio	
precio_pasajero = precio_final / pasajeros			

# SALIDA DE INFORMACIÓN (FORMATEADA A 2 DECIMALES)
separador()
print(f"{C_TITULO}🧾 RESUMEN DE GASTOS 🧾{C_RESET}".center(75))
separador()

# Se utiliza f-strings para formatear a 2 decimales (.2f) y alinear los textos
print(f" {C_EXITO}➜ Precio total del viaje:{C_RESET}       {precio_final:.2f} €")
print(f" {C_EXITO}➜ Precio por cada pasajero:{C_RESET}     {precio_pasajero:.2f} €")
separador()
print(f"{C_INFO}¡Buen viaje!{C_RESET}".center(75) + "\n")
