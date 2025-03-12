'''
Escribe un programa que calcule la nota media de un alumno dadas las notas de sus dos exámenes parciales. El alumno estará suspenso si no ha aprobado ambos parciales.
'''

nota_uno = float(input('Primer examen: '))
nota_dos = float(input('Segundo examen: '))

if (nota_uno or nota_dos) < 4:
    print(F'Solo con aprobar un examen no vale')
elif 5 <= (nota_uno and nota_dos) <= 10:
    nota_final = (nota_uno + nota_dos) / 2
    print(f'Yuhu! Well done mate! You got {nota_final}.')
else:
    print('You dont even know whats yer name mate. On yer bike!')