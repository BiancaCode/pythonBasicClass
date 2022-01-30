"""Tarea 1 Problema 6
Bianca Gonzalez
Determine la distancia entre dos puntos en el espacio. (x1,y1, z1) y(x2, y2, z2)
dis((z2—z1)^2+(y2—y1)^2+(x2—x1)^2)^0.5"""

print("\n - Sistema que calcula la distancia entre dos puntos en el espacio - \n")
x1 = float(input("introduzca el valor x1: "))
y1 = float(input("introduzca el valor y1: "))
z1 = float(input("introduzca el valor z1: "))
x2 = float(input("introduzca el valor x2: "))
y2 = float(input("introduzca el valor y2: "))
z2 = float(input("introduzca el valor z2: "))
dis = ((z2 - z1)**2 + (y2 - y1)**2 + (x2 - x1)**2)**0.5
print("La distancia es: %.2f" % dis)