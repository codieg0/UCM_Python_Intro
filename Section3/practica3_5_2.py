'''
Casi todo el mundo piensa que los años bisiestos son los divisibles por 4 (por ejemplo, 1988, 1992 y 1996 son años bisiestos). Pero existe una excepción a esa regla: los años divisibles por 100 sólo son bisiestos sin además son divisibles por 400. Por ese motivo el año 1600 es bisiesto pero el 1700 no lo es.

Haz un programa que pida un año al usuario e indique si es bisiesto.
'''

anyo = int(input('Intrudece un año bisiesto: '))

if anyo % 4 == 0 and anyo % 100 == 0 and anyo % 400 == 0:
    print('El año es bisiesto.')
else:
    print('Wise up. El año no es bisiesto.')