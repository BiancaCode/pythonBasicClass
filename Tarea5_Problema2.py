"""Se desea un programa que convierta millas a kilómetros. Una milla equivale a 1.609344
kilómetros."""

from tkinter import *

root = Tk()

root.title("mi -> km @bichicode")

root.resizable(True, True)

root.iconbitmap("bichi.ico")

MiFrame = Frame()

MiFrame.pack()

# ----------------------------Variables-------------------------

Valor = StringVar()


# ----------------------------Funciones-------------------------


def obtener_valores():
    numero1 = float(caja1.get())

    validar(numero1)

    return


def validar(n1):

    resp = n1 * 1.609344

    return Valor.set((str(resp)) + " km")


# -----------------------------------------------------------------


titulo = Label(MiFrame, text="Programa de Conversion \n\n Convertir Millas a Kilometros")
titulo.grid(row=2, column=1, padx=55, pady=20, columnspan=2)

num1 = Label(MiFrame, text="Millas")
num1.grid(row=3, column=1, padx=30, pady=20)

caja1 = Entry(MiFrame, justify="right")
caja1.grid(row=3, column=2, padx=30, pady=20)


etiquetaresultado = Label(MiFrame, text="Resultado")
etiquetaresultado.grid(row=15, column=1, padx=30, pady=20, columnspan=2)

cajaresultado = Entry(MiFrame, justify="center", font="bold", textvariable=Valor)
cajaresultado.grid(row=17, column=1, padx=30, pady=15, columnspan=2)

# -----------------------Botones----------------------------------------


boton1 = Button(MiFrame, text="Evaluar", width=13, command=obtener_valores)
boton1.grid(row=10, column=2, padx=30, pady=20)

# ---------------------------------------------------------------------

miImagen = PhotoImage(file="pp.png")
firma = Label(MiFrame, image=miImagen)
firma.grid(row=25, column=1, padx=10, pady=30, columnspan=2)

# ---------------------------------------------------------------------

root.mainloop()