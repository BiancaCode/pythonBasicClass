"""Tarea 7
Problema 4
Bianca

En un almacén se tiene el registro de las ventas de los últimos 12 meses (histórico). Almacenar
el histórico en una tupla. El almacén desea realizar una proyección de ventas para los siguientes 12 meses.
Se tiene que los meses 3. 6 y 12 tienen generalmente en promedio un incremento del 4%,
los meses 1,4, 5 y 7 tienen un incremento del 1.5%
el resto de los meses tienen un incremento aproximado del 0.8 %.
Presentar 13 proyección para los siguientes 12 meses y dejarlos almacenados en una lista.
Al finalizar el programa debe presentar la venta histór ica y la venta proyecta para cada uno de los meses.

"""
print("\nPrograma de proyeccion de un almacen\n")

historico = (1500.00, 5000.00, 4000.00, 2000.00, 5000.00, 2000.00,
             2000.00, 1500.00, 5000.00, 4000.00, 2000.00, 5000.00)

proyeccion = []

for count, mes in enumerate(historico):
    if count+1 == 3 or count+1 == 6 or count+1 == 12:
        valor = mes * 1.04
    elif count+1 == 1 or count+1 == 4 or count+1 == 5 or count+1 == 7:
        valor = mes * 2.5
    else:
        valor = mes * 1.008

    proyeccion.append(valor)

for indice, mes in enumerate(proyeccion):
    print("Mes", indice+1, "Historico", historico[indice], "Proyeccion", mes)






