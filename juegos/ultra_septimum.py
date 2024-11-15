# -*- coding: utf-8 -*-
def jugar():   
    preguntas = {
        "Ciencia": [
            ("El cuerpo humano tiene 206 huesos, ¿V o F?", "V"),
            ("El Sistema Solar tiene 7 planetas, ¿V o F?", "F"),
            ("La gravedad es una fuerza que atrae hacia el centro de la Tierra, ¿V o F?", "V")
        ],
        "Deporte": [
            ("En la Fórmula 1, los coches pueden superar los 300 km/h, ¿V o F?", "V"),
            ("El tenista Juan Martín del Potro ganó el título del US Open en 2009, ¿V o F?", "V"),
            ("La selección de fútbol alemana ha sido más de 3 veces campeona del mundo, ¿V o F?", "V")
        ],
        "Famosos": [
            ("Mirtha Legrand fue contemporánea a Charles Choplin', ¿V o F?", "V"),
            ("Leonardo DiCaprio y Brad Pitt fueron compañeros de secundaria , ¿V o F?", "F"),
            ("Fito Páez se recibió de abogado, ¿V o F?", "F")
        ],
        "Geografía": [
            ("La cordillera de los Andes es la cadena montañosa más larga del mundo, ¿V o F?", "V"),
            ("El océano Atlántico es el más grande de todos los océanos, ¿V o F?", "F"),
            ("El continente más grande es Asia, ¿V o F?", "V")
        ],
        "Idiomas": [
            ("En francés, 'salut' es una manera muy formal de saludar, ¿V o F?", "F"),
            ("En Bélgica se habla francés, ¿V o F?", "V"),
            ("'Saudade' es una palabra portuguesa que se usa para decir 'Salud' cuando alguien estornuda, ¿V o F?", "F")
        ],
        "Historia": [
            ("Cristóbal Colón descubrió América antes que la fundación de Grecia, ¿V o F?", "F"),
            ("San Juan Pablo II fue Papa antes que Benedicto XVI, ¿V o F?", "V"),
            ("Winston Churchill asumió la presidencia del Reino Unido antes que Margaret Thatcher, ¿V o F?", "V")
        ],
        "Tecnología": [
            ("La primera computadora personal fue creada en 1985, ¿V o F?", "F"),
            ("Steve Jobs fundó Microsoft, ¿V o F?", "F"),
            ("Las computadoras cuánticas ya están en uso comercial, ¿V o F?", "F")
        ],
        "Definiciones": {
            "Ciencia": [
                ("Todo lo que tiene masa y ocupa espacio es...", "Materia"),
                ("Metal líquido a temperatura ambiente, utilizado en termómetros y en aplicaciones industriales, tóxico.", "Mercurio"),
                ("Un aparato que transmite sonidos a través de ondas electromagnéticas: ", "Radio")
            ],
            "Deporte": [
                ("El acto de poner una pelota en la canasta en baloncesto", "Encestar"),
                ("Es el país en el que se dio origen al Fútbol", "Inglaterra"),
                ("Deporte de combate en el que los oponentes luchan con espadas, buscando tocar al adversario sin ser tocado.", "Esgrima")
            ],
            "Música": [
                ("Distancia entre dos notas musicales, ya sea ascendente o descendente.", "Intervalo"),
                ("Género musical popular caracterizado por el uso prominente de guitarras eléctricas, batería y bajo eléctrico", "Rock"),
                ("El conjunto de 3 o más notas forman un...", "Acorde")
            ],

            "Gastronomía": [
                ("Guiso tradicional en Argentina a base de maíz, carne, zapallo, entre otros ingredientes.", "Locro"),
                ("Ingrediente común en postres, infusiones y glaseados, se usa como endulzante natural.", "Miel"),
                ("Un tipo de pan mexicano relleno de carne, frijoles, queso y otros ingredientes", "Taco")
            ],
            "Tecnología": [
                ("El sistema operativo más usado en computadoras personales", "Windows"),
                ("Conjunto ordenado y finito de operaciones que permite hallar la solución de un problema.", "Algoritmo"),
                ("Infraestructura de almacenamiento y procesamiento de datos que se encuentra en servidores remotos, accesibles a través de internet.", "Nube")
            ]
        }
    }

    game_over = """
    -----------------------
    |     GAME OVER :(    |
    -----------------------
    """

    trofeo = """
    ¡FELICIDADES! Eres todo un cerebrito :D
            🎉🎉🎉🎉🎉
                🏆
            🎉🎉🎉🎉🎉
    ¡RECIBE EL TROFEO MAGISTER DE ULTRA SEPTIMUM!
    """

    vidas = 3
    # correctas = 0
    nivel = 1

    print("""
 
            -------------------------------
            |                             | 
            | Bienvenido a Ultra Septimum | 
            |                             | 
            -------------------------------

        Responde correctamente 2 o 3 preguntas de cada nivel para avanzar al siguiente. 
        Recuerda que solo tienes 3 vidas.

PRIMER NIVEL: Verdadero o Falso - Ciencia
SEGUNDO NIVEL: Verdadero o Falso - Deporte
TERCER NIVEL: Verdadero o Falso - Famosos
CUARTO NIVEL: Verdadero o Falso - Geografía
QUINTO NIVEL: Verdadero o Falso - Idiomas
SEXTO NIVEL: Verdadero o Falso - ¿Qué pasó primero? Historia
SÉPTIMO NIVEL: Verdadero o Falso - Tecnología
OCTAVO NIVEL: Definiciones de la categoría que elija entre Ciencia, Deporte, Música, Gastronomía, y Tecnología.

            
            """)
    

    while nivel <= 8 and vidas > 0:
        print("NIVEL: ", nivel)
        print("Tienes",vidas,"vidas disponibles.")
        print("----------------------------------")

        if nivel < 8:
            correctas = 0 
            if nivel == 1:
                categoria = "Ciencia"
            elif nivel == 2:
                categoria = "Deporte"
            elif nivel == 3:
                categoria = "Famosos"
            elif nivel == 4:
                categoria = "Geografía"
            elif nivel == 5:
                categoria = "Idiomas"
            elif nivel == 6:
                categoria = "Historia"
            elif nivel == 7:
                categoria = "Tecnología"

            correctas = 0
            preguntas_categoria = preguntas[categoria]
            for i in range(len(preguntas_categoria)):
                preg = preguntas_categoria[i][0]
                opcion_correcta = preguntas_categoria[i][1]
                print(preg)
                rta = input()
                if rta.upper() == opcion_correcta:
                    print("¡Respuesta Correcta!")
                    correctas += 1
                else:
                    print("¡Incorrecto!, el resultado correcto era:", opcion_correcta)
            print("----------------------------------")
         

            
            if correctas >= 2:
                nivel += 1
                print("Felicidades, subes al siguiente nivel.")
                
            else:
                vidas -= 1
                if vidas > 0:
                    print("Perdiste una vida, reintenta este nivel.")

                else:
                    print(game_over)
                    
        else:
        
            correctas = 0
            print("""
    ----------------------------------------------------------------
                        ¡Felicidades! 
                Has llegado al último nivel. 
            
    Deberás escribir la palabra correspondiente a la definición 
    que aparezca en pantalla. Si aciertas DOS de las tres definiciones,
    te llevas el trofeo Magister de Ultra Septimum. 
                  

                 ¡Estás a tan solo un paso!

    -----------------------------------------------------------------

    A continuación, deberás elegir una de las siguentes categorías ingresando su número correspondiente:

1: Ciencia
2: Deporte
3: Música
4: Gastronomía
5: Tecnología

Elige sabiamente...¡Y que comience la última batalla!

            """)
            
            categoria = int(input("Eliges la categoría: "))
            
            if categoria == 1:
                categoria = "Ciencia"
            elif categoria == 2:
                categoria = "Deporte"
            elif categoria == 3:
                categoria = "Música"
            elif categoria == 4:
                categoria = "Gastronomía"
            elif categoria == 5:
                categoria = "Tecnología"
            
            preguntas_categoria = preguntas["Definiciones"][categoria]
            for i in range(len(preguntas_categoria)):
                preg = preguntas_categoria[i][0]
                opcion_correcta = preguntas_categoria[i][1]
                print(preg)
                rta = input()
                if rta.capitalize() == opcion_correcta:
                    print("¡Respuesta Correcta!")
                    correctas += 1
                else:
                    print("¡Incorrecto!, el resultado correcto es:", opcion_correcta)

            if correctas >= 2:
                print(trofeo)
                break
                
            else:
                print(game_over)
                break

jugar()