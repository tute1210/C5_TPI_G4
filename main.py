from juegos.CazadoresDeGramatica import cazadores_de_gramatica
from juegos.JuegoAdivinaAnimal import iniciar_juego
from juegos.ChOrD3 import juego_musica
from juegos.tablas_de_multiplicar import LlamarJuegoMultiplicar
from juegos.ultra_septimum import jugar
from juegos.preguntas8_python import jugarpython8
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
    print("        |3| →   Tablas de multiplicar     |")
    print("        |4| →            Ch0rD3           |")
    print("        |5| →        Ultra Septimum       |")
    print("        |6| →     8 Preguntas Python      |")
    print("        |7| →          Buscaminas         |")
    print("        |8| →            SALIR            |")
    print()
    menu = int(input("              Opcion a elegir →"))
    if menu == 1:
        cazadores_de_gramatica()
    elif menu == 2:
        iniciar_juego()
    elif menu == 3:
        LlamarJuegoMultiplicar()
    elif menu == 4:
        juego_musica()
    elif menu == 5:
        jugar()
    elif menu == 6:
        jugarpython8()
    elif menu == 7:
        iniciar_Buscaminas()
    elif menu == 8:
        print("            PROGRAMA FINALIZADO")


