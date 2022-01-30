"""Tarea 1 Problema 10
Bianca Gonzalez
Construya un programa que dado el radio y la altura de un cilindro calcule e imprima el área y
su volumen.
Volumen = p ”radio” altura"""
import math

print("\n -Sistema de Area y Volumen de un Cilindro-\n")
radio = float(input("Ingrese el radio = "))
altura = float(input("Ingrese la altura = "))
area = 2 * math.pi * radio * (radio + altura)
volumen = math.pi * (radio ** 2) * altura
print("Área = %.2f" % area + "\nVolumen = %.2f"%volumen)