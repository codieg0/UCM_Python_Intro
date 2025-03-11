'''
Escribe un programa que solicite al usuario la base y la altura de un triángulo y calcule su área (base * altura / 2). Si alguno de los datos introducidos no es válido (por ejemplo, altura negativa o cero) debe mostrar un mensaje de error y no hacer ningún cálculo.
'''

base = float(input('Base: '))
altura = float(input('Altura: '))

area = base * altura / 2

if (base or altura) <= 0:
    print('Por favor, no hay que ser inutil. Ponga un numero mayor que 0.')
else:
    print(f'El area del triangulo es {area:.2f}')