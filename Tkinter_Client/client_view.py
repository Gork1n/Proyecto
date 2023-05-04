from tkinter import StringVar
from tkinter import IntVar
from tkinter import Frame
from tkinter import Entry
from tkinter import Label
from tkinter import Button
from client_model import Abmc
from tkinter import ttk
import tkinter as tk

class Ventana:
    def __init__(self, window):
        self.root = window
        self.nmb = StringVar()
        self.stk = StringVar()
        self.prc = StringVar()
        self.prc_v = StringVar()
        self.a = IntVar()
        self.opcion = StringVar()
        self.f = Frame(self.root)
        self.tree = ttk.Treeview(self.f)
        self.objeto_base=Abmc()

        self.root.title("OrgStock")
        self.f.config(width=820, height=420)
        self.f.grid(row=20, column=0, columnspan=10)

        #Texto
        self.nombre = Label(self.root, text="Nombre")
        self.unidades = Label(self.root, text="Unidades")
        self.precio = Label(self.root, text="Precio de Compra")
        self.precio_venta = Label(self.root, text="Precio de Venta")
        self.nombre.grid(row=1, column=0, sticky="w")
        self.unidades.grid(row=2, column=0, sticky="w")
        self.precio.grid(row=3, column=0, sticky="w")
        self.precio_venta.grid(row=4, column=0, sticky="w")
        
        #Entradas
        self.Ent1 = Entry(self.root, textvariable=self.nmb,)
        self.Ent1.grid(row=1, column=1, sticky="w")
        self.Ent2 = Entry(self.root, textvariable=self.stk)
        self.Ent2.grid(row=2, column=1, sticky="w")
        self.Ent3 = Entry(self.root, textvariable=self.prc)
        self.Ent3.grid(row=3, column=1, sticky="w")
        self.Ent4 = Entry(self.root, textvariable=self.prc_v)
        self.Ent4.grid(row=4, column=1, sticky="w")

        #Botones
        self.boton_alta = Button(self.root, text="Alta", command=lambda: self.alta())
        self.boton_alta.grid(row=4, column=3)
        self.boton_editar = Button(self.root, text="Actualizar", command=lambda: self._modificar())
        self.boton_editar.grid(row=5, column=3)
        self.boton_borrar = Button(self.root, text="Borrar", command=lambda: self.borrar())
        self.boton_borrar.grid(row=6, column=3)


        #Tabla
        self.tree["columns"] = ("col1", "col2", "col3", "col4")
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Producto")
        self.tree.heading("col2", text="Unidades")
        self.tree.heading("col3", text="Compra")
        self.tree.heading("col4", text="Precio Venta")
        self.tree.column("#0", width=80, minwidth=80)
        self.tree.column("col1", width=80, minwidth=80)
        self.tree.column("col2", width=80, minwidth=80)
        self.tree.column("col3", width=80, minwidth=80)
        self.tree.column("col4", width=80, minwidth=80)
        self.tree.grid(column=0, row=7, columnspan=5)
    
    def aviso(self, parent):
        self.top = tk.Toplevel(parent)
        self.parent = parent
        self.top.title("Salir")

        tk.Label(self.top, text="¿Está seguro?").grid(row=0, column=0, columnspan=2)

        self.button1 = tk.Button(self.top, text="Si", command=self.salir)
        self.button2 = tk.Button(self.top, text="No", command=self.minimizar)
        self.button1.grid(row=1, column=0, padx=5, pady=5)
        self.button2.grid(row=1, column=1, padx=5, pady=5)

    def salir(self):
        self.objeto_base.salirr(self)

    def minimizar(self):
        Abmc.minimizar(self)

    def serveer(self,):
        Abmc.server()

    def alta(self):
        Abmc.alta(self)

    def actualizar(self,):
        self.objeto_base.actualizar_info(self.tree, 0)
     
    def borrar(self):
        self.objeto_base.baja(self.tree)

    def _modificar(self):
        Abmc.modificar(self)


    



