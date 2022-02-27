"""Utilizando una función recursiva escribir los números de n a 1 descendentemente. Leer un
número entero positivo.
"""

from tkinter import *

root = Tk()

root.title("Comparar @bichicode")

root.resizable(True, True)

root.iconbitmap("bichi.ico")

myFrame = Frame()

myFrame.pack()

# ----------------------------Variables-------------------------
Lista = StringVar()
# ----------------------------Funciones-------------------------


def obtener_valores():

    n1 = int(caja1.get())
    contar(n1)

    return


def contar(n1, list=""):

    if n1 > 0:
        list = list + str(n1) + " "
        n1 = n1 - 1
        contar(n1, list)
    else:
        Lista.set(list)

    return

# -------------------------------------------------------------------


etiqueta = Label(myFrame, text="Programa de Lista de Numeros \n\n Favor Ingresar el Numeros")
etiqueta.grid(row=2, column=1, padx=55, pady=20, columnspan=2)


etiqueta1 = Label(myFrame, text="Numero")
etiqueta1.grid(row=3, column=1, padx=30, pady=20)

caja1 = Entry(myFrame, justify="right")
caja1.grid(row=3, column=2, padx=30, pady=20)


etiquetaresultado = Label(myFrame, text="Numeros")
etiquetaresultado.grid(row=15, column=1, padx=30, pady=20, columnspan=2)

cajaresultado = Entry(myFrame, justify="center", font="bold", textvariable=Lista)
cajaresultado.grid(row=17, column=1, padx=30, pady=15, columnspan=2)


# -----------------------Botones----------------------------------------

boton1 = Button(myFrame, text="Calcular", width=13, command=obtener_valores)
boton1.grid(row=10, column=2, padx=30, pady=20)

# ---------------------------------------------------------------------

miImagen = PhotoImage(file="pp.png")
firma = Label(myFrame, image=miImagen)
firma.grid(row=25, column=1, padx=10, pady=30, columnspan=2)


# ---------------------------------------------------------------------

root.mainloop()