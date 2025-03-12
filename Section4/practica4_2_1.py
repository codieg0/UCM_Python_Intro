'''
Vuelve a hacer el ejercicio de imprimir la suma de los números naturales, pero esta vez pregunta al usuario desde qué número quiere empezar a sumar y hasta que número quiere llegar. Por ejemplo, si el usuario introduce los números 5 y 10, el programa debe calcular 5+6+7+8+9+10.
'''

numero_inicio = int(input('Numero que quieres empezar: '))
numero_final = int(input('Numero que quieres acabar: '))

suma = 0 
for i in range(numero_inicio, numero_final+1):
    suma = suma + i

print(f'La suma de todos los numeros es {suma}')