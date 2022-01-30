"""Tarea 2 Problema 5
Bianca Gonzalez
Escriba un programa aue le solicite al usuario que ingrese una frase y un carácter que será
utilizado para reemplazar los espacios en blanco que contiene la frase.
."""

print("\n -Programa Para Reemplazar Los Espacios En Blanco- \n")
s1 = input("Introduzca la cadena: ")
c = input("Introduzca el caracter que reemplazará el espacio: ")
print("Nueva Cadena: " + s1.replace(" ", c))
a = s1.find(" ")
if a == -1:
    print("No se realizó cambio alguno porque \"" + s1 + "\" no contiene espacios en blanco")
