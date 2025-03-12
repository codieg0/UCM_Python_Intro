'''
Escribe un programa que pregunte al usuario un nombre de mes y escriba el número de días que tiene. El nombre del mes puede estar escrito en mayúsculas, minúsculas o una combinación de ambas. Consideraremos que el año no es bisiesto y por tanto febrero siempre tiene 28 días. Si el usuario introduce un mes que no existe el programa mostrará un mensaje indicando que no conoce ese mes.

A continuación, se muestran varios ejemplos de ejecución:

Introduzca el nombre del mes: enero
enero tiene 31 días.
Introduzca el nombre del mes: Abril
Abril tiene 30 días
Introduzca el nombre del mes: JuNiO
JuNiO tiene 30 días
Introduzca el nombre del mes: diciemb
No conozco ese mes

El nombre del mes debe aparecer exactamente como lo escribió el usuario al indicar el número de días.

Cuando termines el ejercicio, entrega el fichero .py con el código del programa a través del Campus para que te lo corrijamos. La entrega para este ejercicio se llama Entrega del Ejercicio 2.
'''

# Escribimos los meses y le asignamos el numero de dias
enero = 31
febrero = 28
marzo = 31
abril = 30
mayo = 31
junio = 30
julio = 31
agosto = 31
septiembre = 30
octubre = 31
noviembre = 30
diciembre = 31

# Pedimos al usuario que escriba el mes. Recordar que el mes debe aparecer exactamente como lo escribió el usuario

mes = input('Introduzca el nombre del mes: ')

nuevo_mes = mes.lower()

if nuevo_mes == 'enero':
    print(f'El mes de {mes} tiene {enero} dias.')
elif nuevo_mes == 'febrero':
    print(f'El mes de {mes} tiene {febrero} dias')
elif nuevo_mes == 'marzo':
    print(f'El mes de {mes} tiene {marzo} dias.')
elif nuevo_mes == 'abril':
    print(f'El mes de {mes} tiene {abril} dias.')
elif nuevo_mes == 'mayo':
    print(f'El mes de {mes} tiene {mayo} dias.')
elif nuevo_mes == 'junio':
    print(f'El mes de {mes} tiene {junio} dias.')
elif nuevo_mes == 'julio':
    print(f'El mes de {mes} tiene {julio} dias.')
elif nuevo_mes == 'agosto':
    print(f'El mes de {mes} tiene {agosto} dias.')
elif nuevo_mes == 'setptiembre':
    print(f'El mes de {mes} tiene {septiembre} dias.')
elif nuevo_mes == 'octubre':
    print(f'El mes de {mes} tiene {octubre} dias.')
elif nuevo_mes == 'noviembre':
    print(f'El mes de {mes} tiene {noviembre} dias.')
elif nuevo_mes == 'diciembre':
    print(f'El mes de {mes} tiene {diciembre} dias.')
else:
    print('No conozco ese mes.')