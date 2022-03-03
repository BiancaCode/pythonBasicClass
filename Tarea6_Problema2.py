"""Tarea 6
Problema2
Bianca
2.	En una tienda que vende por departamentos se están otorgando descuentos a las compras de los clientes.

L   Línea Blanca            5%
A   Audio y Video           6%
U   útiles de oficina y escolares 4
H   Hogar 3
T   Auto 3
E   Electridad 5
M   Lámparas 8
J   Jardinería 4
P   Mascotas 6
Otro    Otro 2



El usuario debe suministrar al programa los datos de la compra.

El programa debe calcular el subtotal de la compra, el descuento, el impuesto y el total a pagar.

STotal = Cantidad * Precio

Descuento = STotal * % Descuento(según el departamento en donde se realizó la compra) Impuesto =(Stotal  Descuento) * 7%
Total= (Stotal - Descuento)+ Impuesto
"""


from tkinter import *
from tkinter.ttk import Combobox

root = Tk()

root.title("Facturacion @bichicode")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))

root.resizable(True, True)

root.iconbitmap("bichi.ico")

MiFrame = Frame()

MiFrame.pack()

# ---------------------------Cabecera---------------------------

cabecera = PhotoImage(file="logotienda.png")
cb = Label(MiFrame, image=cabecera)
cb.grid(row=1, column=1, padx=10, pady=30, columnspan=3)

# ----------------------------Variables-------------------------

Valor = StringVar()
Detalle_Fact = StringVar()
opciones = ["Línea Blanca", "Audio y Video", "Utiles de oficina y escolar", "Hogar", "Auto", "Electridad", "Lámparas",
            "Jardinería", "Mascotas", "Otro"]
codigos = ["L", "A", "U", "H", "T", "E", "M", "J", "P", "Otro"]
descuentos = [0.05, 0.06, 0.04, 0.03, 0.03, 0.05, 0.08, 0.04, 0.06, 0.02]
t_descuento = 0
subtotal = 0
info = ""
# ----------------------------Funciones--------------------------


def obtener_valores():

    marca = caja1.get()
    precio_ = caja2.get()
    cantidad = caja3.get()

    des_m, cod = descuento_marca(marca, float(precio_), int(cantidad))
    acumular(float(precio_), int(cantidad), des_m)
    resumen_pedido(cod, precio_, cantidad, des_m)

    caja1.delete("0", "end")
    caja2.delete("0", "end")
    caja3.delete("0", "end")

    return


def descuento_marca(marca, prec, ca):

    indice = opciones.index(marca)
    codigo = codigos[indice]
    descuento = descuentos[indice]

    calculo = (prec * ca) * descuento
    descuento_m = round(calculo, 2)

    return descuento_m, codigo


def acumular(precio_u, cantidad_u, descuento_u):

    global t_descuento
    global subtotal

    a = precio_u * cantidad_u
    redondeado = round(a, 2)

    subtotal = round((subtotal + redondeado), 2)
    t_descuento += descuento_u

    return


def resumen_pedido(m, p, c, d):

    global info
    descuento = str(d)

    renglon = " >> Dep: " + m + " - Precio: " + p + " - Cantidad: " + c + " Descuento: " + descuento + "  "

    info = info + renglon       # Acumula el detalle del pedido

    return


def sieteporciento():  # -- Calculos y despliegue final se acciona cuando el usuario hace clic en el boton aceptar

    global subtotal
    global t_descuento
    global info

    impuesto = round((subtotal - t_descuento) * 0.07, 2)        # --Calculo del 7%
    total = round(((subtotal - t_descuento) * 1.07), 2)     # --Calculo del gran total de la compra
    imprimir = " - Sub total: " + str(subtotal) + "  Descuentos: " + str(t_descuento) + "  Imp 7%: " + str(impuesto) + "  >>Total: " + str(total) + "$"

    Detalle_Fact.set(info)
    return Valor.set(imprimir)


# --------------------------------------------------------------------


titulo = Label(MiFrame, text="Facturacion")
titulo.grid(row=2, column=1, padx=55, pady=20, columnspan=3)

producto = Label(MiFrame, text="Producto")
producto.grid(row=6, column=1, padx=30, pady=20)

caja1 = Combobox(MiFrame, values=opciones, state="readonly")
caja1.grid(row=7, column=1, padx=30, pady=10)

precio = Label(MiFrame, text="Precio")
precio.grid(row=6, column=2, padx=30, pady=10)

caja2 = Entry(MiFrame, justify="right")
caja2.grid(row=7, column=2, padx=30, pady=10)

cantidadl = Label(MiFrame, text="Cantidad")
cantidadl.grid(row=6, column=3, padx=30, pady=10)

caja3 = Entry(MiFrame, justify="right")
caja3.grid(row=7, column=3, padx=30, pady=10)


etiquetafactura = Label(MiFrame, text="Factura")
etiquetafactura.grid(row=13, column=1, padx=45, pady=10, columnspan=3)


caja4 = Entry(MiFrame, textvariable=Detalle_Fact, justify="left", font="bold")
caja4.grid(row=14, column=1, columnspan=3, padx=10, pady=10,  ipadx=200, ipady=35)

caja5 = Entry(MiFrame, textvariable=Valor, justify="left", font="bold")
caja5.grid(row=20, column=1, columnspan=3, padx=10, pady=10,  ipadx=200, ipady=35)


# -------------------------Botones-------------------------------------


boton1 = Button(MiFrame, text="Aceptar", width=13, command=obtener_valores)
boton1.grid(row=10, column=2, padx=30, pady=20)

boton2 = Button(MiFrame, text="Facturar", width=13, command=sieteporciento)
boton2.grid(row=10, column=3, padx=30, pady=20)

# ------------------------------Pie---------------------------------

miImagen = PhotoImage(file="pp.png")
firma = Label(MiFrame, image=miImagen)
firma.grid(row=70, column=1, padx=45, pady=2, columnspan=3)


# -----------------------------Fin de Bucle----------------------------------------

root.mainloop()