# from juegos.CazadoresDeGramatica import test (Linea de codigo definida para cuando esten las funciones echas)
from juegos.JuegoAdivinaAnimal import iniciar_juego
from juegos.ChOrD3 import juego_musica
from juegos.Buscaminas import iniciar_Buscaminas
menu = 0

while menu != 8:
    print("=======================================================")

    print("                  |MENU PRINCIPAL|")

    print("=======================================================")
    print("        |SELECCIONA UN JUEGO PARA COMENZAR|")
    print()
    print("        |1| →   Cazadores De Gramatica    |")
    print("        |2| →       Adivina El Animal     |")
    print("        |3| →            Ch0rD3           |")
    print("        |4| →          Buscaminas         |")
    print("        |8| →            SALIR            |")
    print()
    menu = int(input("              Opcion a elegir →"))
    if menu == 1:
        from juegos.CazadoresDeGramatica import test #IGNORAR ESTA LINEA
    elif menu == 2:
        iniciar_juego()
    elif menu == 3:
        juego_musica()
    elif menu == 4:
        iniciar_Buscaminas()
    elif menu == 8:
        print("            PROGRAMA FINALIZADO")

        
