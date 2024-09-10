import random


def obtener_palabra_secreta() -> str:
    palabras = [
        "quimera",
        "colorario",
        "catalejo",
        "simpatia",
        "cuaderno",
        "perro",
        "casa",
    ]
    return random.choice(palabras)


def mostar_progreso(palabra_secreta, letras_adivinadas):
    adivinado = ""

    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_"
    return adivinado


def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 6
    juego_terminado = False

    print("¡Bienvenidos al juego del ahorcado!")
    print(f"Tenés {intentos} intentos para adivinar la palabra secreta")
    print(
        mostar_progreso(palabra_secreta, letras_adivinadas),
        "La cantidad de letras de la palabra es:",
        len(palabra_secreta),
    )

    while (
        not juego_terminado and intentos > 0
    ):  # me asegura que las letras que ingresen sean en minuscula
        adivinanza = input("Introduce una letra: ").lower()

        # chequea si no es una letra
        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Por favor introduzca sólo una letra")
        elif adivinanza in letras_adivinadas:
            print("Ya has usado esa letra, por favor intenta con otra")
        else:
            letras_adivinadas.append(adivinanza)

            if adivinanza in palabra_secreta:
                print(
                    f"¡Excelente, has adivinado!. La letra '{adivinanza}' esté en la palabra secreta"
                )
            else:
                intentos -= 1
                print(f"La letra '{adivinanza}' no está presente en la palabra secreta")
                print(f"Te quedan {intentos} intentos")

        progreso_actual = mostar_progreso(palabra_secreta, letras_adivinadas)
        print(progreso_actual)

        if "_" not in progreso_actual:
            juego_terminado = True
            palabra_secreta = palabra_secreta.capitalize()  # para ponerla destacada
            print(
                f"¡Felicitaciones, has ganado! La palabra secreta es: '{palabra_secreta}'"
            )
    if intentos == 0:
        palabra_secreta = palabra_secreta.capitalize()  # para ponerla destacada
        print(
            f"Se te han acabo los intentos, la palabra secreta es: '{palabra_secreta}'"
        )


juego_ahorcado()
