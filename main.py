# from juegos.CazadoresDeGramatica import test (Linea de codigo definida para cuando esten las funciones echas)
from juegos.JuegoAdivinaAnimal import iniciar_juego
from juegos.ChOrD3 import juego_musica
from juegos.tablas_de_multiplicar import LlamarJuegoMultiplicar 
from juegos.ultra_septimum import jugar
menu = 0

while menu != 3:
    print("=======================================================")

    print("                  |MENU PRINCIPAL|")

    print("=======================================================")
    print("        |SELECCIONA UN JUEGO PARA COMENZAR|")
    print()
    print("        |1| →   Cazadores De Gramatica    |")
    print("        |2| →       Adivina El Animal     |")
    print("        |3| →   Tablas de multiplicar     |")
    print("        |4| →            Ch0rD3           |")
    print("        |5| →        Ultra Septimum       |")
    print("        |6| →            SALIR            |")
    print()
    menu = int(input("              Opcion a elegir →"))
    if menu == 1:
        from juegos.CazadoresDeGramatica import test #IGNORAR ESTA LINEA
    elif menu == 2:
        iniciar_juego()
    elif menu == 3:
        tablas()
    elif menu == 4:
        juego_musica()
    elif menu == 5:
        juegar()
    elif menu == 6:
        print("            PROGRAMA FINALIZADO")

        
