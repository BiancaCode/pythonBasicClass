"""Tarea 9
Problema 2
Bianca
Cree un programa en Python que combine dos diccionarios.
"""
from pprint import pprint

agenda = {"Directorio": "102", "Policia": "104", "Emergencias": "911",
          "Bomberos": "103", "Sinaproc": "316-3200", "ATTT": "511-9320", "Bomberos Juan Diaz": "512-6148"}

diccionario = {'nombre': 'Marta', 'apellido': 'Perez', 'edad': 46, 'cedula': '8-88-88'}

print("Programa que combina dos diccionarios\n")

diccionario.update(agenda)

pprint(diccionario)

