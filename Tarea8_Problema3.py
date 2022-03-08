"""Tarea 8
Problema 3
Bianca
Se le solicita crear un programa que tenga un conjunto con nombre de colores.
El programa debe tener un menú con las siguientes opciones:
a. Utilizar el método pop e imprimir el resultado.
b. Copiar el conjunto original en un conjunto llamado colorcopia e imprimir el resultado
de colorcopia.
c. Eliminar un elemento del conjunto.
El usuario debe indicar cuando desea salir del programa."""


# --------------------------------Funciones--------------------------------------------------------------------------


def menu(c1):
    while True:

        op = int(input("\nMenu\n1 Imprimir \n2 Copiar \n3 Eliminar \n4 Salir: "))

        if op == 1:
            resultado = c1.pop()
            print("", resultado)
            print(c1)
        elif op == 2:
            colorcopia = c1.copy()
            print(colorcopia)
        elif op == 3:
            elemento = input("\nColor a eliminar: ")
            c1.remove(elemento)
            print(c1)
        elif op == 4:
            print("Fin del Programa")
            break


# ------------------------------------------------------------------------------------------------------------------


print("\nPrograma de colores")

colores = {"rosa", "celeste", "azul", "morado", "amarillo", "blanco", "verde", "lila"}

menu(colores)