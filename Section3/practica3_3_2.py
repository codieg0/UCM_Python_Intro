'''
Escribe un programa que solicite al usuario un número par entre 10 y 20 o un número impar entre 40 y 50. El programa debe comprobar que el número cumple todas las condiciones usando una única expresión y escribir un mensaje en la consola indicando si el número es válido.

Pista: puedes saber si un número es par comprobando si el resto de la división entera al dividirlo por 2 es 0. Es decir, x es par si x % 2 == 0.
'''

numero = int(input('Introduce un numero par entre 10 y 20 o un numero impar entre 40 y 50: '))

if (10 <= numero <= 20 and numero % 2 == 0) or (40 <= numero <= 50 and numero %2 != 0):
    print(f'Tu numero {numero} esta en el rango que se propuso. Gracias!')
else:
    print(f'Tu numero no esta en ela rango que se pidio. Hasta luego!')