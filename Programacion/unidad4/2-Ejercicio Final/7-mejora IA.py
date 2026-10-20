import os

# --- Función para limpiar la pantalla (mejora estética) ---
def limpiar_pantalla():
    # Detecta si es Windows ('nt') o Mac/Linux para usar el comando correcto
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# ==========================================
# DEFINICIÓN DE CLASES
# ==========================================

# CREO LA CLASE MADRE PILOTO
class Piloto():
    def __init__(self, nombre, apellidos, edad):        
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

# CREO LAS CLASES HIJAS PILOTO F1 Y PILOTO F2
class PilotoF1(Piloto):
    def __init__(self, nombre, apellidos, edad, escuderia, dorsal): 
        super().__init__(nombre, apellidos, edad)
        self.escuderia = escuderia
        self.dorsal = dorsal

    def listar(self):                                               
        print(f"🏎️  F1 | {self.nombre} {self.apellidos} | Edad: {self.edad} | Escudería: {self.escuderia} | Dorsal: {self.dorsal}") 

class PilotoF2(Piloto):
    def __init__(self, nombre, apellidos, edad, academia):  
        super().__init__(nombre, apellidos, edad)
        self.academia = academia

    def listar(self):                       
        print(f"🏁 F2 | {self.nombre} {self.apellidos} | Edad: {self.edad} | Academia: {self.academia}")    

# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

lista_de_pilotos = []    # CREO UNA LISTA VACIA PARA ALMACENAR LOS PILOTOS

limpiar_pantalla()
print("="*40)
print(" 🏎️  APLICACIÓN GESTIÓN DE PILOTOS v.02 🏁")
print("               por Fernando Puig")
print("="*40)

while True:             
    print("\n" + "="*30)
    print("           MENÚ PRINCIPAL")
    print("="*30)
    print(" [1] Insertar un nuevo Piloto")
    print(" [2] Listar Pilotos")
    print(" [3] Salir del programa")
    print("="*30)
    
    opcion = input("👉 Indica tu opción (1-3): ")

    # OPCION 1: INSERTAR UN PILOTO
    if opcion == "1":
        limpiar_pantalla()
        print("\n--- ➕ AÑADIR PILOTO ---")
        print(" [1] Piloto de F1")
        print(" [2] Piloto de F2")
        print(" [0] Cancelar")
        opcion_categoria = input("\nSelecciona la categoría: ")
        
        if opcion_categoria == "1":
            print("\n--- Datos del piloto de F1 ---")
            nombre = input("Nombre: ")
            apellidos = input("Apellidos: ")
            edad = input("Edad: ")
            escuderia = input("Escudería: ")
            dorsal = input("Dorsal: ")

            nuevo_piloto = PilotoF1(nombre, apellidos, edad, escuderia, dorsal)
            lista_de_pilotos.append(nuevo_piloto)
            print("\n✅ ¡Piloto de F1 guardado con éxito!")

        elif opcion_categoria == "2":
            print("\n--- Datos del piloto de F2 ---")
            nombre = input("Nombre: ")
            apellidos = input("Apellidos: ")
            edad = input("Edad: ")
            academia = input("Academia: ")

            nuevo_piloto = PilotoF2(nombre, apellidos, edad, academia)
            lista_de_pilotos.append(nuevo_piloto)
            print("\n✅ ¡Piloto de F2 guardado con éxito!")
            
        elif opcion_categoria == "0":
            print("\nVolviendo al menú principal...")
        else:
            print("\n❌ Opción no válida.")

    # OPCION 2: LISTAR LOS PILOTOS
    elif opcion == "2":
        limpiar_pantalla()
        print("\n--- 📋 MENÚ DE LISTADO ---")
        
        if len(lista_de_pilotos) == 0:
            print("⚠️ Todavía no hay pilotos registrados.")
        else:
            print(" [1] Listar SÓLO pilotos de F1")
            print(" [2] Listar SÓLO pilotos de F2")
            print(" [3] Listar TODOS los pilotos")
            opcion_listado = input("\n¿Qué deseas listar?: ")
            
            print("\n" + "-"*50)
            
            if opcion_listado == "1":
                print("           PILOTOS DE FÓRMULA 1")
                print("-" * 50)
                # Recorremos la lista y solo mostramos si el tipo de objeto es PilotoF1
                for piloto in lista_de_pilotos:
                    if isinstance(piloto, PilotoF1):
                        piloto.listar()
                        
            elif opcion_listado == "2":
                print("           PILOTOS DE FÓRMULA 2")
                print("-" * 50)
                # Recorremos la lista y solo mostramos si el tipo de objeto es PilotoF2
                for piloto in lista_de_pilotos:
                    if isinstance(piloto, PilotoF2):
                        piloto.listar()
                        
            elif opcion_listado == "3":
                print("        PARRILLA COMPLETA (F1 y F2)")
                print("-" * 50)
                # Recorremos la lista y mostramos todos, aprovechando el polimorfismo
                for piloto in lista_de_pilotos:     
                    piloto.listar()
                    
            else:
                print("❌ Opción de listado no válida.")
                
            print("-" * 50)

    # OPCION 3: SALIR
    elif opcion == "3":
        print("\n👋 ¡Gracias por usar la aplicación de gestión de pilotos! Cerrando...")
        break # Esto rompe el bucle while True y termina el programa
        
    else:
        print("\n❌ Opción incorrecta. Por favor, elige 1, 2 o 3.")