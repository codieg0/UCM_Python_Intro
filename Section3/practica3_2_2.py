'''
Escribe un programa que pida al usuario el nombre de un país europeo y, a continuación, escriba su población según la siguiente tabla.

España	Francia	Portugal	Alemania	Reino Unido
46M	    64M	    10M	        81M	        65M
Si el país introducido no está en la tabla anterior, el programa dirá que no conoce la población de ese país.

¿Se te ocurre como hacer que funcione independientemente de como escriba el usuario el nombre del país (mayúsculas, minúsculas o una mezcla de ambas)?

Pista: recuerda que puedes trasformar las cadenas a minúsculas, mayúsculas, etc.
'''
# Esto es un dictionario
paises = {"Espana": "46M", "Reino Unido": "65M", "Alemania": "81M", "Francia": "64M", "Portugal": "10M"}

pais = input('Pais: ')
paisNuevo = pais.capitalize()

if paisNuevo in paises:
    print(f'Este pais, {paisNuevo}, tiene {paises[paisNuevo]} de habitantes.')
else:
    print('No conozco el pais.')