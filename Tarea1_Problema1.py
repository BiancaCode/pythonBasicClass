"""Tarea1 Problema1
Bianca Gonzalez

Se requiere que elabore un programa para calcular el salario de un empleado. Para ello debe
solicitar al usuario que inqrese las horas laboradas en el mes, así como la tarifa por hora. El
programa debe calcular el salario a pagar y debe imprimirlo.
"""

print("-Sistema de Calculo de Salario")
horas_laboradas = float (input ("Ingrese las horas laboradas en el mes: "))
tarifa = float(input("Ingrese la tarifa por hora: "))
salario = horas_laboradas * tarifa
print("Salario calculado es de: %.2f"%salario + "$")
