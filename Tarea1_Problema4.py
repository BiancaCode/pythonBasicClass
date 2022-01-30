"""Tarea1 Problema 4
Bianca Gonzalez
Dado la velocidad de 2 cuerpos que se dirigen uno al encuentro de otro determinar el tiempo de
encuentro si la distancia aue los se para inicialmente es “D”.
va = velocidad del cuerpo a
vb = velocidad del cuerpo b
D = distancia aue separa “a” de “b”
te = d/(va +vb)"""

print("\n -Sistema De Calculo Del Tiempo de Encuentro-\n")
va = float(input("Introduzca la velocidad del cuerpo a: "))
vb = float(input("Introduzca la velocidad del cuerpo b: "))
D = float(input("Introduzca la distancia que separa ""a"" de ""b"": "))
te = D/(va + vb)
print("El tiempo de encuentro es de: %.2f" % te)
