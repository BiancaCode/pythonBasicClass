""" Se desea un programa que lea la cantidad comprada de un producto y el precio. El programa
debe suministrar el total a pagar.
TP = CANTIDAD*PRECIO"""

from tkinter import *

root = Tk()

root.title("Total a Pagar @Bichicode")

root.resizable(True, True)

root.iconbitmap("bichi.ico")

miFrame = Frame()

miFrame.pack()

# miFrame.config(width="650", height="750")

# --------------------------Variables-----------------------------------
TP = StringVar()


# --------------------------Funciones-----------------------------------

def total_pagar():
    total = float(cajacant.get()) * float(cajaprecio.get())
    return TP.set(str(total))

# -----------------------------------------------------------------------


etiqueta1 = Label(miFrame, text="Programa de Facturación \n\n Favor ingresar los datos del producto")
etiqueta1.grid(row=2, column=1, padx=55, pady=20, columnspan=2)


etiquetacant = Label(miFrame, text="Cantidad")
etiquetacant.grid(row=5, column=1, padx=30, pady=20)

cajacant = Entry(miFrame, justify="right")
cajacant.grid(row=5, column=2, padx=30, pady=20)


etiquetaprecio = Label(miFrame, text="Precio")
etiquetaprecio.grid(row=6, column=1, padx=30, pady=20)

cajaprecio = Entry(miFrame, justify="right")
cajaprecio.grid(row=6, column=2, padx=30, pady=20)

etiquetatotal = Label(miFrame, text="Total")
etiquetatotal.grid(row=20, column=1, padx=45, pady=20, columnspan=2)

caja3 = Entry(miFrame, textvariable=TP, justify="right")
caja3.grid(row=22, column=1, padx=30, pady=15, columnspan=2)


# -----------------------------Boton------------------------------------

boton1 = Button(miFrame, text="Calcular", width=13, command=total_pagar)
boton1.grid(row=9, column=2, padx=30, pady=20)


# ---------------------------------------------------------------------

miImagen = PhotoImage(file="pp.png")
firma = Label(miFrame, image=miImagen)
firma.grid(row=24, column=1, padx=10, pady=30, columnspan=2)

# ---------------------------------------------------------------------

root.mainloop()





