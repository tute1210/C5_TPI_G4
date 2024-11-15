import random
respCorrectasN1 = 0
respCorrectasN2 = 0
respCorrectasN3 = 0
respCorrectasN4 = 0
respCorrectasN5 = 0
vidas = 3
recompensa = 0
cont = 0
respCorrectas = 0
nombre = input("Ingresa tu nombre\n")
print("Bienvenido/a",nombre,"al juego de las tablas\n")
print("Pon a prueba tu conocimiento y aprende jugando\n")
print("Selecciona el nivel de dificultad con el que quieres jugar\n")
print("Digita 1 para seleccionar el nivel fácil")
print("Digita 2 para seleccionar el nivel dificil")
dificultad = int(input())
if dificultad == 1:
#NIVEL 1
    while respCorrectasN1 != 3 and vidas != 0:
        cont += 1
        print("Resuelve esta multiplicación")
        num1 = random.randint(1, 3)
        num2 = random.randint(1, 3)
        print("==================================================")
        print(num1,"x",num2)
        print("==================================================")
        print("Respuesta:")
        resultado = int(input())
        if resultado == num1*num2:
            respCorrectas += 1
            print("---------------------------------------------")
            print("           ✅  Correcto" )
            print("---------------------------------------------")
            respCorrectasN1 += 1
        else:
            print("---------------------------------------------")
            print("               ✗   Incorrecto")
            print("---------------------------------------------")
            vidas -= 1
            print("Te quedan:",vidas,"vidas ♡")
            print("")
    if respCorrectasN1 == 3:    
        print("Felicidades,",nombre," avanzaste de nivel:")
        print("")
        print("Pregunta BONUS")
        num1Bonus = random.randint(1, 5)
        num2Bonus = random.randint(1, 5)
        num3Bonus = random.randint(1, 5)
        num1Bonus = str(num1Bonus)                                                                                   
        num2Bonus = str(num2Bonus)                                                        
        bonus1 = num1Bonus + num2Bonus
        bonus1 = int(bonus1)
        print(bonus1,"x",num3Bonus)
        resultadoBonus = int(input())
        if resultadoBonus == bonus1*num3Bonus :
            print("---------------------------------------------")
            print("           ✅  Correcto" )
            print("---------------------------------------------")
            print("")
            print("⇩ Reclama tu recompensa ⇩")
            print("")
            print("Digite 1 para obtener una vida extra")
            print("Digite 2 para empezar el nivel 2 con una pregunta menos")
            recompensa = int(input())
            if recompensa == 1:
                vidas += 1
                print("")
                print("Has elegido una vida extra ♡ !")
                print("")
                print("Ahora tienes",vidas,"vidas ♡")
                print("")
                print("Bienvenido al nivel 2")
                
            elif recompensa == 2:
                print("")
                print("Has elegido comenzar el nivel 2 con una pregunta menos")
                print("")
                print("Bienvenido al nivel 2")
                respCorrectasN2 += 1
    
    #NIVEL 2    
   
    while respCorrectasN2 != 3 and vidas != 0:
        cont += 1
        print("Resuelve esta multiplicación")
        num1 = random.randint(4, 6)
        num2 = random.randint(4, 6)
        print("==================================================")
        print(num1,"x",num2)
        print("==================================================")
        resultado = int(input())
        if resultado == num1*num2:
            respCorrectas += 1
            print("---------------------------------------------")
            print("           ✅  Correcto" )
            print("---------------------------------------------")
            respCorrectasN2 += 1
        else:
            print("---------------------------------------------")
            print("               ✗   Incorrecto")
            print("---------------------------------------------")
            vidas -= 1
            print("Te quedan:",vidas,"vidas ♡")
    if respCorrectasN2 == 3:    
        print("Felicidades,",nombre," avanzaste de nivel:")
        print("")
        print("Pregunta BONUS")
        num1Bonus = random.randint(1, 5)
        num2Bonus = random.randint(1, 5)
        num3Bonus = random.randint(1, 5)
        num1Bonus = str(num1Bonus)                                                                                   
        num2Bonus = str(num2Bonus)                                                        
        bonus1 = num1Bonus + num2Bonus
        bonus1 = int(bonus1)
        print(bonus1,"x",num3Bonus)
        resultadoBonus = int(input())
        if resultadoBonus == bonus1*num3Bonus :
            print("---------------------------------------------")
            print("           ✅  Correcto" )
            print("---------------------------------------------")
            print("")
            print("⇩ Reclama tu recompensa ⇩")
            print("")
            print("Digite 1 para obtener una vida extra")
            print("Digite 2 para empezar el nivel 3 con una pregunta menos")
            recompensa = int(input())
            if recompensa == 1:
                print("")
                print("Has elegido una vida extra ♡ !")
                print("")
                vidas += 1
                print("Ahora tienes",vidas,"vidas ♡")
                print("")
                print("Bienvenido al nivel 3")
                
            elif recompensa == 2:
                print("")
                print("Has elegido comenzar el nivel 3 con una pregunta menos")
                print("")
                print("Bienvenido al nivel 3")
                respCorrectasN3 += 1
  
     #NIVEL 3    
    
    while respCorrectasN3 != 3 and vidas != 0:
        cont += 1
        print("Resuelve esta multiplicación")
        num1 = random.randint(7, 9)
        num2 = random.randint(7, 9)
        print("==================================================")
        print(num1,"x",num2)
        print("==================================================")
        resultado = int(input())
        if resultado == num1*num2:
            respCorrectas += 1
            print("---------------------------------------------")
            print("           ✅  Correcto" )
            print("---------------------------------------------")
            respCorrectasN3 += 1
        else:
            print("---------------------------------------------")
            print("               ✗   Incorrecto")
            print("---------------------------------------------")
            vidas -= 1
            print("Te quedan:",vidas,"vidas ♡")
    if respCorrectasN3 == 3:    
        print("Felicidades,",nombre," has completado todos los niveles")
        print("¡Eres un ganador ♛!")
    else:
        print("Mas suerte la proxima")    
