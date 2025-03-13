'''
Escribe un programa que pida un número al usuario, calcule su factorial usando una instrucción for, y lo imprima. Recuerda que el factorial de un número se define así:
                        n! = 1 * 2 *3... * n
'''

numero = int(input('Introduce un numero entero: '))

factorial = 1

for i in range(1, numero + 1):
    factorial = factorial * i

print(f'El factorial de {numero}! es {factorial}')