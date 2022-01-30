"""Tarea 1 Problema 8
Bianca Gonzalez
Dado un dato con la cantidad de días. Encuentre el equivalente en meses, semanas y días
sobrantes. Suponqa que cada mes tiene treinta días.
Ejemplo. Si el dato es 175 el resultado será 5 meses, 3 semanas y 4 días"""

print("\n -Sistema de Calculo de Meses, Semanas y Días-\n")
d = int(input("Ingrese la cantidad de días: "))
meses = d // 30
semanas = (d % 30) // 7
dias = (d % 30) % 7
print("Meses: "+ str (meses) + "\nSemanas: "+ str (semanas)+"\nDías: "+ str(dias))
