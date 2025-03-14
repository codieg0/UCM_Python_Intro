'''
Escribe un programa que, dada una lista, elimine todos los elementos duplicados. 
No nos importa el orden en el que aparezcan los elementos en la lista final.
'''

lista = []

for i in range(1, 10):
    numero = int(input('Introduce 10 numeros naturales [positivos o negativos]: '))
    lista.append(numero)

print('Hemos removido los numeros negativos')

duplicados = set(lista)

print(f'Tu lista tiene {len(duplicados)} elementos.')

print(f'Esta es la nueva lista curada: {duplicados}')