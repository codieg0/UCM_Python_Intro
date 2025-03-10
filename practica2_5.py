'''
Los ingleses utilizan en su día a día sistemas métricos distintos de los que usamos nosotros. Por ejemplo, 1 milla son 5280 pies y 1.60934 kilómetros.

Escribe un programa que, dado un valor de distancia en millas, imprima el valor equivalente en pies y en kilómetros.
'''

millas = input("Cuantas millas has corrido? ")

pies = 5280 * millas

km = 1.60934 * millas

print(f'Has corrido {pies} pies y {km} kms')