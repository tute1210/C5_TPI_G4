def JuegoMusica():
    import random
        
    def representacion_piano():
        piano = ["DO   RE   MI FA   SOL   LA   SI DO",
                    "  !#!  !#!  !  !#!   !#!  !#!  !  ",
                    "  !#!  !#!  !  !#!   !#!  !#!  !  ",
                    "  !#!  !#!  !  !#!   !#!  !#!  !  "]
        for i in piano:
            print(i)
        
    def puntajes(nombre, puntaje, mas100, menos100):
            archivo_directorio = "C:/Users/Public/Documents/puntajes.txt"
            archivo = open(archivo_directorio, "a")
            archivo.write(nombre + " - Puntaje total: " + str(puntaje) + " (Ganados: " + str(mas100) + ", Perdidos: " + str(menos100) + ")\n")
            archivo.close()
        
    nombre = input("Ingrese su nombre: ")
    puntaje = 0
    puntajes_ganados = 0
    puntajes_perdidos = 0
    notas = ["Do", "Re", "Mi", "Fa", "Sol", "La", "Si", "Do"]
    acorde_do = tuple([notas[0], notas[2], notas[4]])
    acorde_re = tuple([notas[1], notas[3], notas[5]])
    acorde_mi = tuple([notas[2], notas[4], notas[6]])
    acorde_fa = tuple([notas[3], notas[5], notas[7]])
    acorde_sol = tuple([notas[4], notas[6], notas[1]])
    acorde_la = tuple([notas[5], notas[7], notas[2]])
    acorde_si = tuple([notas[6], notas[1], notas[3]])
    acordes_azar = [acorde_do, acorde_re, acorde_mi, acorde_fa, acorde_sol, acorde_la, acorde_si]
    resp_acordes = {
        acorde_do: "C",
        acorde_re: "Dm",
        acorde_mi: "Em",
        acorde_fa: "F",
        acorde_sol: "G",
        acorde_la: "Am",
        acorde_si: "Bdim"
    }
        
    print("Notas de la escala mayor de C: ", notas)
    print("Si el acorde es Do Mayor, responder con C")
    print("Si el acorde es Re menor, responder con Dm")
    print("Si el acorde es Mi menor, responder con Em")
    print("Si el acorde es Fa Mayor, responder con F")
    print("Si el acorde es Sol Mayor, responder con G")
    print("Si el acorde es La menor, responder con Am")
    print("Si el acorde es Si disminuido, responder con Bdim") 
    print()
        
    while puntaje < 1000:
        representacion_piano()
        print()
        tres_notas = random.choice(acordes_azar)
        print(tres_notas)
        resp_usuario = input("Que acorde es?: ")
        if resp_usuario == resp_acordes[tres_notas]:
            print("                                                              ¡Correcto! +100p")
            puntaje = puntaje + 100
            puntajes_ganados = puntajes_ganados + 100
        else:
            puntaje = puntaje - 100
            puntajes_perdidos = puntajes_perdidos + 100 
            print("                                                              Incorrecto... -100p, recuerda que:") 
            print("Un acorde Mayor tiene que tener una distancia de dos tonos entre la primera nota y la segunda y un tono y medio entre la segunda y tercera")
            print("Un acorde menor tiene una distancia de un tono y medio entre la primera nota y la segunda y dos tonos entre la segunda y la última")
            print("Un acorde disminuido tiene una distancia de un tono y medio entre las tres notas") 
    if puntaje >= 1000:
        print("¡Felicidades, llegaste a los 1.000 puntos!")
        
    print()
    puntajes(nombre, puntaje, puntajes_ganados, puntajes_perdidos)
    print("Su puntaje ha sido guardado " + nombre)
