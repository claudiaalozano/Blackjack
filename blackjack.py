from random import choice, sample

cartas = {
    chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,
}

print("Cartas: {}".format(" ".join(cartas.keys())))
print("Puntos: {}".format(list(cartas.values())))

print("1\ Iteración estándar sobre un diccionario")
for carta, valor in cartas.items():
    print("la carta {} vale {}".format(carta, valor))

print("2\ Iteración ordenada sobre un diccionario")
for carta in sorted(cartas.keys()):
    print("la carta {} vale {}".format(carta, cartas[carta]))

print("3\ Black Jack")
lista_cartas = list(cartas)

while True:
    print("Ha seleccionado:", end=" ")
    carta = choice(lista_cartas)
    score = cartas[carta]
    print(carta, end=" ")
    carta = choice(lista_cartas)
    score += cartas[carta]
    print(carta, end=" ")
    print(" >>> su puntuación es de", score)

    main_banca = sample(lista_cartas, 2)
    score_banca = sum(cartas[carta] for carta in main_banca)
    print("La banca tiene: {} {}  >> su score es {}".format(main_banca[0], main_banca[1], score_banca))

    numero_partida= int(input("Cuantas partidas quieres jugar: "))
    contador= 0


    if score_banca == score:
        contador= contador + 1
        numero_partida= numero_partida - 1
        print("Habeis empatado, vuelva a jugar." , "Número de partidas jugadas: " , contador , "." , "Te quedan " , numero_partida , " partidas")
        jugar= input("¿Quieres volver a jugar? (si/no): ")
        if jugar ==  "no":
            print("Gracias por jugar.")
            break

    if score_banca > score: 
        contador= contador + 1
        numero_partida = numero_partida - 1
        print("Has perdido, vuelva a jugar." , "Número de partidas jugadas: " , contador , "." , "Te quedan" , numero_partida , " partidas")
        jugar= input("¿Quieres volver a jugar? (si/no): ")
        if jugar ==  "no":
            print("Gracias por jugar.")
            break
    else:
        contador = contador + 1
        print("Has ganado." , "Número de partidas jugadas: " , contador)
        jugar= input("¿Quieres volver a jugar? (si/no): ")
        if jugar ==  "no":
            print("Gracias por jugar.")
            break