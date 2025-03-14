'''
Escribe un programa que pida el nombre de un mes y devuelva el número de días que tiene ese mes. Te suena, ¿verdad? Pero en esta ocasión almacena los nombres de los meses que tienen el mismo número de días en una lista (meses con 30 y meses con 31 días) y verás como se simplifican las condiciones.
'''

dias_28 = {'febrero'}

dias_31 = {
    'enero', 'marzo', 'mayo', 'julio', 'agosto', 'octubre', 'diciembre'    
}

dias_30 = {
    'abril', 'junio', 'septiembre', 'noviembre'
}

mes = input('Mes: ')
nuevo_mes = mes.lower()

while nuevo_mes not in dias_28 and nuevo_mes not in dias_30 and nuevo_mes not in dias_31:
    print(f'{nuevo_mes} no es un mes, tarado!')
    mes = input('Introduzca el mes correcto: ')
    nuevo_mes = mes.lower()
    
if nuevo_mes in dias_28:
    print(f'El mes de {nuevo_mes.capitalize()} tiene 28 dias.')
elif nuevo_mes in dias_30:
    print(f'El mes de {nuevo_mes.capitalize()} tiene 30 dias.')
elif nuevo_mes in dias_31:
    print(f'El mes de {nuevo_mes.capitalize()} tiene 31 dias.')