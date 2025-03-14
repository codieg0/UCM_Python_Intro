'''
Crea un diccionario que contenga como claves los nombres de los números del 1 al 10 en español (uno, dos, …) 
y como valores los nombres de los mismos números en inglés (one, two, …). 
Después pide al usuario números en español y muéstrale su traducción al inglés.
'''

espanol = {
    1 : 'uno',
    2 : 'dos',
    3 : 'tres',
    4 : 'cuatro',
    5 : 'cinco',
    6 : 'seis',
    7 : 'siete',
    8 : 'ocho',
    9 : 'nueve',
    10 : 'diez'
}

ingles = {
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'ten'
}

# Pedir al usuario un numero en espanol y mostrarle la traduccion al ingles

numero = int(input('Un numero del 1 al 10: '))

if numero in espanol:
    print(f'El numero {numero} es {ingles[numero]} en ingles.')
else: 
    print(f'No se ese {numero}.')