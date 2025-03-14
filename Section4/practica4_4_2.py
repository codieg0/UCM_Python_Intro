'''
Crea un conjunto con los nombres de los meses. Después pide nombres de meses al usuario e indica, para cada uno de ellos, si es un nombre de mes válido o no usando la operación de pertenencia a conjuntos.
'''

meses = {'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', \
    'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'}

mes = input('Mes: ')
nuevo_mes = mes.lower()

while nuevo_mes != 'fin':

    if nuevo_mes in meses:
        print(f'Mes {nuevo_mes.capitalize()} existe!')
    else:
        print(f'El mes {nuevo_mes} no existe.')

    mes = input('Mes: ')