'''
Pide al usuario 10 palabras y almacénalas en un conjunto usando un bucle. Imprime después el número de palabras distintas introducidas por el usuario.
'''

palabra = input('Palabra: ')

lista_palabras = []

inicializacion = 1

for i in range(1, 11):
    palabra = input('Palabra: ')
    lista_palabras.append(palabra)
    inicializacion += i

print(f'Esta es el conjunto de palabras: {set(lista_palabras)}')