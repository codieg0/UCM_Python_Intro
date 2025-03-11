'''
Escribe un programa que pida al usuario el valor del radio y a continuación imprima la longitud de la circunferencia y el área del círculo asociados. Te recordamos las fórmulas matemáticas que debes usar:
longitudcircunferencia = 2 * pi * radio
areacirculo = pi * radio * radio
Recuerda que el valor aproximado de pi es 3.14159. La ejecución debería ser similar a la siguiente:
Introduzca la longitud del radio: 2
La longitud de la circunferencia es 12.56636
El área del círculo es 12.56636
Cuando termines el ejercicio, entrega el fichero .py con el código del programa a través 
del Campus para que te lo corrijamos. 
La entrega para este ejercicio se llama Entrega del Ejercicio 1
'''

# Pedimos al usuario que introduxca la longitud del radio.
valorRadio = float(input('Introduzca la longitud del radio: '))

# Valor de pi
pi = 3.14159

# Formulas
longitudCircunferencia = 2 * pi * valorRadio
areaCirculo = pi * (valorRadio ** 2)

# Imprimimos la info
print(f'La longitud de la circunferencia es: {longitudCircunferencia}')
print(f'El area del circulo es {areaCirculo}')