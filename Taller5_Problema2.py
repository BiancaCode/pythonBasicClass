"""Se desea un programa que lea dos números enteros. El programa debe indicar si el número1
es divisible por el número2."""

from tkinter import *


root = Tk()

root.title("Divisibles @bichicode")

root.resizable(True, True)

root.iconbitmap("bichi.ico")

miFrame = Frame()

miFrame.pack()

# --------------------------Variables---------------------------------------------------------------
TP = StringVar()


# _____________________________Funciones_____________________________________________________________

def obtener_valores():
    num1 = int(caja1.get())
    num2 = int(caja2.get())
    es_divisible(num1, num2)
    return


def es_divisible(n1, n2):
    modulo = n1 % n2
    if modulo == 0:
        mensaje = "Es Divisible"
    else:
        mensaje = "No Es Divisible"
    return TP.set(str(mensaje))


# -------------------------------------------------------------------------------------------------


etiqueta = Label(miFrame, text="Programa de Divisibilidad \n\n Favor ingresar numeros enteros")
etiqueta.grid(row=2, column=1, padx=55, pady=20, columnspan=2)


etiqueta1 = Label(miFrame, text="Primer Numero")
etiqueta1.grid(row=5, column=1, padx=30, pady=20)

caja1 = Entry(miFrame, justify="right")
caja1.grid(row=5, column=2, padx=30, pady=20)


etiqueta2 = Label(miFrame, text="Segundo Numero")
etiqueta2.grid(row=6, column=1, padx=30, pady=20)

caja2 = Entry(miFrame, justify="right")
caja2.grid(row=6, column=2, padx=30, pady=20)


caja3 = Entry(miFrame, textvariable=TP, justify="center")
caja3.grid(row=22, column=1, padx=30, pady=15, columnspan=2)


# -------------------------------------Botones--------------------------------------------------------------

boton1 = Button(miFrame, text="Evaluar", width=13, command=obtener_valores)
boton1.grid(row=9, column=2, padx=30, pady=20)


# -----------------------------------------------------------------------------------------------------------

miImagen = PhotoImage(file="pp.png")
firma = Label(miFrame, image=miImagen)
firma.grid(row=24, column=1, padx=10, pady=30, columnspan=2)

# -------------------------------------------------------------------------------------------------------------

root.mainloop()