
def cazadores_de_gramatica():
    from juegos.utilidades.funciones_CDG import leer_archivo
    from juegos.utilidades.funciones_CDG import comparacion_oraciones
    from juegos.utilidades.funciones_CDG import comparacion_sustantivos
    from juegos.utilidades.funciones_CDG import comparacion_verbos
    from juegos.utilidades.funciones_CDG import comparacion_adjetivos
    from juegos.utilidades.inicio_CDG import incio_CDG
    import random # Libreria "random" para poder obtener oraciones aleatorias de la lista "oraciones"

    #Codigo ANSI de diferentes modos para decorar texto
    BOLD = '\033[1m'       
    ITALIC = '\033[3m' 
    DARKCYAN = '\033[36m'    
    RED = '\033[91m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    END = '\033[0m'      

    #Presentación del juego + instrucciones

    incio_CDG()  

    #Inicio de variables
    oraciones = []
    puntuacion = 0                                                                                           

    leer_archivo(oraciones) 
                                  
    indices_aleatorios = random.sample(range(len(oraciones)), 5)

    j = 0    #Contador de oraciones de pantalla jugador
    for i in indices_aleatorios:

        print(f"{YELLOW}{BOLD}{j + 1} Oración a corregir:{END}", oraciones[i]["incorrecta"]) # Imprimo en pantalla oración aleatoria a corregir

        intentos = 2
        while intentos > 0:

            oracion_player = input(f"{YELLOW}{BOLD}Jugador: {END}")
                
                #Acá comparo el largo de la oración ingresada por el jugador por si se hace el vivo y quiere usar menos palabras de las que debe.
            if len(oracion_player.split()) != len(oraciones[i]["correcta"].split()):
                intentos -= 1
                if intentos > 0:
                    print("\n", f"{RED}La cantidad de palabras no coinciden. Inténtalo de nuevo.{END}")
                else:
                    print("\n", f"{RED}Dejaste escapar esta oración.{END}")
                    break
            else:
                
                errores = comparacion_oraciones(oracion_correcta=oraciones[i]["correcta"], oracion_player=oracion_player)
                    
                if errores == 0:
                    print("\n","\n", f"Felicitaciones!{GREEN} Oración perfecta.{END} Obtuviste 100 puntos.")
                    puntuacion += 100
                elif errores == 1:
                    print("\n", "\n", "Ups! Tuviste ", f"{RED}{errores}{END}", ". Obtuviste 90 puntos.")
                    puntuacion += 90
                elif errores == 2:
                    print("\n", "\n", "Ups! Tuviste ",f"{RED}{errores}{END}",". Obtuviste 70 puntos.")
                    puntuacion += 70
                elif errores == 3:
                    print("\n", "\n", "Ups! Tuviste ", f"{RED}{errores}{END}", ". Obtuviste 50 puntos.")
                    puntuacion += 50
                elif errores > 3:
                    print("\n", "\n", "Dejaste escapar la oración y sumas 0 puntos. Mejor suerte la proxima.")
                    puntuacion += 0

                print("\n", "Ahora sumemos unos puntos extra!")

                print("\n", "A continuación escriba los sustantivos de la oración:", "\n")
                sustantivos_jugador = input(f"{YELLOW}{BOLD}Jugador: {END}")
                errores_sustantivos = comparacion_sustantivos(oraciones[i]["sustantivos"],sustantivos_jugador)
                if errores_sustantivos == 0:
                    puntuacion += 30
                    print("Errores sustantivos: ",f"{GREEN}{errores_sustantivos}{END}")
                else:
                    print("Errores sustantivos: ",f"{RED}{errores_sustantivos}{END}.", "(Respuesta correcta: ", oraciones[i]["sustantivos"],")")

                print("A continuación escriba los verbos de la oración:", "\n")
                verbos_jugador = input(f"{YELLOW}{BOLD}Jugador: {END}")
                errores_verbos = comparacion_verbos(oraciones[i]["verbos"], verbos_jugador)
                if errores_verbos == 0:
                    puntuacion += 30
                    print("Errores verbos: ",f"{GREEN}{errores_verbos}{END}")
                else:
                    print("Errores verbos: ",f"{RED}{errores_verbos}{END}.", "(Respuesta correcta: ", oraciones[i]["verbos"],")")

                print("A continuación escriba los adjetivos de la oración:", "\n")
                adjetivos_jugador = input(f"{YELLOW}{BOLD}Jugador: {END}")
                errores_adjetivos = comparacion_adjetivos(oraciones[i]["adjetivos"], adjetivos_jugador)
                if errores_adjetivos == 0:
                    puntuacion += 30
                    print("Errores adjetivos: ",f"{GREEN}{errores_adjetivos}{END}")
                else:
                    print("Errores adjetivos: ",f"{RED}{errores_adjetivos}{END}.", "(Respuesta correcta: ", oraciones[i]["adjetivos"],")")

                break
        j += 1
                    
    
    print("La cazeria a terminado! Felicitaciones por haber llegado hasta el final!")
    print("Tu puntaje final es: ", puntuacion)
    

    while True:
        volver_menu = input("\nPresiona 'x' para volver al menú: ").lower()
        if volver_menu == 'x':
            print("Regresando al menú principal...")
            break