import random

billete = 0

print("Bienvenido a mi rol espacial\n")
print("Estás caminando un día por la noche y te dan un golpe y te secuestran\n")
print("Te encuentras que te han dejado en una habitación, ves una puerta y una ventana medio rota\n")

h1 = input("¿Qué haces?\n"
           "A. Salir por la ventana\n"
           "B. Intentar salir por la puerta\n"
           "C. Intentar buscar objetos\n")

if h1 == "A":
    h2 = input("Le das un puñetazo para acabar de romper la ventana para poder pasar, pero te haces sangre y oyes que viene gente hacia ti, ¿Qué haces?\n"
               "A. Me hago el muerto\n"
               "B. Me intento pelear con ellos\n"
               "C. Vuelvo por donde he vuelto e intento esconderme\n")
    if h2 == "A":
        print("Pasar desapercibido por los guardias pensando que estás muerto, pero te viene una rata que ha olido la sangre y te muerde, lo cual te infecta y te mata\n")
    elif h2 == "B":
        print("Te intentas pelear con los guardias, pero van armados y te disparan, mueres\n")
    else:
        print("Te da tiempo a esconderte, pero los guardias ven el rastro de sangre y mueres\n")

elif h1 == "B":
    h11 = input("Intentas salir por la puerta pero te das cuenta de que está cerrada, ¿Qué haces?\n"
                "A. Intentar tirar la puerta abajo\n"
                "B. Echarme a llorar\n")
    if h11 == "A":
        print("Los guardias lo oyen, entran y te disparan, has muerto\n")
    else:
        print("¿Qué te esperas conseguir llorando? Te oyen los guardias y mueres\n")

elif h1 == "C":
    h11 = input("Te encuentras una llave que se habían dejado los guardias, un móvil de concha, ¿qué haces?\n"
                "A. Cojo solo la llave\n"
                "B. Cojo solo el móvil\n"
                "C. Cojo los dos\n"
                "D. Sigo buscando\n")
    if h11 == "A":
        # Pregunta del guardia
        numero_aleatorio = random.randint(1, 10)
        respuesta_usuario = int(input(f"El guardia te pregunta: ¿Cuánto es 5 * {numero_aleatorio}? "))
        respuesta_correcta = 5 * numero_aleatorio

        if respuesta_usuario == respuesta_correcta:
            print("¡Has acertado! El guardia te deja vivir.")
            billete = 1
        else:
            print("Has respondido incorrectamente. El guardia te dispara y mueres.\n")

    elif h11 == "B":
        print("Coges el móvil y intentas llamar, pero no hay cobertura y los guardias te oyen intentar llamar y te matan\n")
    elif h11 == "C":
        busqueda = input("Sigues buscando y te encuentras dos billetes de 50€, ¿los coges? (S/N)\n")
        if busqueda == "S":
            billete = 1
            objetos = input("¿Quieres coger el resto de objetos? (S/N)\n")
            if objetos == "S":
                dinero = input("Te diriges a la puerta y la abres, te encuentras a dos guardias, ¿qué haces?\n"
                               "A. Me voy corriendo dentro y cierro la puerta\n"
                               "B. Intento correr y rezar que no me disparen\n"
                               "C. Me quedo quieto\n")
                if billete == 1:
                    print("Te quedas quieto pero los guardias ven que tienes dinero, te piden el dinero y te dejan salir\n"
                          "Usas el teléfono para poder llamar y volver a tu casa")
                else:
                    print("Te quedas quieto, los guardias no te ven como una amenaza y te permiten salir\n"
                          "Usas el teléfono para poder llamar y volver a tu casa")

            else:
                print("¿Qué suponías que iba a pasar solo cogiendo el dinero? ¿Que se abriría un portal?")
        else:
            print("Decides no coger el billete y los guardias, al ver que no tienes nada valioso, te disparan y mueres\n")

else:
    print("Tiene que ser A, B o C alcornoque")
