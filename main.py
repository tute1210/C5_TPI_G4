# from juegos.CazadoresDeGramatica import test (Linea de codigo definida para cuando esten las funciones echas)
from juegos.JuegoAdivinaAnimal import iniciar_juego
menu = 0

while menu != 3:
    print("=======================================================")

    print("                  |MENU PRINCIPAL|")

    print("=======================================================")
    print("        |SELECCIONA UN JUEGO PARA COMENZAR|")
    print()
    print("        |1| →   Cazadores De Gramatica    |")
    print("        |2| →       Adivina El Animal     |")
    print()
    print("        |3| →            SALIR            |")
    print()
    menu = int(input("              Opcion a elegir →"))
    if menu == 1:
        from juegos.CazadoresDeGramatica import test #IGNORAR ESTA LINEA
    elif menu == 2:
        iniciar_juego()
    elif menu == 3:
        print("            PROGRAMA FINALIZADO")

        