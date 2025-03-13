'''
Crea un programa que realice los siguientes pasos imprimiendo la lista tras cada uno de ellos:

pida 5 palabras al usuario y las almacene en una lista.
pida al usuario un nuevo elemento y lo añada al final de la lista
pida al usuario una posición y elimine el elemento en esa posición. Si la posición no es válida se deben seguir pidiendo posiciones hasta que se introduzca una posición válida.
'''
print('Vas a introducir 5 palabras')
lista_palabra = []
numero = 1

for i in range(1, 6): 
    palabra = input(f'Introduce {numero} palabra: ')
    numero += 1
    lista_palabra.append(palabra)

print(f'Has introducido {len(lista_palabra)} y son estas: {lista_palabra}.')

print('Ahora vas a anadir una palabra nueva.')
palabra_nueva = input('Palabra nueva: ')
lista_palabra.append(palabra_nueva)

print(f'Esta es la nueva lista: {lista_palabra}')

print('Ahora vas a eliminar una position.')

for position, value in enumerate(lista_palabra):
    print(position, value)

elegir = int(input('Elige el numero que quieres eliminar: '))

while elegir != 0 and elegir != 5:
    elegir = int(input('Elige el numero que quieres eliminar: '))
else:
    print(f'Vale. Se eliminara la posicion {elegir} que seria la palabra {lista_palabra[elegir]}')
    del lista_palabra[elegir]
    print(f'La nueva lista es {lista_palabra}')
