'''
Escribe un programa que imprima la tabla de multiplicar de un número introducido por el usuario usando una instrucción for. Por ejemplo, si el usuario introduce el 7, el programa debe imprimir la tabla del 7.
'''

numero = int(input('Numero: '))

for i in range(1, 11):
    multiplicacion = numero * i
    print(f'La tabla del numero {numero} por {i} es {multiplicacion}')