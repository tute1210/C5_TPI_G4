def iniciar_Buscaminas(): 
    import math
    import random

    def redondear(num):
        return math.ceil(num) if num >= 0.5 else math.floor(num)

    def imprimir_campo(campo):
        for f in campo:
            print("".join(f))

    def ocupado(campo,x,y):
        return campo[y][x]=="X"

    def contar_minas_alrededor(campo,x,y):
        minas_alrededor=0
        for i in range(-1,2):
            for j in range(-1,2):
                if i==0 and j==0:
                    continue
                nx=x+i
                ny=y+j
                if nx>=0 and nx<len(campo[0]) and ny>=0 and ny<len(campo):
                    if campo[ny][nx]=="X":
                        minas_alrededor=minas_alrededor+1
        return minas_alrededor

    def desactivar(campo,x,y):
        campo[y][x]="V"

    def explorar_pos(campo,x,y):
        if ocupado(campo,x,y):
            return "MINA DETONADA! Fin del Juego"
        else:
            minas_alrededor=contar_minas_alrededor(campo,x,y)
            return str(minas_alrededor)

    def obtener_ancho(filas):
        return redondear(filas*(16/9))

    alto=int(input())
    ancho=obtener_ancho(alto)
    campomin=[["O"]*ancho for _ in range(alto)]


    cantidad_minas = redondear(alto * 2)
    posiciones_disponibles = [(x, y) for x in range(ancho) for y in range(alto)]
    random.shuffle(posiciones_disponibles)

    for _ in range(cantidad_minas):
        x, y = posiciones_disponibles.pop()
        campomin[y][x] = "X"

    print("Carga completa! MODO DESACTIVACION")
    imprimir_campo(campomin)
    minas_desact = 0
    while True:
        coordenadas=input()
        if len(coordenadas)==5 and coordenadas.isnumeric():
            x=redondear(float(coordenadas[:2]))
            y=redondear(float(coordenadas[2:4]))
            if x>=0 and x<ancho and y>=0 and y<alto:
                accion=redondear(float(coordenadas[4]))
                if accion==1:
                    if ocupado(campomin,x,y):
                        desactivar(campomin,x,y)
                        minas_desact=minas_desact+1
                        print("DESACTIVADA")
                elif accion==0:
                    result_exploracion=explorar_pos(campomin,x,y)
                    print(result_exploracion)
                    if result_exploracion=="MINA DETONADA! Fin del Juego":
                        break
            else:
                print("COORDENADAS INVALIDAS (FUERA DE RANGO)")
        else:
            print("COORDENADAS INVALIDAS (FORMATO INCORRECTO)")

        if minas_desact==cantidad_minas:
            print("CAMPO MINADO DESACTIVADO! Fin del Juego")
            break
        
    pass