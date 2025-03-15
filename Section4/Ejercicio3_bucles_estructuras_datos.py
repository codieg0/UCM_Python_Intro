'''
Escribe un programa que te ayude a llevar un registro de tus gastos. 
El programa te hará 3 preguntas para cada gasto: el motivo, el lugar y la cantidad. 
Tras cada gasto introducido, el programa te preguntará si quieres introducir otro gasto más. 
Al finalizar, el programa debe imprimir todos los gastos en el mismo orden que los introdujiste 
y la cantidad total de dinero gastado.

A continuación, mostramos un ejemplo de cómo debería funcionar tu programa:

--------
Quieres introducir más gastos (si/no): si
Motivo del gasto: camiseta
Lugar del gasto: El Corte Inglés
Cantidad gastada: 15
Quieres introducir más gastos (si/no): si
Motivo del gasto: fruta
Lugar del gasto: mercado
Cantidad gastada: 20
Quieres introducir más gastos (si/no): no

Gastos:
camiseta en El Corte Inglés : 15.0 euros
fruta en mercado : 20.0 euros
Cantidad total : 35.0 euros
--------

La información de cada gasto la debes almacenar como un diccionario con 3 claves de tipo cadena: 
motivo, lugar y cantidad. Para almacenar la secuencia de gastos debes usar una lista. 
Es decir, la estructura de datos que almacena la información es una lista 
donde cada elemento es un diccionario.

Como este ejercicio es un poco más complicado que los anteriores, a continuación, 
te proponemos la estructura que debería tener tu programa. 
Al escribir el programa deberás traducir cada línea en una o más instrucciones Python.

--------
crear lista de gastos vacía
preguntar al usuario si quiere introducir más gastos
mientras haya más gastos
    pedir datos del gasto al usuario
    crear diccionario con la información del gasto
    añadir el diccionario a la lista de gastos
    preguntar al usuario si quiere introducir más gastos

cantidad_total = 0
para cada gasto en la lista de gastos:
    imprimir información del gasto
    acumular la cantidad del gasto en cantidad_total

imprimir cantidad_total
--------

Cuando termines el ejercicio, entrega el fichero .py con el código del programa 
a través del Campus para que te lo corrijamos. 
La entrega para este ejercicio se llama Entrega del Ejercicio 3
'''

gastos = []

preguntar = input('Quieres introducir más gastos (si/no): ')
preguntar.lower()

while preguntar == 'si':

    motivo = input('Motivo del gasto: ')
    lugar = input('Lugar del gasto: ')
    cantidad = float(input('Cantidad gastada: '))

    dict_gastos = {'motivo' : motivo, 'lugar' : lugar, 'cantidad' :cantidad}
    gastos.append(dict_gastos)

    preguntar = input('Quieres introducir más gastos (si/no): ')
    preguntar.lower()

    if preguntar == 'no':
        print('Gastos:')
        for gasto in gastos:
            print(f'{gasto["motivo"]} en {gasto["lugar"]}: {gasto["cantidad"]} euros')

        total = sum(gasto["cantidad"] for gasto in gastos)
        print(f'Cantidad total : {total} euros.')