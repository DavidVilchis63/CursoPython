"""
    Modulo TKinter
"""

from tkinter import *

#Iniciar aplicaion
aplicacion = Tk()

#Tamaño de la ventana
aplicacion.geometry("1020x630+0+0")

#Evitar maximar
aplicacion.resizable(False, False)

#Titulo de ventana
aplicacion.title("Restaurante - Sistema de facturacion")

#Color de la ventana
aplicacion.config(bg="burlywood")

#Panel superior
panelSuperior = Frame(aplicacion, bd=1, relief=FLAT)
panelSuperior.pack(side=TOP)

#Etiqueta titulo
etiquetaTitulo = Label(panelSuperior, text="Sistema de facturación", fg="azure4", font=("Dosis", 58,), bg="burlywood", width=24)
etiquetaTitulo.grid(row = 0, column = 0)

#Panel izquierdo
panelIzquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panelIzquierdo.pack(side=LEFT)

#Panel costos
panelCostos = Frame(panelIzquierdo, bd=1, relief=FLAT)
panelCostos.pack(side=BOTTOM)

#Panel comida
panelComida = LabelFrame(panelIzquierdo, text="Comida", font=("Dosis", 19, "bold"), bd=1, relief=FLAT, fg="azure4")
panelComida.pack(side=LEFT)

#Panel bebidas
panelBebidas = LabelFrame(panelIzquierdo, text="Bebidas", font=("Dosis", 19, "bold"), bd=1, relief=FLAT, fg="azure4")
panelBebidas.pack(side=LEFT)

#Panel postres
panelPostres = LabelFrame(panelIzquierdo, text="Postres", font=("Dosis", 19, "bold"), bd=1, relief=FLAT, fg="azure4")
panelPostres.pack(side=LEFT)

#Panel derecha
panelDerecha = Frame(aplicacion, bd=1, relief=FLAT)
panelDerecha.pack(side=RIGHT)

#Panel calculadora
panelCalculadora = Frame(panelDerecha, bd=1, relief=FLAT, bg="burlywood")
panelCalculadora.pack()

#Panel recibo
panelRecibo = Frame(panelDerecha, bd=1, relief=FLAT, bg="burlywood")
panelRecibo.pack()

#Panel botones
panelBotones = Frame(panelDerecha, bd=1, relief=FLAT, bg="burlywood")
panelBotones.pack()

#Mantener ventana activa
aplicacion.mainloop()