#DIFIULTAD DIFICIL        
elif dificultad == 2:
#NIVEL 1    
    while respCorrectasN1 != 3 and vidas != 0:
        cont += 1
        print("Resuelve esta multiplicación")
        num1 = random.randint(1, 3)
        num2 = random.randint(1, 3)
        print("==================================================")
        print(num1,"x",num2)
        print("==================================================")
        resultado = int(input())
        if resultado == num1*num2:
            respCorrectas += 1
            print("---------------------------------------------")
            print("           ✅  Correcto" )
            print("---------------------------------------------")
            respCorrectasN1 += 1
        else:
            print("---------------------------------------------")
            print("               ✗   Incorrecto")
            print("---------------------------------------------")
            vidas -= 1
            print("Te quedan:",vidas,"vidas ♡")
    if respCorrectasN1 == 3:    
        print("Felicidades,",nombre," avanzaste de nivel:")
        print("")
        print("Pregunta BONUS")
        num1Bonus = random.randint(1, 5)
        num2Bonus = random.randint(1, 5)
        num3Bonus = random.randint(1, 5)
        num1Bonus = str(num1Bonus)                                                                                   
        num2Bonus = str(num2Bonus)                                                        
        bonus1 = num1Bonus + num2Bonus
        bonus1 = int(bonus1)
        print(bonus1,"x",num3Bonus)
        resultadoBonus = int(input())
        if resultadoBonus == bonus1*num3Bonus :
            print("         ✅  Correcto!")
            print("")
            print("⇩ Reclama tu recompensa ⇩")
            print("")
            print("Digite 1 para obtener una vida extra")
            print("Digite 2 para empezar el nivel 2 con una pregunta menos")
            recompensa = int(input())
            if recompensa == 1:
                vidas = vidas + 1
                print("")
                print("Has elegido una vida extra ♡ !")
                print("")
                vidas += 1
                print("Ahora tienes",vidas,"vidas ♡")
                print("")
                print("Bienvenido al nivel 2")
            elif recompensa == 2:
                print("")
                print("Has elegido comenzar el nivel 2 con una pregunta menos")
                print("")
                print("Bienvenido al nivel 2")
                respCorrectasN2 += 1
    
