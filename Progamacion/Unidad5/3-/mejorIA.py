import os

# Códigos ANSI para darle ese toque "hacker/neón"
C_VERDE = '\033[92m'
C_AMARILLO = '\033[93m'
C_AZUL = '\033[94m'
C_MAGENTA = '\033[95m'
C_CYAN = '\033[96m'
C_RESET = '\033[0m'
C_NEGRITA = '\033[1m'

# Función para limpiar la consola y que no se acumule el texto
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    limpiar_pantalla()
    # Cabecera to guapa
    print(f"{C_MAGENTA}{C_NEGRITA}")
    print(" 🎬 ========================================== 🎬 ")
    print("  🎞️       PROGRAMA EN AGENDA v0.1          🎞️  ")
    print("                por Fernando Puig                ")
    print(" 🎬 ========================================== 🎬 ")
    print(f"{C_RESET}")
    
    print(f"\n{C_CYAN}🌟 ESCOGE UNA OPCIÓN 🌟{C_RESET}")
    print(f"{C_AMARILLO}  [1]{C_RESET} ➕ Insertar una película")
    print(f"{C_AMARILLO}  [2]{C_RESET} 📋 Listado de películas")
    
    opcion = input(f"\n{C_VERDE}👉 Indica tu opción: {C_RESET}")
    
    if opcion == "1":
        limpiar_pantalla()
        print(f"{C_AZUL}✨ NUEVA PELÍCULA ✨{C_RESET}")
        print("-" * 25)
        # Ponemos el input del usuario en amarillo para que destaque
        nombre = input(f"🍿 Introduce un nombre: {C_AMARILLO}")
        print(f"{C_RESET}", end="")
        director = input(f"🎬 Introduce el director: {C_AMARILLO}")
        print(f"{C_RESET}", end="")
        año = input(f"📅 Introduce el año de estreno: {C_AMARILLO}")
        print(f"{C_RESET}", end="")
        genero= input(f"🎭 Introduce el género: {C_AMARILLO}")
        print(f"{C_RESET}", end="")
        
        archivo = open("peliculas.csv", 'a')
        archivo.write(nombre + "," + director + "," + año + "," + genero + "\n")
        archivo.close()
        
        print(f"\n{C_VERDE}✔️ ¡Película guardada con éxito!{C_RESET}")
        input(f"\n{C_AZUL}Pulsa ENTER para volver al menú...{C_RESET}")
        
    elif opcion == "2":
        limpiar_pantalla()
        print(f"{C_MAGENTA}🎬 TU COLECCIÓN DE PELÍCULAS 🎬{C_RESET}")
        print("=" * 65)
        try:
            archivo = open("peliculas.csv", 'r')
            lineas = archivo.readlines()
            for linea in lineas:
                # Separamos los datos por las comas para maquetarlos como una ficha
                datos = linea.strip().split(',')
                if len(datos) == 4:
                    print(f"📌 {C_AMARILLO}{datos[0]}{C_RESET} | 🎬 {datos[1]} | 📅 {datos[2]} | 🎭 {datos[3]}")
                else:
                    print(f"📌 {linea.strip()}")
            archivo.close()
        except FileNotFoundError:
            # Por si intentan listar antes de crear el archivo
            print(f"{C_AMARILLO}¡Vaya! Aún no tienes películas guardadas.{C_RESET}")
            
        print("=" * 65)
        input(f"\n{C_AZUL}Pulsa ENTER para volver al menú...{C_RESET}")
