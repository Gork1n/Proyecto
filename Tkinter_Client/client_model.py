import socket
import pickle

HOST = "127.0.0.1" # Servidor
PORT = 55555
HEADER = 10
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class Abmc:
    def server():
        server.connect((HOST, PORT))
    def alta(self):
        nombre = self.nmb.get()
        stock = self.stk.get()
        precio = self.prc.get()
        precio_venta = self.prc_v.get()

        info= [nombre, stock, precio, precio_venta]
        data_serial = pickle.dumps(info)
        data_len = str(len(data_serial))
        message = bytes(f"{data_len:<{HEADER}}",'utf-8')+ data_serial
        server.send(message)
        Abmc.actualizar_info(self, self.tree, 0)
    
    def baja(self, mitreeview):
        try:
            item_sleccionado = mitreeview.focus()
            if not item_sleccionado:
                print("No marco el objeto deseado")
            else:
                valor_id = mitreeview.item(item_sleccionado)
                valor = valor_id["text"]
                list = [valor, "_baja"]
                data_serial = pickle.dumps(list)
                data_len = str(len(data_serial))
                message = bytes(f"{data_len:<{HEADER}}",'utf-8')+ data_serial
                server.send(message)
        except:
            print("Error al eliminar")
    
    def modificar(self):
        item_sleccionado = self.tree.focus()
        valor_id = self.tree.item(item_sleccionado)
        valor = valor_id["text"]
        list = [valor, "_modi", self.nmb.get(), self.stk.get(), self.prc.get(), self.prc_v.get()]
        data_serial = pickle.dumps(list)
        data_len = str(len(data_serial))
        message = bytes(f"{data_len:<{HEADER}}",'utf-8')+ data_serial
        server.send(message)
        
    def actualizar_info(self,mitreeview, m):
        if m == 0:
            prueba=0
            data_serial = pickle.dumps(prueba)
            data_len = str(len(data_serial))
            message = bytes(f"{data_len:<{HEADER}}",'utf-8')+ data_serial
            server.send(message)

        records = mitreeview.get_children()
        for element in records:
            mitreeview.delete(element)
        

        while True:
            data_len = server.recv(HEADER)
            if not data_len:
                break
            else:
                data = b''
                data += server.recv(int(data_len))
                data_deserial = pickle.loads(data)
                fin = data_deserial
                if data_deserial == 0:
                    break
                else:
                    mitreeview.insert("", 0, text=fin[0], values=(fin[1], fin[2], fin[3], fin[4]))

    def message(self, msg):
        if msg == "_quit":prueba=["", msg]
        else: prueba = msg
        data_serial = pickle.dumps(prueba)
        data_len = str(len(data_serial))
        message = bytes(f"{data_len:<{HEADER}}",'utf-8')+ data_serial
        server.send(message)
    
    def salirr(self_Abmc, self_Vista):
        self_Abmc.message("_quit")
        self_Vista.top.destroy()
        self_Vista.parent.destroy()
    
    def minimizar(self):
        self.top.destroy()
        self.parent.iconify()
        

                
            

