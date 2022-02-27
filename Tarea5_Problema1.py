"""Se desea un programa que lea dos números enteros. El programa debe realizar las
siguientes validaciones:
a. Si el primer número es mayor que el segundo, debe devolver 1.
b. Si el primer número es menor que el segundo, debe devolver -1.
c. Si ambos números son iguales, debe devolver un 0."""

from tkinter import *

root = Tk()
    
root.title("Notas @bichicode")

root.resizable(True, True)

root.iconbitmap("bichi.ico")

MiFrame = Frame()

MiFrame.pack()

# ----------------------------Variables-------------------------

Valor = StringVar()

# ----------------------------Funciones-------------------------


def obtener_valores():
    
    numero1 = float(caja1.get())
    numero2 = float(caja2.get())
    
    validar(numero1, numero2)

    return


def validar(n1, n2):
    
    if n1 > n2:
        val = 1
    elif n2 > n1:
        val = -1
    elif n1 == n2:
        val = 0
    else:
        val = "Error de datos"
    
    return Valor.set(str(val))


# -----------------------------------------------------------------


titulo = Label(MiFrame, text="Programa de Comparacion \n\n Favor ingresar dos numeros")
titulo.grid(row=2, column=1, padx=55, pady=20, columnspan=2)


num1 = Label(MiFrame, text="Primer Numero")
num1.grid(row=3, column=1, padx=30, pady=20)

caja1 = Entry(MiFrame, justify="right")
caja1.grid(row=3, column=2, padx=30, pady=20)


num2 = Label(MiFrame, text="Segundo Numero")
num2.grid(row=5, column=1, padx=30, pady=20)

caja2 = Entry(MiFrame, justify="right")
caja2.grid(row=5, column=2, padx=30, pady=20)


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