BOLD = '\033[1m'       
ITALIC = '\033[3m' 
DARKCYAN = '\033[36m'    
RED = '\033[91m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
END = '\033[0m'      

def incio_CDG():
    print(f"{DARKCYAN}///////////////////////////////////////////////////////////////////////////////////////////")
    print(f"///////////////////////////////////////////////////////////////////////////////////////////")
    print(f"/////////        _____                             _                                     //")
    print(f"/////////       / ____|                           | |                                    //")
    print(f"/////////      | |        __ _   ____   __ _    __| |   ___    _ __    ___   ___         //")
    print(f"/////////      | |       / _` | |_  /  / _` |  / _` |  / _ \  | '__|  / _ \ / __|        //")
    print(f"/////////      | |____  | (_| |  / /  | (_| | | (_| | | (_) | | |    |  __/ \__ \        //")
    print(f"/////////       \_____|  \__,_| /___|  \__,_|  \__,_|  \___/  |_|     \___| |___/        //")
    print(f"/////////                                                                                //")                                                                   
    print(f"/////////                                     _                                          //")
    print(f"/////////                                    | |                                         //")
    print(f"/////////                                  __| |   ___                                   //")
    print(f"/////////                                 / _` |  / _ \                                  //")
    print(f"/////////                                | (_| | |  __/                                  //")
    print(f"/////////                                 \__,_|  \___|                                  //")                                                                                                                                       
    print(f"/////////        _____                                      _     _                      //")
    print(f"/////////       / ____|                                    | |   (_)                     //")
    print(f"/////////      | |  __   _ __    __ _   _ __ ___     __ _  | |_   _    ___    __ _       //")
    print(f"/////////      | | |_ | | '__|  / _` | | '_ ` _ \   / _` | | __| | |  / __|  / _` |      //")
    print(f"/////////      | |__| | | |    | (_| | | | | | | | | (_| | | |_  | | | (__  | (_| |      //")
    print(f"/////////       \_____| |_|     \__,_| |_| |_| |_|  \__,_|  \__| |_|  \___|  \__,_|      //")
    print(f"/////////                                                                                //")           
    print(f"///////////////////////////////////////////////////////////////////////////////////////////")
    print(f"///////////////////////////////////////////////////////////////////////////////////////////{END}")
    print("\n","\n","\n","\n","\n","\n","\n","\n")   



    print(f"{BOLD}INSTRUCCIONES:{END}")
    print("")
    print("El juego inicia mostrando una oración incorrecta.", )
    print("")
    print("El jugador tendrá dos intentos para colocar la oración completa, de lo contrario")
    print("")
    print("se le dará la oración como incorrecta.")
    print("")
    print("Pasada esta instancia, el jugador tendrá la oportunidad de sumar puntos extras,")
    print("")
    print("primero ingresando los sustantivos, luego verbos y por último adjetivos.")
    print("")
    print("Ejemplo ingreso de sustantivos: 'sustantivo1 sustantivo2 etc'")
    print("")
    print(f"{BOLD}TABLA DE PUNTUACIONES{END}")
    print("")
    print(f"{BOLD}PUNTUACIÓN PRINCIPAL{END}")
    print("Oración perfecta: 100 puntos")
    print("Oración con 1 error: 90 puntos")
    print("Oración con 2 errores: 70 puntos")
    print("Oración con 3 errores: 50 puntos")
    print("Mas de 3 errores: 0 puntos")
    print("")
    print("PUNTOS EXTRAS: solo acertando la totalidad de sus componentes respectivamente")
    print("Puntos extras: 30 puntos")
    print("Más de 1 error: 0 puntos")
    print("")
    print("")
    print("¡AHORA COMENCEMOS A JUGAR!")
