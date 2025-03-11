'''
Escribe un programa que pida una frase al usuario (por ejemplo, Hoy va a ser un gran día) y a continuación:

La escriba en minúsculas (HOY VA A SER UN GRAN DÍA).
La escriba en mayúsculas (hoy va a ser un gran día).
La escriba poniendo sólo la primera letra de cada palabra en mayúsculas (Hoy Va A Ser Un Gran Día).
Escriba sólo los 6 primeros caracteres de la frase en mayúsculas (HOY VA)
Escriba los primeros 6 caracteres en mayúsculas y el resto en minúsculas (HOY VA a ser un gran día)
Indique si la frase contiene la letra u. (True)
'''

frase = input('Frase: ')

print(frase.lower())
print(frase.upper())
print(frase.title())
print(frase[0:7].upper())
print(frase[0:7].upper() + frase[7:].lower())
print('u' in frase)
