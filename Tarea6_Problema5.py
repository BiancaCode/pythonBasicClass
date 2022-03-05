"""
Tarea 6
Problema 5
Bianca
5.	Se desea un programa que lea la temperatura promedio diaria por 7 días. El programa debe
permitir realizar lo siguiente:
•	Conocer el promedio de las temperaturas
•	Presentar la lista de forma ordenada
•	Presentar la mayor de las temperaturas
•	Presentar la menor de las temperaturas.

"""
from statistics import mean

# ------------------------------Funciones--------------------------------------------------------------------


def menu(temp, dias):
    while True:
        op = int(input("\nMenus\n1 Promedio de Temperaturas\n2 Lista de Forma ordenada\n3 Mayor de las temperaturas\n"
                       "4 Menor de las temperaturas\n5 Salir >>"))
        if op == 1:
            print(mean(temp), "°")
        elif op == 2:
            listacaracter = []
            for t in range(7):
                caracter = str(temp[t])+"°"
                listacaracter.append(caracter)
            lista = sorted(listacaracter)
            print(lista)
        elif op == 3:
            mayor = max(temp)
            indice = temp.index(mayor)
            print("La mayor de las temperaturas es: ", mayor, "° ", dias[indice])
        elif op == 4:
            menor = min(temp)
            indice = temp.index(menor)
            print("La menor de las temperaturas es: ", menor, "° ", dias[indice])
        elif op == 5:
            print("Fin del programa")
            break
    return

# ----------------------------------------------------------------------------------------------------------


temperaturas = []
semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sabado", "domingo"]

print("Programa de temperatura\nIntroduzca la temperatura en grados ejemplo 24°\n")

for t in range(7):
    toma = input(f"Temperatura del, {semana[t]}: ")
    toma = float(toma.replace("°", ""))
    temperaturas.append(toma)

menu(temperaturas, semana)







