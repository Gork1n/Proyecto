from flet import *
from c_model import Abmc
import threading
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "127.0.0.1" # Servidor
PORT = 55555      # puerto de envio
HEADER = 10

class Ventana:
    def __init__(self,page:Page):
        self.page = page
        self.page.scroll = 'always'
        self.nm = TextField(label='Producto',width=400)
        self.uni = TextField(label='Unidades',width=400)
        self.prc = TextField(label='Precio',width=400)
        self.prc_v = TextField(label='Precio de Venta',width=400)
        self.youid = TextField(label='')
        self.table_list = [self.nm, self.uni, self.prc, self.prc_v]

        self.mytable = DataTable(
            columns=[
                DataColumn(Text('id')),
                DataColumn(Text('Producto')),
                DataColumn(Text('Unidades')),
                DataColumn(Text('Precio')),
                DataColumn(Text('Precio de Venta'))],
            rows=[])
        self.addButton = ElevatedButton('add new', bgcolor='blue',color='white', on_click=self.addnewdata)
        self.delButton = ElevatedButton('delete this', bgcolor='red',color='white',on_click=self.removeindex)
        self.edButton = ElevatedButton('update data', bgcolor='orange',color='white',on_click=self.editandsave)
        self.rButton = ElevatedButton(' ← ',on_click=self.back)
        self.delButton.visible = False
        self.rButton.visible = False
        self.edButton.visible = False

        thread1 = threading.Thread(target=self.aviso_ac, args=())
        thread1.start()
        self.page.add(
            Column([
                Text('Orgstock',size=30, weight='bold'),
                self.nm, self.uni, self.prc, self.prc_v,
                Row([self.addButton,self.edButton,self.delButton,self.rButton]),
                self.mytable,
            ]))
    
    def back(self,e):
        self.rButton.visible = False
        self.delButton.visible = False
        self.edButton.visible = False
        self.addButton.visible = True
        self.page.update()

    def addnewdata(self,e):
        Abmc.addnewdata(self,e)
        
    def editandsave(self,e):
        Abmc.editandsave(self,e)
        self.back(e)
    
    def removeindex(self,e):
        Abmc.removeindex(self,e)
        self.back(e)
    
    def server():
        Abmc.server()
    
    def mensaje():
        Abmc.message(["", "_quit"])
    
    def aviso_ac(self):
        server.connect((HOST, 55555))
        Abmc.message(1)
        while True:
            data = server.recv(1000).decode('utf-8')
            if data == "_ac":
                Abmc.actualizar_info(self, 0)
                self.page.update()