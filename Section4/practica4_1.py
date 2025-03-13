'''
Escribe un programa que pida palabras al usuario hasta que introduzca alguna que comience por la letra a (mayúscula o minúscula). Antes de finalizar, el programa indicará el número total de palabras introducidas.

Pistas:

Recuerda que puedes acceder a un carácter particular de una cadena usando el operador corchete [].
Necesitarás una variable para contar palabras que deberás incrementar cada vez que pidas otra palabra.
'''

palabra = input('Introduzca palabra que empiece con a: ')
while palabra[0] != 'a' and palabra[0] != 'A':
    palabra = input('Nos quedamos aqui hasta que pongas una palabra que empiece por a, hombre ya!: ')

print(f'Tu palabra tiene {len(palabra)} letras.')