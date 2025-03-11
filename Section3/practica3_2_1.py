'''
Escribe un programa que pida dos números enteros al usuario y, a continuación, imprima el menor de ellos.
'''

primerNumero = int(input('Numero entero: '))
segundoNumero = int(input('Numero entero: '))

if primerNumero == segundoNumero:
    print('Ambos numeros son iguales.')
elif primerNumero < segundoNumero:
    print(f'El numero menor es {primerNumero}')
else:
    print(f'El numero menor es {segundoNumero}')