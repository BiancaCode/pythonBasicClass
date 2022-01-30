"""Tarea 1 Problema 11
Bianca Gonzalez
Se desea un proqrama que calcule el monto a cobrar en una venta y el cambio que debe devolver
al cliente una vez realizado el paqo. Calcular el subtotal que sería la cantidad comprada ” precio
del producto, el impuesto (7%) que debe ser sumado al subtotal para obtener el monto a cobrar.
Finalmente indicar el dinero a devolver al cliente después de su pago. Es importante que su
proqrama imprima el subtotal, monto del impuesto, monto a cobrar, el paqo del cliente y el monto a
devolver."""

print("\n-Sistema de Cobro-\n")
cantidad = int(input("Cantidad: "))
precio = float(input("Precio: "))
subtotal = cantidad * precio
print ("Subtotal: %.2f"%subtotal)
print("Impuesto 7%%: %.2f"%(subtotal*0.07))
total = subtotal * 1.07
print("Total: %.2f"%total)
pago = float(input("Ingrese el pago: "))
cambio = pago - total
print("Cambio: %.2f" % cambio)