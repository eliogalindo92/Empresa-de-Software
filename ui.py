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

    ## esto es para controlar los radiobutton
    def sel(self):
        selection = "A seleccionado la opcion " + str(self.var.get())
        self.label = Label()
        self.label.config(text = selection)        
        self.label.pack()

    ## boton de prueba guardar entrada
    def guardarE(self):
        self.result=(self.campoTextoID.get(), self.campoTextoLineas.get(), self.campoTextoHoras.get())
        print(self.result)

    ## boton de prueba editar entrada
    def editarE(self):
        self.result=(self.campoTextoID.get(), self.campoTextoLineas.get(), self.campoTextoHoras.get())
        print(self.result)

    ## boton de prueba eliminar entrada
    def eliminarE(self):
        self.result=(self.campoTextoID.get(), self.campoTextoLineas.get(), self.campoTextoHoras.get())
        print(self.result)
        
    def _unidadGrafica(self):
        ## iniciando menu
        self.menuBarr()

        ## label de inicio
        self.lab1 = Label(self.root, text="Esto es un Label")
        self.lab1.pack()

        ## Reloj
        self.reloj_label()

        ## Radiobuttom
        self.var = IntVar()
        R1 = Radiobutton(self.root, text="Opcion 1", variable=self.var, value=1, command=self.sel)
        R1.pack( anchor = W )

        R2 = Radiobutton(self.root, text="Opcion 2", variable=self.var, value=2, command=self.sel)
        R2.pack( anchor = W )

        R3 = Radiobutton(self.root, text="Opcion 3", variable=self.var, value=3, command=self.sel)
        R3.pack( anchor = W)

        ## entrada de texto
        self.lab1 = Label(self.root, text="ID")
        self.lab1.pack()

        self.campoTextoID=tk.Entry(self.root)
        self.campoTextoID.pack()

        self.lab1 = Label(self.root, text="lineas de codigo")
        self.lab1.pack()

        self.campoTextoLineas=tk.Entry(self.root)
        self.campoTextoLineas.pack()

        self.lab1 = Label(self.root, text="Horas trabajadas")
        self.lab1.pack()

        self.campoTextoHoras=tk.Entry(self.root)
        self.campoTextoHoras.pack()

        btnRead=tk.Button(self.root, height=1, width=10, text="guardar", command= self.guardarE)
        btnRead.pack()

        btnRead=tk.Button(self.root, height=1, width=10, text="editar", command= self.editarE)
        btnRead.pack()

        btnRead=tk.Button(self.root, height=1, width=10, text="eliminar", command= self.eliminarE)
        btnRead.pack()

main_UI = GUI()