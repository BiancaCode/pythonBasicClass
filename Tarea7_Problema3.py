"""Tarea 7
Problema 3
Bianca
Construya un programa que utilice una tupla con cinco nombres de países
luego de cada nombre extraiga
las 3 primeras posiciones y las inserta en otra tupla.
Finalmente imprima el contenido de ambas tuplas de la siguiente forma:
PAN-PANAMA
COL-COLOMBIA
VEN-VENEZUELA
"""
print("\n Programa de Paises\n")

tupla = ("PANAMA", "COLOMBIA", "VENEZUELA", "NICARAGUA", "MEXICO")

lista = []

for pais in tupla:
    pais2 = pais[0:3] + "-" + pais
    lista.append(pais2)

tupla2 = tuple(lista)

print(tupla2)

