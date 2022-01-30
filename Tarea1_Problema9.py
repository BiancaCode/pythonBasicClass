"""Tarea 1 Problema 9
Bianca Gonzalez
El examen de una materia es el 70% de la nota total. Las lecciones constituyen el 20% y las
tareas el 10% de la nota total. Inqrese como datos la nota del examen calificado sobre 100 puntos,
la nota de una lección calificada sobre 10 puntos, y las notas de tres tareas calificadas cada una
sobre 10 puntos. Calcule la calificación total sobre 100 puntos."""

print("\n-Sistema de Calculo de Calificación Final-\n")
examen = int(input("Ingrese la calificación del examen: "))
leccion = int(input("Ingrese la calificación de la lección: "))
tarea1 = int(input("Ingrese la calificación de la tarea 1: "))
tarea2 = int(input("Ingrese la calificación de la tarea 2: "))
tarea3 = int(input("Ingrese la calificación de la tarea 3: "))
calificacion= examen * 0.7 + (leccion * 10 ) * 0.2 + ( ( (tarea1 + tarea2 + tarea3) * 10) / 3) * 0.1
print("La Calificación total es: %.2f"%calificacion)

