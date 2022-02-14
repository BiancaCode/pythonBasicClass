"""Se desea un programa que lea dos notas parciales de un estudiante. El programa debe utilizar
una función en donde se calcule el promedio y asigne la literal. La función debe regresar el
promedio y la literal."""

from tkinter import *

root = Tk()

root.title("Notas @bichicode")

root.resizable(True, True)

root.iconbitmap("bichi.ico")

myFrame = Frame()

myFrame.pack()

# ----------------------------Variables-------------------------
Prom = StringVar()
# ----------------------------Funciones-------------------------
def obtener_valores():
    nota = float(caja1.get())
    nota2 = float(caja2.get())
    Prom.set(str(promedio(nota, nota2)))
    return

def promedio(n1, n2):
    p = (n1 + n2)/2

    if (p >= 91) and (p <= 100):
        letra = "A"
    elif (p >= 81) and (p <= 90):
        letra = "B"
    elif (p >= 71) and (p <= 80):
        letra = "C"
    elif (p >= 61) and (p <= 70):
        letra = "D"
    elif (p >= 0) and (p <= 60):
        letra = "F"
    else:
        letra = "Error"

    return p, letra

# -------------------------------------------------------------------


etiqueta = Label(myFrame, text="Programa de Promedio \n\n Favor ingresar las calificaciones")
etiqueta.grid(row=2, column=1, padx=55, pady=20, columnspan=2)


etiqueta1 = Label(myFrame, text="Primera Calificacion")
etiqueta1.grid(row=3, column=1, padx=30, pady=20)

caja1 = Entry(myFrame, justify="right")
caja1.grid(row=3, column=2, padx=30, pady=20)


etiqueta2 = Label(myFrame, text="Segunda Calificacion")
etiqueta2.grid(row=5, column=1, padx=30, pady=20)

caja2 = Entry(myFrame, justify="right")
caja2.grid(row=5, column=2, padx=30, pady=20)


etiquetaresultado = Label(myFrame, text="Promedio")
etiquetaresultado.grid(row=15, column=1, padx=30, pady=20, columnspan=2)

cajaresultado = Entry(myFrame, justify="center", font="bold", textvariable=Prom)
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