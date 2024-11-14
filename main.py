# from juegos.CazadoresDeGramatica import test (Linea de codigo definida para cuando esten las funciones echas)

menu = 0

while menu != 2:
    print("Seleccione una opción:")
    print("1 - Cazadores De Gramatica")
    print("2 - SALIR")
    menu = int(input())

    if menu == 1:
        from juegos.CazadoresDeGramatica import test #IGNORAR ESTA LINEA
    elif menu == 2:
        print("FIN")