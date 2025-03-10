'''
Ejercicios para practicar
Haz un programa que pida al usuario su nombre y escriba el número de letras que contiene.

Haz un programa que pida al usuario la longitud de un lado de un cuadrado e imprima su perímetro y su área.
'''

nombre = input("Escriba su nombre: ")
print(f"Tu nombre es {nombre.capitalize()} y contiene {len(nombre)} letras.")

long_cuadrado = int(input("Longitud de un lado de un cuadrado: "))

perimetro = 4 * long_cuadrado
area = long_cuadrado ** 2

print(f"El perimetro del cuadrado es {perimetro}")
print(f'El aread del cuadrado es {area}')