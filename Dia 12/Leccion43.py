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

#Lista de productos
listaComidas = ["pollo", "cordero", "salmon", "merluza", "kebab", "pizza", "sushi", "sopa"]
listaBebidas = ["agua", "soda", "cerveza", "vino", "tequila", "ron", "whisky", "jugo"]
listaPostres = ["helado", "tarta", "fruta", "brownie", "flan", "tiramisu", "cheesecake", "mousse"]

#Generar items comida
variableComida = []
cuadrosComida = []
textoComida = []
contador = 0
for comida in listaComidas:

    #Crear checkbutton
    variableComida.append("")
    variableComida[contador] = IntVar()
    comida = Checkbutton(panelComida,
                         text = comida.title(),
                         font=("Dosis", 16, "bold"),
                         onvalue=1,
                         offvalue=0,
                         variable=variableComida[contador])
    comida.grid(row=contador,
                column=0,
                sticky=W)
    
    #Crear cuadro de entrada
    cuadrosComida.append("")
    textoComida.append("")
    textoComida[contador] = StringVar()
    textoComida[contador].set("0")
    cuadrosComida[contador] = Entry(panelComida,
                                    font=("Dosis", 16, "bold"),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=textoComida[contador])
    cuadrosComida[contador].grid(row=contador,
                                 column=1)

    contador += 1

#Generar items bebidas
variableBebida = []
cuadrosBebida = []
textoBebida = []
contador = 0
for bebidas in listaBebidas:

    #Crear checkbutton
    variableBebida.append("")
    variableBebida[contador] = IntVar()
    bebidas = Checkbutton(panelBebidas,
                          text = bebidas.title(),
                          font=("Dosis", 16, "bold"),
                          onvalue=1,
                          offvalue=0,
                          variable=variableBebida[contador])
    bebidas.grid(row=contador,
                 column=0,
                 sticky=W)
    
    #Crear cuadro de entrada
    cuadrosBebida.append("")
    textoBebida.append("")
    textoBebida[contador] = StringVar()
    textoBebida[contador].set("0")
    cuadrosBebida[contador] = Entry(panelBebidas,
                                    font=("Dosis", 16, "bold"),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=textoBebida[contador])
    cuadrosBebida[contador].grid(row=contador,
                                 column=1)

    contador += 1

#Generar items postres
variablePostres = []
cuadrosPostres = []
textoPostres = []
contador = 0
for postres in listaBebidas:

    #Crear checkbutton
    variablePostres.append("")
    variablePostres[contador] = IntVar()
    postres = Checkbutton(panelPostres,
                          text = postres.title(),
                          font=("Dosis", 16, "bold"),
                          onvalue=1,
                          offvalue=0,
                          variable=variablePostres[contador])
    postres.grid(row=contador,
                 column=0,
                 sticky=W)
    
    #Crear cuadro de entrada
    cuadrosPostres.append("")
    textoPostres.append("")
    textoPostres[contador] = StringVar()
    textoPostres[contador].set("0")
    cuadrosPostres[contador] = Entry(panelPostres,
                                    font=("Dosis", 16, "bold"),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=textoPostres[contador])
    cuadrosPostres[contador].grid(row=contador,
                                 column=1)

    contador += 1


#Mantener ventana activa
aplicacion.mainloop()