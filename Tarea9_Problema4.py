"""Tarea 9
 Problema 4
 Cree un programa que le permita obtener la clave para el valor mínimo que se encuentra
en el diccionario."""

print("\nPrograma para obtener la clave para el valor mínimo\n")

diccionario = {"Bianca": 100, "Astrid": 61, "Leopoldo": 80, "Maria": 95}

minimo = (min(diccionario.items()))

print(minimo[0])
