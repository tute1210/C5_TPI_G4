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