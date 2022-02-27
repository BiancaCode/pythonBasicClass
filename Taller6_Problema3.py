"""3.	En una fábrica se proporcionan los datos de producción de 10 diferentes productos para el
año pasado. Tener dos listas paralelas.

Lista 1	Lista2
Producto	Costo de Producción
1	100,000.00
2	50,000 .00
3	55,000.00
4	150,000.00
5	78,000.00
6	45,000 .00
7	12,000.00
8	203,000.0 0
9	205,000.0 0
10	145,000.00

Construya un programa que pueda proporcionar la siguiente información:

•	El costo anual de producción.
•	Obtenga el costo de producción más alto.
•	Obtener el promedio del costo de producción.

"""
# -----------------------------------------------Bibliotecas----------------------------------------------------------

import statistics


# -------------------------------------------------------Funciones------------------------------------------------------

def costoAnual(lista):
    return sum(lista, 0)


def promedio(lista):
    return statistics.mean(lista)


def maximo(prod, cost):
    maxim = max(cost)
    indice = cost.index(maxim)
    return prod[indice], maxim

# ------------------------------------------------------------Listas----------------------------------------------------


producto = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
costo = [100000.00, 50000.00, 55000.00, 150000.00, 78000.00, 45000.00, 12000.00, 203000.00, 205000.00, 145000.00]


# ----------------------------------------------------------------------------------------------------------------------

print("\n Fabrica de Produccion\n")

costoproduccion = costoAnual(costo)
productoMasAlto, costoMasAlto = maximo(producto, costo)
promedioProduccion = promedio(costo)

print("Costo Anual: ", costoproduccion,
      "\nCosto de Produccion mas alto: ", productoMasAlto," ", costoMasAlto,
      "\nPromedio del Costo de produccion: ", promedioProduccion)