while True:
    from jugador import jugador_aleatorio
    from validar import validar_numero
    from sumar import sumar_numero

    print("Squid Games")
    print("Bienvenido al juego carrera 20")
    print(
        "Instrucciones: El jugador 1 deberas colocar un numero, ya sea 1 o 2, el numero que digites se iran acomulando y se sumaran con el numero (1 o 2) del jugador 2, el primero en conseguir que la sumatoria les de 20 gana "
    )
    print("Que empiece el juego")

    jugador_1 = input("Jugador 1, favor de escribir tu nombre: ")
    jugador_2 = input("Jugador 2, favor de escribir tu nombre: ")
    jugador_actual = jugador_aleatorio(jugador_1, jugador_2)

    print(jugador_actual, "Comenzaras")
    suma_parcial = 0

    while suma_parcial < 20:
        numero = input(f"{jugador_actual}, por favor escribe un número del 1 al 2: ")
        while not validar_numero(numero):
            print("Número inválido")
            numero = input(
                f"{jugador_actual}, por favor escribe un número válido del 1 al 2: "
            )
        suma_parcial = sumar_numero(suma_parcial, jugador_actual, numero)
        if suma_parcial >= 20:
            print(f"Felicidades {jugador_actual}, ¡ganaste!")
            break
        else:
            jugador_actual = jugador_1 if jugador_actual == jugador_2 else jugador_2

    while True:
        jugar_otra_vez = input("¿Quieres jugar otra vez? (si/no): ")
        if jugar_otra_vez.lower() == "si":
            break
        elif jugar_otra_vez.lower() == "no":
            print("Gracias por jugar. ¡Hasta la próxima!")
            exit()
        else:
            print("Respuesta inválida. Por favor escribe 'si' o 'no'")
