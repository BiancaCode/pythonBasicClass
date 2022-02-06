"""
Tarea 3 Problema 4
Bianca Gonzalez
El índice de masa corporal IMC de una persona se calcula con la fórmula IMC=P/T2 en donde
P es el peso en Kg. y T es la talla en metros.
Lea un valor de P y de T, calcule el IMC y muestre su estado según la siguiente tabla:
IMC Estado
Menos de 18.5 Desnutrido
18.5 a 25.5 Peso Normal
Más de 25.5 Sobrepeso
"""

print("\n -Programa de IMC- \n")
p = float(input("Ingrese el peso en kg: "))
t = float(input("Ingrese la talla en metros: "))
imc = p / (t * 2)
print("Su IMC es: %.2f" % imc)
if (imc > 0) and (imc < 18.5):
    print("Desnutrido")
elif (imc >= 18.5) and (imc <= 25.5):
    print("Peso normal")
elif imc > 25.5:
    print("Sobrepeso")
else:
    print("Error de datos favor vuelva a ingresar")