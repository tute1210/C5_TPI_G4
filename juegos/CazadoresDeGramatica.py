
def cazadores_de_gramatica():
    from juegos.utilidades.funciones_CDG import leer_archivo
    from juegos.utilidades.funciones_CDG import comparacion_oraciones
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
                                  
    indices_aleatorios = random.sample(range(len(oraciones)), 1)

    j = 0    #Contador de oraciones
    for i in indices_aleatorios:

        print(f"{YELLOW}{BOLD}{j + 1} Oración a corregir:{END}", oraciones[i]["incorrecta"]) # Imprimo en pantalla oración aleatoria a corregir

        intentos = 2
        while intentos > 0:
            oracion_player = input(f"{YELLOW}{BOLD}Jugador: {END}")
            
            #Acá comparo el largo de la oración ingresada por el jugador por si se hace el vivo y quiere usar menos palabras de las que debe.
            if len(oracion_player.split()) != len(oraciones[i]["correcta"].split()):
                print(f"{RED}La cantidad de palabras no coincide. Inténtalo de nuevo.{END}")
                intentos -= 1
            break

        errores = comparacion_oraciones(oracion_correcta=oraciones[i]["correcta"], oracion_player=oracion_player)
        if errores == 0:
            print("\n", "Felicitaciones! Oración perfecta. Obtuviste 100 puntos.")
            puntuacion += 100
        elif errores == 1:
            print("\n", "Felicitaciones! Tuviste ", errores, ". Obtuviste 90 puntos.")
            puntuacion += 90
        elif errores == 2:
            print("\n", "Felicitaciones! Tuviste ", errores,". Obtuviste 70 puntos.")
            puntuacion += 70
        elif errores == 3:
            print("\n", "Felicitaciones! Tuviste ", errores, ". Obtuviste 50 puntos.")
            puntuacion += 50
        elif errores > 3:
            print("\n", "Dejaste escapar la oración y sumas 0 puntos. Mejor suerte la proxima.")
            puntuacion += 0

        print("\n", "Ahora sumemos unos puntos extra!")

        print("A continuación escriba los sustantivos de la oración:", "\n")
        sustantivos_jugador = input(f"{BOLD}Jugador: {END}")
        errores_sustantivos = comparacion_sustantivos(oraciones[i]["sustantivos"],sustantivos_jugador)
        if errores_sustantivos == 0:
            puntuacion += 30
        print("Errores sustantivos: ",errores_sustantivos)

        print("A continuación escriba los verbos de la oración:", "\n")
        verbos_jugador = input(f"{BOLD}Jugador: {END}")
        errores_verbos = comparacion_verbos(oraciones[i]["verbos"], verbos_jugador)
        if errores_verbos == 0:
            puntuacion += 30
        print("Errores sustantivos: ",errores_verbos)

        print("A continuación escriba los adjetivos de la oración:", "\n")
        adjetivos_jugador = input(f"{BOLD}Jugador: {END}")
        errores_adjetivos = comparacion_adjetivos(oraciones[i]["adjetivos"], adjetivos_jugador)
        if errores_adjetivos == 0:
            puntuacion += 30
        print("Errores sustantivos: ",errores_adjetivos)
        j += 1

    print("La cazeria a terminado! Felicitaciones por haber llegado hasta el final!")
    print("Tu puntaje final es: ", puntuacion)
    

    while True:
        volver_menu = input("\nPresiona 'x' para volver al menú: ").lower()
        if volver_menu == 'x':
            print("Regresando al menú principal...")
            break

    #Función que compara la oración correcta guardada en oraciones.txt con lo que ingresa el jugador
    # def comparacion_oraciones(oracion_correcta, oracion_player):
    #     palabras_correctas = oracion_correcta.split()
    #     palabras_jugador = oracion_player.split()

    #     aciertos = 0
    #     errores = 0

    #     long = len(palabras_correctas)
    #     # Compara palabra por palabra

    #     for palabra in palabras_jugador:
    #         if palabra in palabras_correctas:
    #             print(f"{GREEN} {palabra} {END}", end = "")
    #         else:
    #             errores += 1
    #             print(f"{RED} {palabra} {END}", end = "")

    #     return errores

    #Función que compara los sustantivos correctos guardados en oraciones.txt con lo que ingresa el jugador
    def comparacion_sustantivos(sustantivos, sustantivos_jugador):
        sustantivos_correctos = sustantivos.split()
        sustantivos_jugador = sustantivos_jugador.split()

        aciertos = 0
        errores = 0

        long = len(sustantivos_correctos)

        for sustantivo in sustantivos_jugador:
            if sustantivo in sustantivos_correctos:
                aciertos += 1
            else:
                errores += 1
        # print("Aciertos: ", aciertos)
        # print("Errores: ", errores)
        return errores
    
    #Función que compara los verbos correctos guardados en oraciones.txt con lo que ingresa el jugador
    def comparacion_verbos(verbos, verbos_jugador):
        verbos_correctos = verbos.split()
        verbos_jugador = verbos_jugador.split()

        aciertos = 0
        errores = 0

        long = len(verbos_correctos)

        for verbo in verbos_jugador:
            if verbo in verbos_correctos:
                aciertos += 1
            else:
                errores += 1
        # print("Aciertos: ", aciertos)
        # print("Errores: ", errores)
        return errores
    
    #Función que compara los adjetivos correctos guardados en oraciones.txt con lo que ingresa el jugador
    def comparacion_adjetivos(adjetivos, adjetivos_jugador):
        adjetivos_correctos = adjetivos.split()
        adjetivos_jugador = adjetivos_jugador.split()

        aciertos = 0
        errores = 0

        long = len(adjetivos_correctos)

        for adjetivo in adjetivos_jugador:
            if adjetivo in adjetivos_correctos:
                aciertos += 1
            else:
                errores += 1
        
        # print("Aciertos: ", aciertos)
        # print("Errores: ", errores)
        return errores