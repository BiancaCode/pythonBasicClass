"""
2.	Crear una lista con 10 númercs. Los números deben ser solicitados al usuar-io. Con los
datos que se tiene en la lista realiza r las siguientes operaciones:
•	Calcular el promedio.
•	Indicar cuántos números son mayores al promedio.
•	Indicar cuántos números son menores al promedio.
•	Indicar cuántos números son iguales al promedio.
"""


# --------------------------------------------------------Funciones-----------------------------------------------------


def llenar():
    lista = []
    for i in range(0, 10):
        lista.append(int(input("Ingrese el elemento: ")))
    return lista


def promedio(lista):
    s = sum(lista, 0)
    return int(s/10)


def evaluar(lista, prom):
    mayores = menores = iguales = 0
    for i in lista:
        if i > prom:
            mayores += 1
        elif i < prom:
            menores += 1
        else:
            iguales += 1
    print("\nPromedio :", prom)
    return mayores, menores, iguales


# ----------------------------------------------------------------------------------------------------------------------

print("\nPrograma de lista de 10 numeros\n")
lista10 = llenar()
mayor, menor, igual = evaluar(lista10, promedio(lista10))
print("Mayores:", mayor, " Menores ", menor, " Iguales ", igual)
