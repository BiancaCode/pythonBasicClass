"""Tarea 7
Problema 5
Bianca
5.	En una sala de urgencias se lleva el registro histórico de la cantidad de pacientes
que han ingresado en los últimos 6 meses.
El hospital está realizando un análisis para determinar en cuántos meses registran la necesidad de mayor personal
en enfermería para atender las urgencias.
Para este análisis es necesario conocer los meses en los cuales
la cantidad de paciente superó el promedio de la cantidad de pacientes que ingres3ron.

El programa debe presentar los datos en formato tabular indicando
el número del registro histórico,
la cantidad ingresos,
la cantidad de pacientes superior al ingreso
y el mensaje se requiere mayor personal de enfermería.
"""
from pprint import pprint
from statistics import mean

historico = (500, 480, 620, 400, 500, 550)

promedio = round(mean(historico), 2)
superior = 0
mensaje = ""
lista = []


for num, mes in enumerate(historico):
    if mes > promedio:
        superior = round(mes - promedio, 2)
        mensaje = " Se requiere mayor personal de enfermeria"
    else:
        superior = 0
        mensaje = ""
    lista.append(str(num+1) + " Pacientes " + str(mes) + " Excedente " + str(superior) + mensaje)

proyeccion = tuple(lista)

pprint(proyeccion)


