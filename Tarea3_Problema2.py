"""
Tarea 3 Problema 2
Bianca Gonzalez
Crear un programa que lea el número de llantas de una compra y debe mostrar el monto a
pagar. El almacén las vende con la siguiente política: Si se compran menos de 5 llantas, el
precio unitario es 80. Si se compran 6 o 7, el precio unitario es 70, y si se compran más de 7
llantas, el precio unitario es 60.
"""

print("\nPrograma de Precio de Llantas\n")
llantas = int(input("Ingrese la cantidad de llantas: "))

if (llantas > 0) and (llantas <= 5):
    total = llantas * 80.00
elif llantas == 6 or llantas == 7:
    total = llantas * 70.00
elif llantas > 7:
    total = llantas * 60.00
else:
    print("Error de datos favor volver a ingresar")
    exit()

print("Monto a pagar: %.2f" % total)