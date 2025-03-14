'''
Escribe un programa que clasifique los elementos de una lista en positivos y negativos. 
Los elementos positivos deben añadirse a una lista y los negativos a otra. 
Si la lista original contiene ceros, se deben ignorar.
'''

lista_original = [1, 3, -40, -2, 2, 2, -6, 81]

lista_positiva = []
lista_negativa = []

for numero in lista_original:
    if numero > 0:
        lista_positiva.append(numero)
    elif numero < 0:
        lista_negativa.append(numero)

print(f'Lista positiva: {lista_positiva}')
print(f'Lista negativa: {lista_negativa}')