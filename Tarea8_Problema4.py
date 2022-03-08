"""Tarea 8
Problema 4
Bianca
Se le solicita crear un programa que tenga un conjunto con nombres para mascotas.
El programa debe tener un menú con las siguientes opciones:
a. Adicionar un elemento al conjunto.
b. Conocer el número de elementos que tiene el conjunto.
c. Limpiar el conjunto.
Con cada opción seleccionada el programa debe imprimir el conjunto.
El usuario debe indicar cuando desea salir del programa."""

# --------------------------------Funciones--------------------------------------------------------------------------
from pprint import pprint


def menu(c1):
    while True:

        op = int(input("\nMenu\n1 Adicionar \n2 Numero de Elementos \n3 Limpiar \n4 Salir: "))

        if op == 1:
            nombre = input("Ingrese el nuevo nombre: ")
            c1.add(nombre)

        elif op == 2:
            print("Cantidad de elemento: ", len(c1))

        elif op == 3:
            c1.clear()

        elif op == 4:
            print("Fin del Programa")
            break

        pprint(c1)

# -------------------------------------------------------------------------------------


mascotas = {"Bella", "Luna", "Lucy", "Daizy", "Zoe", "Lily", "Lola", "Bailey", "Stella", "Molly"}
menu(mascotas)