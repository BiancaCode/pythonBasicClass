"""Tarea 9
Problema 1
Bianca
1. Escribir un programa que implemente una agenda. En la agenda se podrán guardar
nombres y números de teléfono. El programa nos dará el siguiente menú:
a. Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda,
debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto.
Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
b. Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos
cuyos nombres comiencen por dicha cadena.
c. Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la
agenda.
d. Listar: Nos muestra todos los contactos de la agenda."""
from pprint import pprint


def menu(d1):
    while True:

        op = int(input("\nMenu\n1 Anadir/Modificar \n2 Buscar \n3 Borrar \n4 Listar\n5 Salir\n>> "))

        if op == 1:
            nombre = input("Ingrese el nombre: ")
            numero = input("Ingrese el numero: ")
            d1[nombre] = numero
            pprint(d1)

        elif op == 2:
            nom = input("Ingrese el nombre: ")

            for nombre, numero in d1.items():

                if nombre.startswith(nom):
                    print(nombre, agenda[nombre])

            if nom not in d1:
                print("La busqueda no arrojo resultados")

        elif op == 3:
            nombre = input("Ingrese el nombre: ")

            if nombre in d1:
                resp = input("Desea Borrarlo S/N: ")

                if resp == "S":
                    del d1[nombre]
                    pprint(d1)

            else:
                print("El nombre no se encuentra en la agenda")

        elif op == 4:
            pprint(d1)

        elif op == 5:
            print("Fin del programa")
            break


agenda = {"Directorio": "102", "Policia": "104", "Emergencias": "911",
          "Bomberos": "103", "Sinaproc": "316-3200", "ATTT": "511-9320", "Bomberos Juan Diaz": "512-6148"}

menu(agenda)