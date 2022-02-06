"""Tarea 3 Problema 5
Bianca Gonzalez
En un concurso hay tres jueces. La opinión del juez es 1 si está a favor y 0 si está en contra.
Para que un participante pueda continuar en el concurso debe tener al menos dos votos
favorables. Escriba un algoritmo que lea los votos de los tres jueces y muestre el resultado
mediante un mensaje: CONTINUA o ELIMINADO. No sume votos. Debe compararlos."""

print("\n Concurso \nPrograma de Suma de Votos\n")
voto1 = int(input("Ingrese el voto del juez 1: "))
voto2 = int(input("Ingrese el voto del juez 2: "))
voto3 = int(input("Ingrese el voto del juez 3: "))

if (voto1 == 1 and voto2 == 1) or (voto1 == 1 and voto3 == 1) or (voto2 == 1 and voto3 == 1):
    print("CONTINUA")
else:
    print("ElIMINADO")