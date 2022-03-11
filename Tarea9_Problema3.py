"""Tarea9
Problema 3
Bianca
Cree un programa que le permita remover las claves que se encuentran en la lista del
diccionario.
"""
from pprint import pprint

print("Programa que permite remover las claves de un diccionario")

diccionario = {"Directorio": "102", "Policia": "104", "Emergencias": "911",
          "Bomberos": "103", "Sinaproc": "316-3200", "ATTT": "511-9320", "Bomberos Juan Diaz": "512-6148"}

pprint(diccionario)

clave = input("\n Ingrese la clave a eliminar: ")

if clave in diccionario:

    del diccionario[clave]

    pprint(diccionario)

else:

    print("\nLa clave no se encuentra en el diccionario")