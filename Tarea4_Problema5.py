"""
Tarea 4 Problema 5.
Bianca Gonzalez
Calcule el promedio, el menor valor y el mayor valor de los pesos de n paquetes en una bodega.
Estos datos ingresan uno a la vez dentro de un ciclo. n es un dato ingresado al inicio.

"""
n = int(input("Ingrese la cantidad de paquetes: "))
mayor = 0
peso = float(input("Peso: "))
suma = peso
menor = peso
for i in range(1, n):
    if peso >= mayor:
        mayor = peso
    elif peso <= menor:
        menor = peso
    peso = float(input("Peso: "))
    suma = suma + peso

print("El promedio es: ", suma/n)
print("El menor es: ", menor, "El mayor es: ", mayor)
