"""3.	Crear una lista con 10 números. Los números deben ser solicitados al usuario. Con los
datos que se tiene en la lista realiza r las siguientes operaciones:
•	Indicar cuántos números son positivos.
•	Indicar cuántos números son negativos.
•	Indicar cuántos números son ceros.
"""

from tkinter import *

root = Tk()

root.title = "Numeros @bichicode"

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))

root.resizable(True, True)

root.iconbitmap("bichi.ico")

MiFrame = Frame()

MiFrame.pack()

# ---------------------------------Variables---------------------------------------------

Totales = StringVar()
limite10 = 0
lista = []

# ---------------------------------Funciones-----------------------------------------------


def obtener_valores():
    num = caja1.get()
    enlistar(num)
    caja1.delete("0", "end")


def enlistar(n):
    global lista
    global limite10

    lista.append(n)

    limite10 += 1

    if limite10 >= 10:
        caja1.configure(state="disabled")
        print(lista)
        clasificar(lista, 0, 0)
    return


def clasificar(listas, t_negativo, t_positivo):

    t_cero = listas.count("0")

    for num in listas:
        if int(num) < 0:
            t_negativo += 1
        elif int(num) > 0:
            t_positivo += 1

    desplegar(t_negativo, t_cero, t_positivo, listas)

    return


def desplegar(negativos, ceros, positivos, listas):

    Totales.set("Negativos: " + str(negativos) + " Ceros: " + str(ceros) + " Positivos: " + str(positivos) +
                " Detalle: " + str(listas))

    return

# ------------------------------------------------------------------------------------------------------


titulo = Label(MiFrame, text="Numeros")
titulo.grid(row=2, column=1, padx=55, pady=20, columnspan=3)

numero = Label(MiFrame, text="Ingrese el numero")
numero.grid(row=7, column=1, padx=30, pady=10)

caja1 = Entry(MiFrame, justify="right")
caja1.grid(row=7, column=2, padx=30, pady=10)

etiquetaresultado = Label(MiFrame, text="Resultado")
etiquetaresultado.grid(row=13, column=1, padx=45, pady=10, columnspan=3)

caja2 = Entry(MiFrame, textvariable=Totales, justify="left", font="bold")
caja2.grid(row=14, column=1, columnspan=3, padx=10, pady=10,  ipadx=200, ipady=35)


# -------------------------Botones-------------------------------------


boton1 = Button(MiFrame, text="Aceptar", width=13, command=obtener_valores)
boton1.grid(row=10, column=2, padx=30, pady=20)


# ------------------------------Pie---------------------------------

miImagen = PhotoImage(file="pp.png")
firma = Label(MiFrame, image=miImagen)
firma.grid(row=70, column=1, padx=45, pady=2, columnspan=3)


# -----------------------------Fin de Bucle----------------------------------------

root.mainloop()








