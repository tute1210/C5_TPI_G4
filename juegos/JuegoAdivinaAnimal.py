def iniciar_juego():
    import time
    print()
    print()
    print("                         !!Bienvenido a Adivina el Animal!!")
    print()
    print()
    print()
    print("             En este juego deberas de responder una cantidad de 10 preguntas, ")
    print("                       al finalizar sabras tu nivel de sabiduria !")

    print()
    print("                         Ingresa | 1 | para  comenzar a jugar")

    comenzar = int(input("                                 → "))
    dificultad = 0
    print()
    print("             ------------------------------------------------------------")
    cantidad_respuestas_correctas = 0 
    cantidad_respuestas_correctas_seguidas = 0
    if comenzar == 1:
        print("                              ¡Escoje la dificultad! ")
        print()
        print("                            Para Facil presiona |→ 1 ←|")
        print("                          Para Dificil presiona |→ 2 ←|")
        dificultad = int(input("                                 → "))
        print("             ------------------------------------------------------------")

        bandera = 0
        if dificultad == 1:
            print("                               |PRIMERA PREGUNTA|")
            print()
            print("Vivo en la selva y tengo una melena impresionante. Soy el rey de la selva. ¿Quién soy?")
            print()
            print("|1| Tigre")
            print("|2| Leon")
            print("|3| Elefante")
            print("|4| Leopardo")
            respuesta = int(input("Escoje la respuesta correcta → "))
            if respuesta == 2:
                print()
                print("¡Exacto! Tu conocimiento animal es impresionante 🦁")
                cantidad_respuestas_correctas += 1
                cantidad_respuestas_correctas_seguidas += 1
            else:
                print("¡Ups! Casi… pero no es la respuesta correcta 🐢")
            time.sleep(1)
            print()
            print("                               |SEGUNDA PREGUNTA|")
            print()
            print("Tengo rayas negras sobre un cuerpo blanco y vivo en África. Aunque parezco un caballo, no soy uno. ¿Quién soy?")
            print()
            print("|1| Cebra")
            print("|2| Antilope")
            print("|3| Hiena")
            print("|4| Gacela")

            respuesta = int(input("Escoje la respuesta correcta → "))
            if respuesta == 1:
                print()
                print("¡Fantástico! ¡Esa es la respuesta correcta! 🦓")
                cantidad_respuestas_correctas += 1
                cantidad_respuestas_correctas_seguidas += 1
            else:
                print("¡Oh no! Esa fue una buena suposición, pero no es la respuesta correcta.")
                cantidad_respuestas_correctas_seguidas = 0
                
            time.sleep(1)
            print()
            print("                                |TERCER PREGUNTA|")
            print()
            print("Soy conocido por ser lento y vivir en los árboles de la selva.")
            print("Mi nombre se usa como sinónimo de alguien que se mueve despacio. ¿Quién soy?")
            print()
            print("|1| Cebra")
            print("|2| Armadillo")
            print("|3| Perezoso")
            print("|4| Tortuga")

            respuesta = int(input("Escoje la respuesta correcta → "))
            if respuesta == 3:
                print()
                print("¡Muy bien! Has dado en el clavo 🏆🦥")
                cantidad_respuestas_correctas += 1
                cantidad_respuestas_correctas_seguidas +=1
            else:
                print("¡Oh no! Esa fue una buena suposición, pero no es la respuesta correcta.")
                cantidad_respuestas_correctas_seguidas = 0
            time.sleep(1)
            print("                                 |CUARTA PREGUNTA|")
            print()
            print("Vivo en los océanos y soy conocido por mi tamaño enorme y mi canto. ¿Quién soy?")
            print()
            print("|1| Delfín")
            print("|2| Ballena")
            print("|3| Tiburón")
            print("|4| Morsa")

            respuesta = int(input("Escoje la respuesta correcta → "))
            if respuesta == 2:
                print()
                print("¡Eso es! ¡Tienes un gran ojo para las respuestas correctas 👀🐳!")
                cantidad_respuestas_correctas += 1
                cantidad_respuestas_correctas_seguidas += 1
            else:
                print("¡Sigue adelante! A veces los animales nos engañan un poco ")
                cantidad_respuestas_correctas_seguidas = 0
            time.sleep(1)
            print("                                 |QUINTA PREGUNTA|")
            print()
            print("Tengo un caparazón duro y camino lentamente. Mi hogar está siempre conmigo. ¿Quién soy?")
            print()
            print("|1| Cangrejo")
            print("|2| Oruga")
            print("|3| Erizo")
            print("|4| Tortuga")

            respuesta = int(input("Escoje la respuesta correcta → "))
            if respuesta == 4:
                print()
                print("¡Correcto! Eres un experto/a en el reino animal 🐢")
                cantidad_respuestas_correctas += 1
                cantidad_respuestas_correctas_seguidas += 1
                if cantidad_respuestas_correctas_seguidas >= 5 and bandera == 0:
                    print("                 5 RESPUESTAS CORRECTAS SEGUIDAS ERES UN GENIO ! 🧠")
                    bandera = 1
            else:
                print("No era esa, pero sigues acumulando conocimiento animal!")
                cantidad_respuestas_correctas_seguidas = 0
            time.sleep(1)
            print("                                 |SEXTA PREGUNTA|")
            print()
            print("Vivo en los desiertos y puedo pasar mucho tiempo sin beber agua, ya que la guardo en mi joroba. ¿Quién soy?")
            print()
            print("|1| Dromedario")
            print("|2| Caballo")
            print("|3| Camello")
            print("|4| Cabra")

            respuesta = int(input("Escoje la respuesta correcta → "))
            if respuesta == 3:
                print()
                print("¡Fantástico! ¡Esa es la respuesta correcta! 🥳🐫")
                cantidad_respuestas_correctas += 1
                cantidad_respuestas_correctas_seguidas +=1
                if cantidad_respuestas_correctas_seguidas >= 5 and bandera == 0:
                    print("                 5 RESPUESTAS CORRECTAS SEGUIDAS ERES UN GENIO ! 🧠")
                    bandera =1
            else:
                print("¡Inténtalo otra vez! ¡Cada error te lleva más cerca de la respuesta correcta!")      
                cantidad_respuestas_correctas_seguidas = 0  
            time.sleep(1)
            print("                                 |SEPTIMA PREGUNTA|")
            print()
            print("Vuelo de noche y tengo un excelente sentido de la ecolocación. Algunas personas me asocian con Halloween. ¿Quién soy?")
            print()
            print("|1| Lechuza")
            print("|2| Murciélago")
            print("|3| Águila")
            print("|4| Halcón")

            respuesta = int(input("Escoje la respuesta correcta → "))
            if respuesta == 2:
                print()
                print("¡Sí! Parece que has estudiado a estos animales 🦇")
                cantidad_respuestas_correctas += 1
                cantidad_respuestas_correctas_seguidas +=1
                if cantidad_respuestas_correctas_seguidas == 5 and bandera == 0:
                    print("                 5 RESPUESTAS CORRECTAS SEGUIDAS ERES UN GENIO ! 🧠")
                    bandera =1
            else:
                print("No acertaste esta vez, pero ¡la próxima seguro que lo logras!")
                cantidad_respuestas_correctas_seguidas = 0
            time.sleep(1)
            print("                                 |OCTAVA PREGUNTA|")
            print()
            print("Tengo manchas negras y soy el animal terrestre más rápido del mundo. ¿Quién soy?")
            print()
            print("|1| Leopardo")
            print("|2| Tigre")
            print("|3| Guepardo")
            print("|4| Jaguar")

            respuesta = int(input("Escoje la respuesta correcta → "))
            if respuesta == 3:
                print()
                print("¡Correcto! Sabes mucho de animales, ¡bien hecho!🐆")
                cantidad_respuestas_correctas += 1
                cantidad_respuestas_correctas_seguidas += 1
                if cantidad_respuestas_correctas_seguidas >= 5 and bandera == 0:
                    print("                 5 RESPUESTAS CORRECTAS SEGUIDAS ERES UN GENIO ! 🧠")
                    bandera =1
            else:
                print("Esa no era la correcta. ¡Sigue intentándolo, vas por buen camino!")
                cantidad_respuestas_correctas_seguidas = 0
            time.sleep(1)
            print("                                 |NOVENA PREGUNTA|")
            print()
            print("Me gusta estar en el agua, tengo escamas y me adapto a diferentes entornos. ")
            print("Algunas personas me tienen en peceras. ¿Quién soy?")
            print()
            print("|1| Pez")
            print("|2| Rana")
            print("|3| Cocodrilo")
            print("|4| Tortuga")

            respuesta = int(input("Escoje la respuesta correcta → "))
            if respuesta == 1:
                print()
                print("¡Bravo! Has acertado, eres una verdadera enciclopedia animal 🐟")
                cantidad_respuestas_correctas += 1
                cantidad_respuestas_correctas_seguidas += 1
                if cantidad_respuestas_correctas_seguidas >= 5 and bandera == 0:
                    print("                 5 RESPUESTAS CORRECTAS SEGUIDAS ERES UN GENIO ! 🧠")
                    bandera = 1
            else:
                print("No exactamente… ¡pero buena elección! Prueba otra vez 📚")
                cantidad_respuestas_correctas_seguidas = 0
            time.sleep(1)
            print("                                 |DECIMA PREGUNTA|")
            print()
            print("Cambio de color para camuflarme en el entorno, y mis ojos se mueven de manera independiente. ¿Quién soy?")
            print()
            print("|1| Iguana")
            print("|2| Salamandra")
            print("|3| Camaleón")
            print("|4| Lagartija")

            respuesta = int(input("Escoje la respuesta correcta → "))
            if respuesta == 3:
                print()
                print("¡Bravo! Has acertado, eres una verdadera enciclopedia animal 😲")
                cantidad_respuestas_correctas += 1
                cantidad_respuestas_correctas_seguidas +=1
                if cantidad_respuestas_correctas_seguidas >= 5 and bandera == 0:
                    print("                 5 RESPUESTAS CORRECTAS SEGUIDAS ERES UN GENIO ! 🧠")
                    bandera = 1
            else:
                print("¡Ups! Casi… pero no es la respuesta correcta 😢")
                cantidad_respuestas_correctas_seguidas = 0
            time.sleep(1)
        #DIFICULTAD DIFICIL

        elif dificultad == 2:
            print("                               |PRIMERA PREGUNTA|")
            print()
            print("Soy un mamífero marino que parece tener cuernos, aunque en realidad es un diente largo.")
            print("Habito en aguas frías y soy bastante raro. ¿Quién soy?")
            print()
            print("|1| Narval")
            print("|2| Beluga")
            print("|3| Orca")
            print("|4| Manatí")
            respuesta = int(input("Escoje la respuesta correcta → "))
            if respuesta == 1:
                print()
                print("¡Exacto! Tu conocimiento animal es impresionante 🦁")
                cantidad_respuestas_correctas += 1
                cantidad_respuestas_correctas_seguidas += 1
            else:
                print("¡Ups! Casi… pero no es la respuesta correcta 🐢")
                cantidad_respuestas_correctas_seguidas = 0
            time.sleep(1)
            print("                               |SEGUNDA PREGUNTA|")
            print()
            print("Tengo la capacidad de regenerar mis extremidades y tengo una apariencia única en forma de estrella.")
            print("Vivo en el océano y puedo ser de distintos colores. ¿Quién soy?")
            print()
            print("|1| Medusa")
            print("|2| Erizo de mar")
            print("|3| Estrella de mar")
            print("|4| Anémona")
            respuesta = int(input("Escoje la respuesta correcta → "))
            if respuesta == 3:
                print()
                print("!Perfecto! !Tu conocimiento de animales es asombroso! 🚀")
                cantidad_respuestas_correctas += 1
                cantidad_respuestas_correctas_seguidas += 1
            else:
                print("Lástima, no es el correcto. ¡No pasa nada, a por el siguiente! 🦦")
                cantidad_respuestas_correctas_seguidas = 0
            time.sleep(1)
            print("                               |TERCERA PREGUNTA|")
            print()
            print("Aunque muchos piensan que soy un oso, en realidad soy un marsupial. Tengo un pelaje espeso ")
            print("y me alimento principalmente de hojas de eucalipto. ¿Quién soy?")
            print()
            print("|1| Pereza")
            print("|2| Wallaby")
            print("|3| Panda")
            print("|4| Koala")
            respuesta = int(input("Escoje la respuesta correcta → "))
            if respuesta == 4:
                print()
                print("¡Acertaste! La respuesta es correcta. 🐨")
                cantidad_respuestas_correctas += 1
                cantidad_respuestas_correctas_seguidas += 1
            else:
                print("Casi le das, pero no es el animal. ¡Sigue intentándolo! 🐒")
                cantidad_respuestas_correctas_seguidas = 0
            time.sleep(1)
            print("                               |CUARTA PREGUNTA|")
            print()
            print("Puedo correr muy rápido sobre el agua por unos segundos para escapar de los depredadores.")
            print("Soy un reptil pequeño y me llaman “lagarto Jesucristo”. ¿Quién soy?")
            print()
            print("|1| Gecko")
            print("|2| Lagarto basilisco")
            print("|3| Camaleón")
            print("|4| Iguana verde")
            respuesta = int(input("Escoje la respuesta correcta → "))
            if respuesta == 2:
                print()
                print("¡Exactamente! Eres un maestro de los animales. 🦎")
                cantidad_respuestas_correctas += 1
                cantidad_respuestas_correctas_seguidas += 1
            else:
                print("Casi, pero no es el animal correcto. ¡No te rindas! 🐋")
                cantidad_respuestas_correctas_seguidas = 0
            time.sleep(1)
            print("                               |QUINTA PREGUNTA|")
            print()
            print("Tengo un cerebro con forma de rosquilla, y aunque tengo muchas patas, no soy un insecto.")
            print("Me enrollo cuando me siento amenazado. ¿Quién soy?")
            print()
            print("|1| Milpiés")
            print("|2| Ciempies")
            print("|3| Cucaracha")
            print("|4| Grillo")
            respuesta = int(input("Escoje la respuesta correcta → "))
            if respuesta == 1:
                print()
                print("¡Eso fue perfecto! ¡Bien pensado! 😁")
                cantidad_respuestas_correctas +=1
                cantidad_respuestas_correctas_seguidas += 1
                if cantidad_respuestas_correctas_seguidas >= 5 and bandera ==0:
                    print("                 5 RESPUESTAS CORRECTAS SEGUIDAS ERES UN GENIO ! 🧠")
                    bandera = 1
            else:
                print("Esta era difícil. ¡Prueba con el siguiente! 🦇")
                cantidad_respuestas_correctas_seguidas = 0
            time.sleep(1)
            print("                               |SEXTA PREGUNTA|")
            print()
            print("Mi nombre significa ‘pez del diablo’, y tengo una gran boca con un Anzuelo ")
            print("bioluminiscente para atraer presas en la oscuridad. Vivo en las profundidades del océano. ¿Quién soy?")
            print()
            print("|1| Tiburón linterna")
            print("|2| Pez globo")
            print("|3| Morena")
            print("|4| Pez rape")
            respuesta = int(input("Escoje la respuesta correcta → "))
            if respuesta == 4:
                print()
                print("¡Muy acertado! Parece que conoces a los animales a fondo. 🐠")
                cantidad_respuestas_correctas += 1
                cantidad_respuestas_correctas_seguidas += 1
                if cantidad_respuestas_correctas_seguidas >= 5 and bandera == 0:
                    print("                 5 RESPUESTAS CORRECTAS SEGUIDAS ERES UN GENIO ! 🧠")
                    bandera =1
            else:
                print("No es correcto, pero sigues en la jugada. ¡Ánimo! 💪🏼")
                cantidad_respuestas_correctas_seguidas = 0
            time.sleep(1)
            print("                               |SEPTIMA PREGUNTA|")
            print()
            print("Soy uno de los únicos mamíferos que pone huevos. Habito en Australia, tengo pico de pato y cola de castor. ¿Quién soy?")
            print()
            print("|1| Equidna")
            print("|2| Ornitorrinco")
            print("|3| Armadillo")
            print("|4| Wallaroo")
            respuesta = int(input("Escoje la respuesta correcta → "))
            if respuesta == 2:
                print()
                print("¡Eso es! Estás en el camino correcto. 🧐")
                cantidad_respuestas_correctas += 1
                cantidad_respuestas_correctas_seguidas += 1
                if cantidad_respuestas_correctas_seguidas >= 5 and bandera == 0: 
                    print("                 5 RESPUESTAS CORRECTAS SEGUIDAS ERES UN GENIO ! 🧠")
                    bandera = 1
            else:
                print("Esa no es la respuesta, pero lo estás haciendo bien. 🐌")
                cantidad_respuestas_correctas_seguidas = 0
            time.sleep(1)
            print("                               |OCTAVA PREGUNTA|")
            print()
            print("Soy un insecto que puede 'disparar' un líquido tóxico a temperaturas muy altas para defenderme de los depredadores.")
            print("Vivo en el suelo y a menudo en climas cálidos. ¿Quién soy?")
            print()
            print("|1| Termita")
            print("|2| Escorpión")
            print("|3| Escarabajo bombardero")
            print("|4| Grillo")
            respuesta = int(input("Escoje la respuesta correcta → "))
            if respuesta == 3:
                print()
                print("¡Sí! Sabía que lo lograrías. 😏")
                cantidad_respuestas_correctas += 1
                cantidad_respuestas_correctas_seguidas += 1
                if cantidad_respuestas_correctas_seguidas >= 5 and bandera == 0:
                    print("                 5 RESPUESTAS CORRECTAS SEGUIDAS ERES UN GENIO ! 🧠")
                    bandera = 1
            else:
                print("Uy, no es correcto, pero casi lo logras. ¡Vamos! 🦏")
                cantidad_respuestas_correctas_seguidas = 0
            time.sleep(1)
            print("                               |NOVENA PREGUNTA|")
            print()
            print("Soy el ave más pequeña del mundo, con un tamaño promedio de 5-6 cm. Puedo batir mis alas hasta 80 veces por segundo. ")
            print("¿Quién soy?")
            print()
            print("|1| Colibrí")
            print("|2| Pardillo")
            print("|3| Golondrina")
            print("|4| Canario")
            respuesta = int(input("Escoje la respuesta correcta → "))
            if respuesta == 1:
                print()
                print("¡Muy bien! Cada vez más cerca de la victoria. 🦜")
                cantidad_respuestas_correctas += 1
                cantidad_respuestas_correctas_seguidas += 1
                if cantidad_respuestas_correctas_seguidas >= 5 and bandera == 0:
                    print("                 5 RESPUESTAS CORRECTAS SEGUIDAS ERES UN GENIO ! 🧠")
                    bandera = 1
            else:
                print("Mmm, incorrecto, pero cada respuesta te hace aprender más.🤠")
                cantidad_respuestas_correctas_seguidas = 0
            time.sleep(1)
            print("                               |DECIMA PREGUNTA|")
            print()
            print("Cambio mi piel regularmente, tengo tres corazones y sangre de color azul. Soy un cefalópodo muy inteligente. ¿Quién soy?")
            print()
            print("|1| Sepia")
            print("|2| Anguila eléctrica")
            print("|3| Calamar")
            print("|4| Pulpo")
            respuesta = int(input("Escoje la respuesta correcta → "))
            if respuesta == 4:
                print()
                print("¡Exacto! ¡Con esta respuesta, completaste el desafío! ¡Felicidades! ")
                cantidad_respuestas_correctas += 1
                cantidad_respuestas_correctas_seguidas += 1
                if cantidad_respuestas_correctas_seguidas >=5 and bandera == 0:
                    print("                 5 RESPUESTAS CORRECTAS SEGUIDAS ERES UN GENIO ! 🧠")
                    bandera =1
            else:
                print("Uy, no era ese, pero has completado el juego. ¡Buen trabajo! 🐻‍❄️")
                cantidad_respuestas_correctas_seguidas = 0
            time.sleep(1)

    print()
    print()
    if dificultad == 1 or dificultad == 2 and comenzar == 1:
        print("                                 Calculando puntuacion . . . 🔄")
        time.sleep(1)

        if cantidad_respuestas_correctas >0:
            print("                     Obtuviste un total de ",cantidad_respuestas_correctas," Respuestas correctas")
            if cantidad_respuestas_correctas == 10:
                print("                             ERES UN ERUDITO DE ANIMALES!")
        
            if bandera == 1:
                print()
                print("                       !!Lograste responder 5 preguntas seguidas 🧠 !! ")
        else:
            print("           No obtuviste ninguna respuesta correcta, Estudia y vuelve a practicar!😀")
        if cantidad_respuestas_correctas == 10:
            print("¡Increíble! ¡Lo lograste! Has acertado todas las respuestas, eres un experto en animales 🤓. ¡Felicidades!")
        elif cantidad_respuestas_correctas >= 7:
            print("¡Excelente! Has demostrado un gran conocimiento sobre animales. ¡Sigue así, estás muy cerca de la perfección!")
        elif cantidad_respuestas_correctas <5:
            print("¡No te preocupes! Tienes mucho potencial. Sigue practicando y seguro mejorarás. ¡Intenta de nuevo!")
        

    print("                                 !JUEGO FINALIZADO !")

    print("                                 Volviendo al Menu. . . ")
    time.sleep(1)