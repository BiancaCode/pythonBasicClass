"""l.	Realizar un programa que utilice dos listas paralelas.
En una lista almacenan los minutos utilizados por un grupo de N nadadores en una competencia de 100 metros libre y
otra lista en donde se almacenarán los nombres de los nadadores. Los datos de los minutos y de los nombres deben ser
suministrados por el usuario.

Para clasificar su tiempo debe ser menor o igual a un minuto y treinta segundos.
El algoritmo debe calcular e imprimir lo siguiente:

•	El promedio General del Grupo
•	Número de nadadores aprobados y reprobados
•	Porcentaje de nadadores aprobados y reprobados
•	Nadador con el mejor tiempo
"""
# --------------------------------------------Funciones-----------------------------------------------------------------
import statistics


def puntajes():

    tiempos = []
    nombres = []

    n = int(input("Ingrese cantidad de nadadores>> "))

    for i in range(n):
        dato = input("Ingrese el tiempo formato mm:ss >> ")

        if dato[1] == ":":
            minutos = int(dato[0])
        else:
            minutos = int(dato[0:2])
        segundos = int(dato[3:5])
        t = (minutos * 60) + segundos

        tiempos.append(t)

        nombre = input("Ingrese el nombre: ")
        nombres.append(nombre)

    return tiempos, nombres


def promedio(tiempos):
    tsegundos = statistics.mean(tiempos)
    minutos = int(tsegundos / 60)
    segundos = int(tsegundos - (minutos * 60))
    formato = str(minutos) + ":" + str(segundos)
    return formato


def porcentaje(ap, re):
    pa = (ap / (ap + re)) * 100
    pre = 100 - pa
    print("Porcentaje de Aprobados: %.2f" % pa, "%")
    print("Porcentaje de Reprobados: %.2f", pre, "%")


def clasificar(tiempos):
    aprobados = reprobados = 0

    for t in tiempos:
        if t < 90:
            aprobados += 1
        else:
            reprobados += 1

    porcentaje(aprobados, reprobados)
    return aprobados, reprobados


def mejor(nombres, tiempos):
    ganador = min(tiempos)
    indice = tiempos.index(ganador)
    return nombres[indice]


# ----------------------------------------------------------------------------------------------------------------------


print("Programa de la piscina")

marca, nadador = puntajes()

pro = promedio(marca)

print("El promedio general del grupo es ", pro)

aprob, repro = clasificar(marca)

print("Cantidad de aprobados", aprob, "cantidad de reprobados", repro)

# ------- Me faltan los porcentajes

campeon = mejor(nadador, marca)

print("El nadador con mejor tiempo es ", campeon)
