"""Tarea 9
Problema 5
Bianca
Crear un programa que implemente el uso de diccionario para guardar los precios de las
distintas frutas. El programa pedirá el nombre de la fruta y la cantidad que se ha vendido
y nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario.
Si la fruta no existe nos mandará un error. Tras cada consulta el programa nos preguntará
si queremos realizar otra consulta.
"""
diccionario = {"pera": 1.50, "manzana": 1.20, "uvas": 5.00, "banana": 1.00}

print("\nPrograma de Precios de las Frutas\n")

while True:

    nombre = input("Nombre de la fruta: ")

    cantidad = int(input("Cantidad que se ha vendido: "))

    if nombre not in diccionario:

        print("Error")

    else:

        preciofinal = diccionario[nombre] * cantidad

        print("El precio final es: %.2f" % preciofinal)

    resp = input("\nDesea realizar otra consulta si/no: ")

    if resp == "no" or resp == "No" or resp == "NO":

        break
