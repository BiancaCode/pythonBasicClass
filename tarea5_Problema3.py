"""Un proveedor de televisores ofrece un descuento del 10% sobre el precio sin impuesto, de
algún aparato el costo es de $2000 o más. Además, independientemente de esto, ofrece un
5% de descuento adicional sobre el precio si la marca es Super"""

from tkinter import *

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

cabecera = PhotoImage(file="televisores.png")
cb = Label(MiFrame, image=cabecera)
cb.grid(row=2, column=1, padx=10, pady=30, columnspan=3)

# ----------------------------Variables-------------------------

Valor = StringVar()
Detalle_Fact = StringVar()
t_descuento = 0
subtotal = 0
info = ""
# ----------------------------Funciones--------------------------

def obtener_valores():

    marca = caja1.get()
    precio_ = caja2.get()
    cantidad = caja3.get()

    des_p = descuento_precio(float(precio_), int(cantidad))
    des_m = descuento_marca(marca, float(precio_), int(cantidad))
    acumular(float(precio_), int(cantidad), des_p, des_m)
    resumen_pedido(marca, precio_, cantidad)

    caja1.delete("0", "end")
    caja2.delete("0", "end")
    caja3.delete("0", "end")

    return


def descuento_precio(prec, ca):

    if prec >= 2000:
        calculo = (prec * ca) * 0.1
        descuento_p = round(calculo, 2)
    else:
        descuento_p = 0

    return descuento_p


def descuento_marca(marca, prec, ca):

    if marca == "Super":
        calculo = (prec * ca) * 0.05
        descuento_m = round(calculo, 2)
    else:
        descuento_m = 0

    return descuento_m


def acumular( precio_u, cantidad_u, desp, desv):

    global t_descuento
    global subtotal

    a = precio_u * cantidad_u
    redondeado = round(a, 2)

    subtotal = round((subtotal + redondeado),2)
    t_descuento = t_descuento + (desp + desv)

    return


def resumen_pedido(m, p, c):

    global info

    renglon = " >> Marca: " + m + " - Precio: " + p + " - Cantidad: " + c + "  "

    info = info + renglon       # Acumula el detalle del pedido

    return


def sieteporciento(): # Calculos y despliegue final se acciona cuando el usuario hace clic en el boton aceptar

    global subtotal
    global t_descuento
    global info

    impuesto = round((subtotal - t_descuento) * 0.07, 2)        #Calculo del 7%
    total = round(((subtotal - t_descuento) * 1.07), 2)     #Calculo del gran total de la compra
    imprimir = " - Sub total: " + str(subtotal) + "  Descuentos: " + str(t_descuento) + "  Imp 7%: " + str(impuesto) + "  >>Total: " + str(total) + "$"

    Detalle_Fact.set(info)
    return Valor.set(imprimir)


# --------------------------------------------------------------------


titulo = Label(MiFrame, text="Facturacion \n\n Favor introducir los datos solicitados")
titulo.grid(row=3, column=1, padx=55, pady=20, columnspan=3)

producto = Label(MiFrame, text="Producto")
producto.grid(row=6, column=1, padx=30, pady=20)

caja1 = Entry(MiFrame, justify="right")
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