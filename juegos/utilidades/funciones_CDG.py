BOLD = '\033[1m'       
ITALIC = '\033[3m' 
DARKCYAN = '\033[36m'    
RED = '\033[91m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
END = '\033[0m' 

def leer_archivo(oraciones, ruta_archivo="juegos/utilidades/oraciones.txt"):
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        for i in range(20):
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

def comparacion_oraciones(oracion_correcta, oracion_player):
    palabras_correctas = oracion_correcta.split()
    palabras_jugador = oracion_player.split()

    aciertos = 0
    errores = 0

    long = len(palabras_correctas)
    # Compara palabra por palabra

    for palabra in palabras_jugador:
        if palabra in palabras_correctas:
            print(f"{GREEN} {palabra} {END}", end = "")
        else:
            errores += 1
            print(f"{RED} {palabra} {END}", end = "")

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
        # print("Errores: ", errores)
    return errores