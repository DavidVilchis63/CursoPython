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

#Mantener ventana activa
aplicacion.mainloop()