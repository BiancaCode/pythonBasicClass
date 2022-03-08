"""Tarea 8
Problema 2
Bianca

 Se le solicita crear un programa que tenga dos conjuntos formados por nombres de
personas.
El programa debe tener un menú con las siguientes opciones:
a. Realizar la operación de unión. Imprimir el resultado de la unión
b. Comparar si los dos conjuntos son iguales y enviar un mensaje del resultado de la
comparación.
c. Realizar la operación de diferencia. Imprimir el resultado de la operación.
El usuario debe indicar cuando desea salir del programa."""

# ---------------------------------Librerias------------------------------------------------------------------------

from pprint import pprint

# --------------------------------Funciones--------------------------------------------------------------------------


def menu(s1, s2):
    while True:

        op = int(input("\nMenu\n1 Unir \n2 Comparar \n3 Diferencia \n4 Salir: "))

        if op == 1:
            print("\nUnion")
            pprint(s1 | s2)

        elif op == 2:
            print("\nEl resultado de la comparacion es: ", s1 == s2)

        elif op == 3:
            print("\nDiferencia", s1 ^ s2)

        elif op == 4 :
            print("Fin del Programa")
            break


# ------------------------------------------------------------------------------------------------------------------


print("\nPrograma de conjuntos de nombres")

nombres1 = {"Liam", "Lyam", "Lucas", "Loukas", "Lukas", "Mateo", "Matheo", "Levi", "Aiden", "Aaiden"}

nombres2 = {"Thiago", "Matías", "Ian", "Lucas", "Dylan", "Luis", "Juan", "Eithan", "Carlos", "Liam",
            "Josué"}

menu(nombres1, nombres2)