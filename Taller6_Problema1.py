"""
Taller 6
Problema 1
Bianca
l.	Realizar un programa que permita almacenar N elementos en una lista. Después de almacenar los elementos en la lista
el programa debe permitir realizar las siguientes acciones:
•	Mostrar la lista
•	Agregar un elemento a la lista
•	Eliminar un elemento a la lista
"""
# --------------------------------------------FUNCIONES-----------------------------------------------------------------

def mostrarLista(l):
    print(l)

def agregarElemento(l):
        elemento = input("Ingrese el nuevo elemento: ")
        l.append(elemento)
        mostrarLista(l)

def eliminarElemento(l):
    elemento = input("Ingrese el elemento a eliminar: ")
    l.remove(elemento)
    mostrarLista(l)


# ----------------------------------------------------------------------------------------------------------------------


print("\n\nPrograma que almacena y permite manipular una lista\n")
lista = list(input("Ingrese la lista: "))
while True:
    opcion = int(input("Menu\n1: Ver Lista\n2: Agregar elemento\n3: Eliminar elemento\n4: Salir:>> "))
    if opcion == 1:
        mostrarLista(lista)
    elif opcion == 2:
        agregarElemento(lista)
    elif opcion == 3:
        eliminarElemento(lista)
    elif opcion == 4:
        print("Fin del Programa")
        break
    else:
        print("Opcion Invalida")

