"""Tarea8
Problema1
Bianca
Se le solicita crear un programa que tenga dos conjuntos formados por nombres de
países.
El programa debe permitir realizar las siguientes acciones:
a. Indicar si el segundo conjunto es subconjunto del primero.
b. Presentar la intersección de los conjuntos.
c. Presentar la diferencia de los conjuntos. """

america = {"Panama", "Canada", "Chile", "Nicaragua", "Mexico"}
centroamerica = {"Panama", "Costa Rica", "Nicaragua", "El Salvador", "Belice"}

print("\nPrograma de conjunto de paises\n")

print("Resultado de subconjuto: ", centroamerica.issubset(america))

print("Interseccion: ", america & centroamerica)

print("Diferencia: ", america ^ centroamerica)