#NIVEL 2    
    
    while respCorrectasN2 != 3 and vidas != 0:
        cont += 1
        print("Resuelve esta multiplicación")
        num1 = random.randint(3, 6)
        num2 = random.randint(3, 6)
        print("==================================================")
        print(num1,"x",num2)
        print("==================================================")
        resultado = int(input())
        if resultado == num1*num2:
            respCorrectas += 1
            print("---------------------------------------------")
            print("           ✅  Correcto" )
            print("---------------------------------------------")
            respCorrectasN2 += 1
        else:
            print("---------------------------------------------")
            print("               ✗   Incorrecto")
            print("---------------------------------------------")
            vidas -= 1
            print("Te quedan:",vidas,"vidas ♡")
    if respCorrectasN2 == 3:    
        print("Felicidades,",nombre," avanzaste de nivel:")
        print("")
        print("Pregunta BONUS")
        num1Bonus = random.randint(1, 5)
        num2Bonus = random.randint(1, 5)
        num3Bonus = random.randint(1, 5)
        num1Bonus = str(num1Bonus)                                                                                   
        num2Bonus = str(num2Bonus)                                                        
        bonus1 = num1Bonus + num2Bonus
        bonus1 = int(bonus1)
        print(bonus1,"x",num3Bonus)
        resultadoBonus = int(input())
        if resultadoBonus == bonus1*num3Bonus :
            print("---------------------------------------------")
            print("           ✅  Correcto" )
            print("---------------------------------------------")
            print("")
            print("⇩ Reclama tu recompensa ⇩")
            print("")
            print("Digite 1 para obtener una vida extra")
            print("Digite 2 para empezar el nivel 3 con una pregunta menos")
            recompensa = int(input())
            if recompensa == 1:
                print("")
                print("Has elegido una vida extra ♡ !")
                print("")
                vidas += 1
                print("Ahora tienes",vidas,"vidas")
                print("Bienvenido al nivel 3")
            elif recompensa == 2:
                print("")
                print("Has elegido comenzar el nivel 3 con una pregunta menos")
                print("")
                respCorrectasN3 += 1
                print("Bienvenido al nivel 3")
    
#NIVEL 3
    while respCorrectasN3 != 3 and vidas != 0:
        cont += 1
        print("Resuelve esta multiplicación")
        num1 = random.randint(7, 9)
        num2 = random.randint(7, 9)
        print("==================================================")
        print(num1,"x",num2)
        print("==================================================")
        resultado = int(input())
        if resultado == num1*num2:
            respCorrectas += 1
            print("---------------------------------------------")
            print("           ✅  Correcto" )
            print("---------------------------------------------")
            respCorrectasN3 += 1
        else:
            print("---------------------------------------------")
            print("               ✗   Incorrecto")
            print("---------------------------------------------")
            vidas -= 1
            print("Te quedan:",vidas,"vidas ♡")
    if respCorrectasN3 == 3:    
        print("Felicidades,",nombre," avanzaste de nivel:")
        print("")
        print("Pregunta BONUS")
        num1Bonus = random.randint(1, 5)
        num2Bonus = random.randint(1, 5)
        num3Bonus = random.randint(1, 5)
        num1Bonus = str(num1Bonus)                                                                  
        num2Bonus = str(num2Bonus)                                                        
        bonus1 = num1Bonus + num2Bonus
        bonus1 = int(bonus1)
        print(bonus1,"x",num3Bonus)
        resultadoBonus = int(input())
        if resultadoBonus == bonus1*num3Bonus :
            print("---------------------------------------------")
            print("           ✅  Correcto" )
            print("---------------------------------------------")
            print("")
            print("⇩ Reclama tu recompensa ⇩")
            print("")
            print("Digite 1 para obtener una vida extra")
            print("Digite 2 para empezar el nivel 4 con una pregunta menos")
            recompensa = int(input())
            if recompensa == 1:
                print("")
                print("Has elegido una vida extra ♡ !")
                print("")
                vidas += 1
                print("Ahora tienes",vidas,"vidas")
                print("Bienvenido al nivel 4")
            elif recompensa == 2:
                print("")
                print("Has elegido comenzar el nivel 4 con una pregunta menos")
                print("")
                respCorrectasN4 += 1
                print("Bienvenido al nivel 4")
    
