'''
Escribe un programa que calcule el volumen de un cono a partir del radio de la base y su altura. Usa la siguiente fórmula:
volumen = (pi * radio * altura)/3
Solicita los valores de radio y altura al usuario. Recuerda que el valor aproximado de pi es 3.14159.
'''
pi = 3.14159
radio = float(input('Radio: '))
altura = float(input('Altura: '))

volumen = float((pi * radio * altura) / 3)

print(f'El volumen del cono es {volumen:.2f}')