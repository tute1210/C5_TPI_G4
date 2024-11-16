
def cazadores_de_gramatica():

    import random # Libreria "random" para poder obtener oraciones aleatorias de la lista "oraciones"

    #Codigo ASCII de diferentes modos para decorar texto
    BOLD = '\033[1m'       #{BOLD}
    ITALIC = '\033[3m'     #{ITALIC}
    RED = '\033[91m'
    RESET = '\033[0m'      #{RESET}

    #Presentación del juego + instrucciones

    

    #Inicio de variables
    oraciones = []
    puntuacion = 0

    #Abrir archivo oraciones.txt y guardar contenido en lista
    def leer_archivo():
        with open("juegos/oraciones.txt", "r", encoding="utf-8") as archivo:
            for i in range(10):
                oracion_incorrecta = archivo.readline()
                oracion_correcta = archivo.readline()
                sustantivos = archivo.readline()
                verbos = archivo.readline()
                adjetivos = archivo.readline()
                oraciones.append({
                    "incorrecta": oracion_incorrecta,
                    "correcta": oracion_correcta,
                    "sustantivos": sustantivos,
                    "verbos": verbos,
                    "adjetivos": adjetivos
                })
            archivo.close

    leer_archivo()

    #Función que compara la oración correcta guardada en oraciones.txt con lo que ingresa el jugador
    def comparacion_oraciones(oracion_correcta, oracion_player):
        palabras_correctas = oracion_correcta.split()
        palabras_jugador = oracion_player.split()

        aciertos = 0
        errores = 0

        long = len(palabras_correctas)
        # Compara palabra por palabra

        for palabra in palabras_jugador:
            if palabra in palabras_correctas:
                aciertos += 1
            else:
                errores += 1

        # for i in range(long):
        #     if palabras_correctas[i] == palabras_jugador[i]:
        #         aciertos += 1
        #     else:
        #         errores += 1
        # print("Aciertos: ", aciertos)
        # print("Errores: ", errores)
        return errores

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
        # print("Errores: ", errores)s
        return errores

    indices_aleatorios = random.sample(range(len(oraciones)), 1)

    for i in indices_aleatorios:
        print(f"{RED}{BOLD}Oración a corregir:{RESET}", oraciones[i]["incorrecta"])
        oracion_player = input(f"{BOLD}Jugador: {RESET}")
        errores = comparacion_oraciones(oracion_correcta=oraciones[i]["correcta"], oracion_player=oracion_player)
        if errores == 0:
            print("Felicitaciones! Oración perfecta. Obtuviste 100 puntos. Pasemos a la siguiente oraciones:")
            puntuacion += 100
        elif errores == 1:
            print("Felicitaciones! Tuviste ", errores, ". Obtuviste 90 puntos. Pasemos a la siguiente oración:")
            puntuacion += 90
        elif errores == 2:
            print("Felicitaciones! Tuviste ", errores,". Obtuviste 70 puntos. Pasemos a la siguiente oración:")
            puntuacion += 70
        elif errores == 3:
            print("Felicitaciones! Tuviste ", errores, ". Obtuviste 50 puntos. Pasemos a la siguiente oración")
            puntuacion += 50
        else:
            print("")

        print("Ahora sumemos unos puntos extra!")

        print("A continuación escriba los sustantivos de la oración:", "\n")
        sustantivos_jugador = input(f"{BOLD}Jugador: {RESET}")
        errores_sustantivos = comparacion_sustantivos(oraciones[i]["sustantivos"],sustantivos_jugador)
        if errores_sustantivos == 0:
            puntuacion += 30
        print("Errores sustantivos: ",errores_sustantivos)

        print("A continuación escriba los verbos de la oración:", "\n")
        verbos_jugador = input(f"{BOLD}Jugador: {RESET}")
        errores_verbos = comparacion_verbos(oraciones[i]["verbos"], verbos_jugador)
        if errores_verbos == 0:
            puntuacion += 30
        print("Errores sustantivos: ",errores_verbos)

        print("A continuación escriba los adjetivos de la oración:", "\n")
        adjetivos_jugador = input(f"{BOLD}Jugador: {RESET}")
        errores_adjetivos = comparacion_adjetivos(oraciones[i]["adjetivos"], adjetivos_jugador)
        if errores_adjetivos == 0:
            puntuacion += 30
        print("Errores sustantivos: ",errores_adjetivos)

    print("La cazeria a terminado! Felicitaciones por haber llegado hasta el final!")
    print("Tu puntaje final es: ", puntuacion)
    

    while True:
        volver_menu = input("\nPresiona 'x' para volver al menú: ").lower()
        if volver_menu == 'x':
            print("Regresando al menú principal...")
            break