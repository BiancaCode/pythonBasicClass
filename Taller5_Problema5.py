"""Se desea un programa que lea una cadena y una letra. El programa debe indicar si la letra
leída se encuentra en la cadena. Utilizar una función en la implementación de la solución.
"""

from tkinter import *

root = Tk()

root.title("Encontrar Caracter @bichicode")

root.resizable(True, True)

root.iconbitmap("bichi.ico")

myFrame = Frame()

myFrame.pack()

# ----------------------------Variables-------------------------
Mensaje = StringVar()
# ----------------------------Funciones-------------------------
def obtener_valores():
    cadena = str(caja1.get())
    caracter = str(caja2.get())
    busqueda(cadena, caracter)
    return

def busqueda(s1, c):
    var = s1.find(c)
    if var == -1:
        m = "No se encontro"
    else:
        m = "Si se encontro"
    return Mensaje.set(m)

# -------------------------------------------------------------------


etiqueta = Label(myFrame, text="Programa de Busqueda de Caracter\n\n Favor ingresar los datos solicitados")
etiqueta.grid(row=2, column=1, padx=55, pady=20, columnspan=2)


etiqueta1 = Label(myFrame, text="Ingrese la cadena")
etiqueta1.grid(row=3, column=1, padx=30, pady=20)

caja1 = Entry(myFrame, justify="right")
caja1.grid(row=3, column=2, padx=30, pady=20)


etiqueta2 = Label(myFrame, text="Ingrese el caracter a buscar")
etiqueta2.grid(row=5, column=1, padx=30, pady=20)

caja2 = Entry(myFrame, justify="right")
caja2.grid(row=5, column=2, padx=30, pady=20)


etiquetaresultado = Label(myFrame, text="Promedio")
etiquetaresultado.grid(row=15, column=1, padx=30, pady=20, columnspan=2)

cajaresultado = Entry(myFrame, justify="center", font="bold", textvariable=Mensaje)
cajaresultado.grid(row=17, column=1, padx=30, pady=15, columnspan=2)


# -----------------------Botones----------------------------------------

boton1 = Button(myFrame, text="Aceptar", width=13, command=obtener_valores)
boton1.grid(row=10, column=2, padx=30, pady=20)

# ---------------------------------------------------------------------

miImagen = PhotoImage(file="../Taller5/pp.png")
firma = Label(myFrame, image=miImagen)
firma.grid(row=25, column=1, padx=10, pady=30, columnspan=2)


# ---------------------------------------------------------------------

root.mainloop()