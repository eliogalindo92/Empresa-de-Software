import tkinter as tk
from tkinter import ttk
from tkinter import *
import time

class GUI():
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title('Ventana Titulo')
        self.root.geometry("400x350")
        self.root.iconbitmap('') #poner direccion del icono a utilizar
        self._unidadGrafica()
        self.run()

    def run(self):
        self.root.mainloop()

    def menuBarr(self):
        self.barraMenu = Menu(self.root)
        self.root.config(menu=self.barraMenu, widt=300, height=300)   

        self.archivoMenu=Menu(self.barraMenu, tearoff=0)
        self.archivoMenu.add_command(label="nuevo")
        self.archivoMenu.add_command(label="guardar")
        self.archivoMenu.add_command(label="guardar como")
        self.archivoMenu.add_separator()
        self.archivoMenu.add_command(label="cerrar")
        self.archivoMenu.add_command(label="salir")

        archivoEdicion=Menu(self.barraMenu, tearoff=0)
        archivoEdicion.add_command(label="Abrir")
        archivoEdicion.add_command(label="nuevo2")
        archivoEdicion.add_command(label="nuevo3")

        archivoHerramientas=Menu(self.barraMenu, tearoff=0)
        archivoHerramientas.add_command(label="nuevo")
        archivoHerramientas.add_command(label="nuevo")
        archivoHerramientas.add_command(label="nuevo")

        archivoAyuda=Menu(self.barraMenu, tearoff=0)
        archivoAyuda.add_command(label="Licencia")
        archivoAyuda.add_command(label="Ayuda")

        self.barraMenu.add_cascade(label="Archivo", menu = self.archivoMenu)
        self.barraMenu.add_cascade(label="Editar", menu = archivoEdicion)
        self.barraMenu.add_cascade(label="Herramientas", menu = archivoHerramientas)
        self.barraMenu.add_cascade(label="Ayuda", menu = archivoAyuda)

    def reloj_label(self):
        ## creando un label reloj
        self.time1=''
        self.reloj=Label(self.root)
        self.reloj.pack()    
        def relojj():
            global time1
            self.time2 = time.strftime("%H:%M:%S")
            if self.time2 != self.time1:
                self.time1=self.time2
                self.reloj.configure(text=self.time2)
            self.reloj.after(500,relojj)
        relojj()

    def _unidadGrafica(self):
        ## iniciando menu
        self.menuBarr()

        ## label de inicio
        self.lab1 = Label(self.root, text="Esto es un Label")
        self.lab1.pack()

        self.reloj_label()

main_UI = GUI()