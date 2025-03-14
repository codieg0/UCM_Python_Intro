'''
Escribe un programa que calcule la nota final de un alumno a partir de las calificaciones de los 3 exámenes parciales que ha realizado, teniendo en cuenta que el primer examen parcial vale un 20% , el segundo un 30% y el último un 50% de la nota final.
'''

valorPrimerExamen = float(input('Valor del primer examen: '))
valorSegundoExamen = float(input('Valor del primer examen: '))
valorUltimoExamen = float(input('Valor del primer examen: '))


primerExamen = valorPrimerExamen * 0.20
segundoExamen = valorSegundoExamen * 0.30
ultimoExamen = valorUltimoExamen * 0.50

notaFinal = primerExamen + segundoExamen + ultimoExamen

print(f'Tu nota final es {notaFinal:.2f}')