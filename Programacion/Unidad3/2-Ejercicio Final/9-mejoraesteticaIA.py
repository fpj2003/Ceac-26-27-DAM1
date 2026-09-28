"""
Ejercicio Unidad 3 
Lista de Películas, Series y videojuegos (Versión Estética)
Fernando Puig
"""
import os # Importamos os para poder limpiar la pantalla

# DECLARACIÓN DE VARIABLES DE COLOR (Códigos ANSI)
CYAN = '\033[96m'
VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
MAGENTA = '\033[95m'
RESET = '\033[0m'
SEPARADOR = f"{CYAN}════════════════════════════════════════════════════{RESET}"

# DECLARACION DE LISTAS
Peliculas = []
Series = []
Videojuegos = []

# BUCLE PARA MANTENER EL PROGRAMA ACTIVO
while True:
    # Limpia la consola cada vez que carga el menú principal
    os.system('cls' if os.name == 'nt' else 'clear') 
    
    print(f"\n{CYAN}╔══════════════════════════════════════════════════╗{RESET}")
    print(f"{CYAN}║{RESET}       🎬 {AMARILLO}GESTOR DE ENTRETENIMIENTO{RESET} 🎮          {CYAN}║{RESET}")
    print(f"{CYAN}╚══════════════════════════════════════════════════╝{RESET}")
    print(f"  {VERDE}[ 1 ]{RESET} Insertar elemento")
    print(f"  {VERDE}[ 2 ]{RESET} Ver elementos")
    print(f"  {VERDE}[ 3 ]{RESET} Comprobar elementos")
    print(SEPARADOR)
    
    opcion = input(f"{MAGENTA}➤ Elija una opción: {RESET}")
            
    try:                                                                            
        opcion = int(opcion)                                                          
        
        # MENU DE LA OPCION DE INSERTAR
        if opcion == 1: 
            print(f"\n{CYAN}--- INSERTAR ELEMENTO ---{RESET}")                        
            print(f"  {VERDE}1.{RESET} Añadir película")
            print(f"  {VERDE}2.{RESET} Añadir serie")
            print(f"  {VERDE}3.{RESET} Añadir videojuegos")
            opcion_insertar = input(f"{MAGENTA}➤ Elija el elemento a añadir: {RESET}")                     
            opcion_insertar = int(opcion_insertar)
            
            if opcion_insertar == 1:
                peli = input(f"{AMARILLO}Indica el nombre de la película a añadir: {RESET}")                
                Peliculas.append(peli)   
                print(f"{VERDE}✔ ¡Película '{peli}' añadida con éxito!{RESET}")
            elif opcion_insertar == 2:
                serie = input(f"{AMARILLO}Indica el nombre de la serie a añadir: {RESET}")                
                Series.append(serie)
                print(f"{VERDE}✔ ¡Serie '{serie}' añadida con éxito!{RESET}")
            elif opcion_insertar == 3:                          
                videojuego = input(f"{AMARILLO}Indica el nombre del videojuego a añadir: {RESET}")
                Videojuegos.append(videojuego)
                print(f"{VERDE}✔ ¡Videojuego '{videojuego}' añadido con éxito!{RESET}")
            else:
                assert 4 < 3                                                        
            
            input(f"\n{MAGENTA}Presione ENTER para volver al menú...{RESET}")

        # MENU DE LA OPCION DE LISTAR
        elif opcion == 2:                                   
            print(f"\n{CYAN}--- LISTAR ELEMENTOS ---{RESET}")                        
            print(f"  {VERDE}1.{RESET} Ver las películas")
            print(f"  {VERDE}2.{RESET} Ver las series")
            print(f"  {VERDE}3.{RESET} Ver los videojuegos")
            print(f"  {VERDE}4.{RESET} Ver todos los elementos")
            opcion_ver = input(f"{MAGENTA}➤ Elija el elemento a ver: {RESET}")
            opcion_ver = int(opcion_ver)
            
            print(SEPARADOR)
            if opcion_ver == 1:                     
                print(f"{AMARILLO}Listado de Peliculas:{RESET}")
                print(f"🍿 {Peliculas}")                                                    
            elif opcion_ver == 2:
                print(f"{AMARILLO}Listado de Series:{RESET}")
                print(f"📺 {Series}")                                                       
            elif opcion_ver == 3:
                print(f"{AMARILLO}Listado de Videojuegos:{RESET}")
                print(f"🕹️ {Videojuegos}")                                                  
            elif opcion_ver == 4:
                print(f"{AMARILLO}Listado Completo:{RESET}")               
                print(f"🍿 Películas:   {Peliculas}")
                print(f"📺 Series:      {Series}")
                print(f"🕹️ Videojuegos: {Videojuegos}")
            else:
                assert 4 < 3    
                
            input(f"\n{MAGENTA}Presione ENTER para volver al menú...{RESET}")

        # MENU DE LA OPCION DE COMPROBAR 
        elif opcion == 3:
            print(f"\n{CYAN}--- COMPROBAR ELEMENTOS ---{RESET}")                        
            print(f"  {VERDE}1.{RESET} Comprobar película")
            print(f"  {VERDE}2.{RESET} Comprobar series")
            print(f"  {VERDE}3.{RESET} Comprobar videojuegos")
            opcion_comprobar = input(f"{MAGENTA}➤ Elija el elemento a comprobar: {RESET}")
            opcion_comprobar = int(opcion_comprobar)
            
            if opcion_comprobar == 1:
                comparador_pelicula = input(f"{AMARILLO}Introduce la película a comparar: {RESET}")
                existe_pelicula = False                                               
                for i in range(len(Peliculas)):                                     
                    if Peliculas[i] == comparador_pelicula:                         
                        existe_pelicula = True                                        
                if existe_pelicula == True:                                         
                    print(f"{VERDE}✔ La película YA ESTÁ en la lista.{RESET}")
                else:                                                              
                    print(f"{ROJO}✖ La película NO ESTÁ en la lista.{RESET}")                        
            elif opcion_comprobar == 2:                                             
                comparador_serie = input(f"{AMARILLO}Introduce la serie a comparar: {RESET}")
                existe_serie = False
                for i in range(len(Series)):
                    if Series[i] == comparador_serie:
                        existe_serie = True
                if existe_serie == True:
                    print(f"{VERDE}✔ La serie YA ESTÁ en la lista.{RESET}")
                else:
                    print(f"{ROJO}✖ La serie NO ESTÁ en la lista.{RESET}")
            elif opcion_comprobar == 3:
                comparador_videojuego = input(f"{AMARILLO}Introduce el videojuego a comparar: {RESET}")
                existe_videojuego = False
                for i in range(len(Videojuegos)):
                    if Videojuegos[i] == comparador_videojuego:
                        existe_videojuego = True
                if existe_videojuego == True:
                    print(f"{VERDE}✔ El videojuego YA ESTÁ en la lista.{RESET}")
                else:
                    print(f"{ROJO}✖ El videojuego NO ESTÁ en la lista.{RESET}")     
            else:
                assert 4 < 3
                
            input(f"\n{MAGENTA}Presione ENTER para volver al menú...{RESET}")
            
        else:
            assert 4 < 3            
            
    except Exception as e:
        print(f"\n{ROJO}╔══════════════════════════════════════════════════╗{RESET}")
        print(f"{ROJO}║  ⚠️  OPCIÓN NO VÁLIDA - VUELVA A INTENTARLO  ⚠️  ║{RESET}")    
        print(f"{ROJO}╚══════════════════════════════════════════════════╝{RESET}")
        input(f"\n{MAGENTA}Presione ENTER para volver al menú...{RESET}")