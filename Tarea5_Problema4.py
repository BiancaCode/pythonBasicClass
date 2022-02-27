"""Defina una función que acepte tres valores enteros y devuelva el máximo de los tres números."""
from tkinter import *

root = Tk()

root.title("Comparar @bichicode")

root.resizable(True, True)

root.iconbitmap("bichi.ico")

myFrame = Frame()

myFrame.pack()

# ----------------------------Variables-------------------------
Mayor = StringVar()
# ----------------------------Funciones-------------------------
def obtener_valores():
    n1 = float(caja1.get())
    n2 = float(caja2.get())
    n3 = float(caja3.get())
    maximo = mayor(n1, n2, n3)
    return Mayor.set(maximo)

def mayor(n1, n2, n3):

    if (n1 >= n2) and (n2 >= n3) or (n1 >= n3) and (n3 >= n2):
        max = n1
    elif (n2 >= n1) and (n1 >= n3) or (n2 >= n3) and (n3 >= n1):
        max = n2
    else:
        max = n3

    return max

# -------------------------------------------------------------------


etiqueta = Label(myFrame, text="Programa de Mayor \n\n Favor Ingresar Los Numeros")
etiqueta.grid(row=2, column=1, padx=55, pady=20, columnspan=2)


etiqueta1 = Label(myFrame, text="Primer Numero")
etiqueta1.grid(row=3, column=1, padx=30, pady=20)

caja1 = Entry(myFrame, justify="right")
caja1.grid(row=3, column=2, padx=30, pady=20)


etiqueta2 = Label(myFrame, text="Segundo Numero")
etiqueta2.grid(row=5, column=1, padx=30, pady=20)

caja2 = Entry(myFrame, justify="right")
caja2.grid(row=5, column=2, padx=30, pady=20)

etiqueta3 = Label(myFrame, text="Tercer Numero")
etiqueta3.grid(row=7, column=1, padx=30, pady=20)

caja3 = Entry(myFrame, justify="right")
caja3.grid(row=7, column=2, padx=30, pady=20)


etiquetaresultado = Label(myFrame, text="Numero Mayor")
etiquetaresultado.grid(row=15, column=1, padx=30, pady=20, columnspan=2)

cajaresultado = Entry(myFrame, justify="center", font="bold", textvariable=Mayor)
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