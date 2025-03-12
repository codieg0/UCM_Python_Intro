'''
Escribe un programa que solicite al usuario 3 palabras e imprima la que contenga más caracteres. En caso de varias palabras tengan el máximo número de caracteres, puedes imprimir cualquiera de ellas.
'''

palabra_uno = input('Primera palabra: ')
palabra_dos = input('Segunda palabra: ')
palabra_tres = input('Tercera palabra: ')

nuevaPalabra_uno = len(palabra_uno)
nuevaPalabra_dos = len(palabra_dos)
nuevaPalabra_tres = len(palabra_tres)

if nuevaPalabra_uno >= max(nuevaPalabra_dos, nuevaPalabra_tres):
    print(f'La palabra con mas letras es {palabra_uno} con {nuevaPalabra_uno} letras.')
elif nuevaPalabra_dos >= max(nuevaPalabra_uno, nuevaPalabra_tres):
    print(f'La palabra con mas palabras es {palabra_dos} con {nuevaPalabra_dos} palabras.')
else:
    print(f'La palabra con mas letras es {palabra_tres} con {nuevaPalabra_tres} letras.')