# Numpy [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Black jack! [o algo parecido :)]

El objetivo es realizar una aproximación al juego de black jack,
el objetivo es generar una lista de 2 números aleatorios
entre 1 al 10 inclusive, y mostrar los "números" al usuario.

El usuario debe indicar al sistema si desea sacar más
números para sumarlo a la lista o no sacar más

A medida que el usuario vaya sacando números aleatorios que se suman
a su lista se debe ir mostrando en pantalla la suma total
de los números hasta el momento.

Cuando el usuario no desee sacar más números o cuando el usuario
haya superado los 21 (como la suma de todos) se termina la jugada
y se presenta el resultado en pantalla

BONUS Track: Realizar las modificaciones necesarias para que jueguen
dos jugadores y compitan para ver quien sacá la suma de números
más cercanos a 21 sin pasarse!
'''

import random

if __name__ == '__main__':
    print("Ahora sí! buena suerte :)")
    # A partir de aquí escriba el código que resuelve el enunciado
    # Leer el enunciado con atención y consultar cualquier duda
    print('¿Cuantos Juagadores seran?')
    print('Marque 1 para un jugaror')
    print('Marque 2 para dos jugarores')
    
    jugadores = str(input())

    while jugadores != '1' and jugadores != '2':
        print('Debes ingresar 1 o 2')
        jugadores = str(input())

    if jugadores == '1':
        numeros = [random.randint(1, 10) for x in range(2)]
        print('Los numeros que salieron son: ', numeros)
        print('Tienes un total de', sum(numeros), 'puntos')
        while sum(numeros) < 21:
            print("¿Deseas sacar otro numero?")
            print("Marca y si deseas sacar otro y n si no")
            tirar = str(input())
            while tirar != 'y' and tirar != 'n':
                print('Debes ingresar y o n')
                tirar = str(input())
            if tirar == 'y':
                numeros = numeros + [random.randint(1, 10) for x in range(1)]
                print('Los numeros que salieron son: ', numeros)
                print('Tienes un total de', sum(numeros), 'puntos')
            elif tirar == 'n':
                print('Tus puntos son:', sum(numeros))
                break
        print('Tus numeros fueron', numeros)
        if sum(numeros) <= 21:
            print('Tienes: ', sum(numeros), 'puntos')
        else:
            print('Perdiste!')
            print('Te pasaste!! Tus puntos fueron: ', sum(numeros))
    elif jugadores == '2':
        jugador_1 = str(input('Ingrese el nombre del jugador 1: '))
        jugador_2 = str(input('Ingrese el nombre del jugador 2: '))
        numeros_1 = [random.randint(1, 10) for x in range(2)]
        print('Los numeros que salieron son ', numeros_1, 'para:', jugador_1)
        print(jugador_1, 'tiene un total de', sum(numeros_1), 'puntos')
        numeros_2 = [random.randint(1, 10) for x in range(2)]
        print('Los numeros que salieron son ', numeros_2, 'para:', jugador_2)
        print(jugador_2, 'tiene un total de', sum(numeros_2), 'puntos')
        while sum(numeros_1) <= 21:
            print(jugador_1, "¿Deseas sacar otro numero?")
            print("Marca y si deseas sacar otro y n si no")
            tirar = str(input())
            while tirar != 'y' and tirar != 'n':
                print('Debes ingresar y o n')
                tirar = str(input())
            if tirar == 'y':
                numeros_1 = numeros_1 + [random.randint(1, 10) for x in range(1)]
                print('Los numeros que salieron son: ', numeros_1)
                print(jugador_1, 'Tiene un total de', sum(numeros_1), 'puntos')
            elif tirar == 'n':
                print(jugador_1, 'tus puntos son:', sum(numeros_1))
                break
        if sum(numeros_1) <= 21:
            print(jugador_1, 'tienes: ', sum(numeros_1), 'puntos')
        else:
            print(jugador_1, 'perdiste!')
            print('Te pasaste!! Tus puntos fueron: ', sum(numeros_1))
        print(jugador_2, 'tienes', sum(numeros_2))
        while sum(numeros_2) < 21:
            print(jugador_2, "¿Deseas sacar otro numero?")
            print("Marca y si deseas sacar otro y n si no")
            tirar = str(input())
            while tirar != 'y' and tirar != 'n':
                print('Debes ingresar y o n')
                tirar = str(input())
            if tirar == 'y':
                numeros_2 = numeros_2 + [random.randint(1, 10) for x in range(1)]
                print('Los numeros que salieron son: ', numeros_2)
                print(jugador_2, 'tiene un total de', sum(numeros_2), 'puntos')
            elif tirar == 'n':
                print(jugador_2, 'tus puntos son:', sum(numeros_2))
                break
        if sum(numeros_2) <= 21:
            print(jugador_2, 'tienes: ', sum(numeros_2), 'puntos')
        else:
            print(jugador_2, 'perdiste!')
            print('Te pasaste!! Tus puntos fueron: ', sum(numeros_2))
        if sum(numeros_1) > sum(numeros_2) and sum(numeros_1) <= 21 and sum(numeros_2) <= 21:
            print('El ganador es: ', jugador_1)
        elif sum(numeros_1) < sum (numeros_2) and sum(numeros_1) <= 21 and sum(numeros_2) <= 21:
            print('El ganador es: ', jugador_2)
        elif sum(numeros_1) <= 21 and sum(numeros_2) <= 21:
            print('Esto es un empate!!')
        elif sum(numeros_1) > 21:
            print('El ganador es: ', jugador_2)
        elif sum(numeros_2) > 21:
            print('El ganador es: ', jugador_1)
        elif sum(numeros_1) > 21 and sum(numeros_2) > 21:
            print('Perdieron los dos XD')
    print("terminamos")