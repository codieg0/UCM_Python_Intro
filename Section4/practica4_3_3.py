'''
Pide varias palabras al usuario hasta que escriba la palabra ‘fin’ 
y después imprime sólo las que empiezan por ‘a’ o ‘A’ en el mismo orden en el que las escribió.
'''

lista_palabra = []

palabra = input('Palabra: ')

while palabra != 'fin':
    if palabra[0] == 'a' or palabra[0] == 'A':
        lista_palabra.append(palabra)
        print(f'Esta es la lista de palabras {lista_palabra}.')
    else:
        print('Ninguna palabra que empiece por a o A.')
        
    palabra = input('Palabra: ')

print(f'Las palabras que empiezan por a o A son {lista_palabra}')