#NIVEL 4
    while respCorrectasN4 != 3 and vidas != 0:
        cont += 1
        print("Resuelve esta multiplicación")
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        num3 = random.randint(1, 9)
        num1 = str(num1)
        num2 = str(num2)
        suma1 = num1+num2
        suma1 = int(suma1)
        print("==================================================")
        print(suma1,"x",num3)
        print("==================================================")
        resultado = int(input())
        if resultado == suma1*num3:
            respCorrectas += 1
            print("---------------------------------------------")
            print("           ✅  Correcto" )
            print("---------------------------------------------")
            respCorrectasN4 += 1
        else:
            print("---------------------------------------------")
            print("               ✗   Incorrecto")
            print("---------------------------------------------")
            vidas -= 1
            print("Te quedan:",vidas,"vidas ♡")
    if respCorrectasN4 == 3:    
        print("Felicidades,",nombre," avanzaste de nivel:")
        print("")
        print("Pregunta BONUS")
        num1Bonus = random.randint(1,9)
        num2Bonus = random.randint(1,9)
        num3Bonus = random.randint(1,9)
        num4Bonus = random.randint(1,9)
        num1Bonus = str(num1Bonus)                                                              
        num2Bonus = str(num2Bonus) 
        num3Bonus = str(num2Bonus) 
        num4Bonus = str(num2Bonus) 
        bonus1 = num1Bonus + num2Bonus
        bonus2 = num3Bonus + num4Bonus
        bonus1 = int(bonus1)
        bonus2 = int(bonus2)
        print(bonus1,"x",bonus2)
        resultadoBonus = int(input())
        if resultadoBonus == bonus1*bonus2 :
            print("---------------------------------------------")
            print("           ✅  Correcto" )
            print("---------------------------------------------")
            print("")
            print("⇩ Reclama tu recompensa ⇩")
            print("")
            print("Digite 1 para obtener una vida extra")
            print("Digite 2 para empezar el nivel 5 con una pregunta menos")
            recompensa = int(input())
            if recompensa == 1:
                print("")
                print("Has elegido una vida extra ♡ !")
                print("")
                vidas += 1
                print("Ahora tienes",vidas,"vidas ♡ ")
                print("Bienvenido al nivel 5")
            elif recompensa == 2:
                print("")
                print("Has elegido comenzar el nivel 5 con una pregunta menos")
                print("")
                respCorrectasN5 += 1
                print("Bienvenido al nivel 5")
    
#NIVEL 5        
        
    while respCorrectasN5 != 3 and vidas != 0:
        cont += 1
        print("Resuelve esta multiplicación")
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        num3 = random.randint(1, 9)
        num4 = random.randint(1, 9)
        num1 = str(num1)
        num2 = str(num2)
        suma1 = num1+num2
        suma1 = int(suma1)
        num3 = str(num3)
        num4 = str(num4)
        suma2 = num3+num4
        suma2 = int(suma2)
        print(suma1,"x",suma2)
        resultado = int(input())
        if resultado == suma1*suma2:
            respCorrectas += 1
            print("---------------------------------------------")
            print("           ✅  Correcto" )
            print("---------------------------------------------")
            respCorrectasN5 += 1
        else:
            print("---------------------------------------------")
            print("               ✗   Incorrecto")
            print("---------------------------------------------")
            vidas -= 1
            print("Te quedan:",vidas,"vidas ♡")
    if respCorrectasN5 == 3:    
        print("Felicidades,",nombre," has completado todos los niveles")
        print("¡Eres un ganador ♛!")
    else:
        print("Mas suerte la proxima")    
else:
    print("Opcion incorrecta")
print("")    
print(" Estadisticas:")
print("")
print("Has contestado correctamente",respCorrectas,"de",cont,"posibles. Buen trabajo!")
porcentaje = (respCorrectas / cont)*100
porcentaje = round(porcentaje)
print("")
print("Has logrado un porcentaje de aciertos de: ",porcentaje,"%" )