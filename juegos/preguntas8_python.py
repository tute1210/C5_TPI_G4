def nivel1():
    print("Nivel 1: Variables")
    print("Pregunta: ¿Qué valor tendrá 'z' después de este código?")
    print("x = 10\ny = 5\nz = x + y")
    respuesta = input("Tu respuesta: ")
    if respuesta == "15":
        print("¡Correcto! Pasas al siguiente nivel.")
        return True
    else:
        print("Respuesta incorrecta. Intenta de nuevo.")
        return False

def nivel2():
    print("Nivel 2: Condicionales")
    print("Pregunta: ¿Qué se imprime al ejecutar este código?")
    print("""
x = 7
if x % 2 == 0:
    print("Par")
else:
    print("Impar")
    """)
    respuesta = input("Tu respuesta: ")
    if respuesta.lower() == "impar":
        print("¡Correcto! Pasas al siguiente nivel.\n")
        return True
    else:
        print("Respuesta incorrecta. Intenta de nuevo.\n")
        return False

def nivel3():
    print("Nivel 3: Bucles")
    print("Pregunta: ¿Cuántas veces se imprime 'Hola'?")
    print("""
for i in range(3):
    print("Hola")
    """)
    respuesta = input("Tu respuesta: ")
    if respuesta == "3":
        print("¡Correcto! Pasas al siguiente nivel.\n")
        return True
    else:
        print("Respuesta incorrecta. Intenta de nuevo.\n")
        return False

def nivel4():
    print("Nivel 4: Listas")
    print("Pregunta: ¿Cuál será el resultado de 'mi_lista[1]'?")
    print("""
mi_lista = [10, 20, 30]
    """)
    respuesta = input("Tu respuesta: ")
    if respuesta == "20":
        print("¡Correcto! Pasas al siguiente nivel.")
        return True
    else:
        print("Respuesta incorrecta. Intenta de nuevo.")
        return False

def nivel5():
    print("Nivel 5: Diccionarios")
    print("Pregunta: ¿Qué valor imprime 'mi_dict['clave']'?")
    print("""
mi_dict = {'clave': 42, 'otra_clave': 15}
    """)
    respuesta = input("Tu respuesta: ")
    if respuesta == "42":
        print("¡Correcto! Pasas al siguiente nivel.")
        return True
    else:
        print("Respuesta incorrecta. Intenta de nuevo.")
        return False

def nivel6():
    print("Nivel 6: Funciones")
    print("Pregunta: ¿Qué imprime 'suma(2, 3)'?")
    print("""
def suma(a, b):
    return a + b
    """)
    respuesta = input("Tu respuesta: ")
    if respuesta == "5":
        print("¡Correcto! Pasas al siguiente nivel.")
        return True
    else:
        print("Respuesta incorrecta. Intenta de nuevo.")
        return False

def nivel7():
    print("Nivel 7: Manejo de errores")
    print("Pregunta: ¿Qué se imprime si ocurre un error?")
    print("""
try:
    x = int("hola")
except ValueError:
    print("Error de valor")
    """)
    respuesta = input("Tu respuesta: ")
    if respuesta.lower() == "error de valor":
        print("¡Correcto! Pasas al siguiente nivel.")
        return True
    else:
        print("Respuesta incorrecta. Intenta de nuevo.")
        return False

def nivel8():
    print("Nivel 8: Archivos")
    print("Pregunta: ¿Qué contiene el archivo después de este código?")
    print("""
with open("archivo.txt", "w") as f:
    f.write("Hola mundo")
    """)
    respuesta = input("Tu respuesta: ")
    if respuesta.lower() == "hola mundo":
        print("¡Correcto! Pasas al siguiente nivel.")
        return True
    else:
        print("Respuesta incorrecta. Intenta de nuevo.")
        return False

def jugarpython8():
    print("¡Bienvenido al juego de Python!")
    print("Reglas del juego:")
    print("1. El objetivo es completar los 8 niveles resolviendo preguntas de programación.")
    print("2. Solo puedes avanzar si respondes correctamente.")
    print("3. Tienes intentos ilimitados, pero reflexiona antes de responder.")
    print("4. ¡Aprende y diviértete mientras mejoras tus habilidades!")
    print("¿Estás listo? ¡Comencemos!")

    niveles = [nivel1, nivel2, nivel3, nivel4, nivel5, nivel6, nivel7, nivel8]

    i = 0  
    while i < len(niveles): 
        print("=== Nivel", i + 1, "===")  
        if not niveles[i](): 
            print("¡Intenta de nuevo para mejorar!")
            break
        i += 1 
    else:
        print("¡Felicidades! Has completado todos los niveles.")
        print("SOS UN CRACK EN PYTHON")
