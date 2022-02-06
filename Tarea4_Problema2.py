"""
Tarea 4 Problema 2.
Bianca Gonzalez
Solicitar al usuario un número entero positivo. El programa debe escribir los números entre
el número ingresado y uno menos del doble del mismo.
"""
while True:
    entero = int(input("Ingrese un entero positivo: "))
    if entero > 0:
        for n in range(entero, (entero * 2)):
            print(n)
        break
    else:
        print("\nError de datos, favor vuelva a ingresar el número \n ")

