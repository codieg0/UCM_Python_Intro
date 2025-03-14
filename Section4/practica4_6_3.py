'''
Escribe un programa que almacene las notas obtenidas por cada alumno en clase. 
El profesor introducirá cada vez el nombre de un alumno y una de sus notas. 
Al final del programa se mostrarán las notas obtenidas por cada uno de los alumnos.

Observa que este ejemplo es un poco más complejo porque usamos un diccionario 
donde las claves son los nombres de los alumnos y el valor asociado a cada clave es una lista de enteros. 
Es decir, cuando recuperamos el valor asociado a un alumno, lo que conseguimos es una lista.
'''

notas_alumnos = {}

for i in range(1, 6):
    alumno = input('Alumno: ')
    nota = float(input('Nota: '))
    notas_alumnos[alumno] = nota

suspensos = {}
aprovados = {}

for alumno, nota in notas_alumnos.items():
    if nota < 5:
        suspensos[alumno] = nota
    elif 5 <= nota <= 10: 
        aprovados[alumno] = nota

print('Los alumnos suspendidos son: ')
for alumno, nota in suspensos.items():
    print(alumno, nota)

print('Los alumnos aprovados son: ')
for alumno, nota in aprovados.items():
    print(alumno, nota)