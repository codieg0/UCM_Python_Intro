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

# Correccion

- Agrupa los meses que tienen el mismo número de días usando condiciones compuestas para conseguir que el programa quede más compacto. Si lo piensas con cuidado, sólo hay 4 posibilidades.

- En este caso no tiene sentido usar variables con el número de días porque sólo se utilizan en un punto del programa y no es un valor que vaya a cambiar. Escribe directamente el número de días en el mensaje.

TIENES QUE REPETIR EL EJERCICIO. Envía una nueva versión teniendo en cuenta los comentarios de la corrección, por favor.
'''

# Pedimos al usuario que escriba el mes. Recordar que el mes debe aparecer exactamente como lo escribió el usuario

mes = input('Introduzca el nombre del mes: ')
nuevo_mes = mes.lower()

if nuevo_mes == 'enero' or nuevo_mes == 'marzo' or nuevo_mes == 'mayo'\
    or nuevo_mes == 'julio' or nuevo_mes == 'agosto' \
    or nuevo_mes == 'octubre' or nuevo_mes == 'diciembre':
    print(f'Es mes de {mes} tiene 31 dias.')
elif nuevo_mes == 'febrero':
    print(f'El mes de {mes} tiene 28 dias.')
elif nuevo_mes == 'abril' or nuevo_mes == 'junio' or nuevo_mes == 'septiembre'\
    or nuevo_mes == 'noviembre':
    print(f'El mes de {mes} tiene 30 dias.')
else:
    print(f'No conozco el mes de {mes}')