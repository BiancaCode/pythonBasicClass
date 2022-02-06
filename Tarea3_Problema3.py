"""
Tarea 3
Problema3
El número de pulsaciones que debe tener una persona por cada 10 segundos de ejercicio
aeróbico se calcula con la fórmula:
Género femenino (1): número de pulsaciones = (220 - edad en años)/10
Género masculino (2): número de pulsaciones = (210 - edad en años)/10
"""

print("\n Programa de numero de Pulsaciones\n")
genero = int(input("Ingrese un número según su género \n 1 para femenino \n 2 para masculino \n>> "))
edad = int(input("Ingrese su edad en años: "))

if genero == 1:
    pulsaciones = (220 - edad) /10
elif genero == 2:
    pulsaciones = (210 - edad) /10
else:
    print("Error de datos favor volver a ingresar al programa")
    exit()

print("El numero de pulsaciones que debe tener por cada 10 segundos es de: ", pulsaciones)
