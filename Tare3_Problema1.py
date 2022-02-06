""""
Tarea3 Problema 1
Bianca Gonzalez
Cree un programa que lea la cantidad de Kw que ha consumido una familia y el precio por Kw.
Si la cantidad es mayor a 700, incremente el precio en 5% para el exceso de Kw sobre 700.
Muestre el valor total a pagar.
"""

print("Programa Valor Total A Pagar Según Consumo de Kw")
precio = float (input("Ingrese el precio por kw: "))
kw = float(input("Ingrese la cantidad de kw consumidos: "))

if (kw > 0) and (kw <= 700):
    total = kw * precio
elif kw > 700:
    total = (700 * precio) + ((kw-700) * (precio * 1.05))
else:
    print("Error: Favor ingrese los datos con el formato correcto")

print("El valor total a pagar es: %.2f:" % total)


