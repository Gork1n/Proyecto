import socket
import pickle

HOST = "127.0.0.1" # Servidor
PORT = 55555
HEADER = 10
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class Abmc:
    def server(self,):
        server.connect((HOST, PORT))

    def alta(self, _nombre, _stock, _precio, _precio_venta, mitreeview):
        nombre = _nombre.get()
        stock = _stock.get()
        precio = _precio.get()
        precio_venta = _precio_venta.get()

        info= [nombre, stock, precio, precio_venta]
        data_serial = pickle.dumps(info)
        data_len = str(len(data_serial))
        message = bytes(f"{data_len:<{HEADER}}",'utf-8')+ data_serial
        server.send(message)
    
    def baja(self, mitreeview):
        try:
            item_sleccionado = mitreeview.focus()
            valor_id = mitreeview.item(item_sleccionado)
            valor = valor_id["text"]
            list = [valor, "_baja"]
            data_serial = pickle.dumps(list)
            data_len = str(len(data_serial))
            message = bytes(f"{data_len:<{HEADER}}",'utf-8')+ data_serial
            server.send(message)
        except:
            print("No marco el objeto deseado")
    
    def modificar(self, nombre, stock, precio, precio_venta, mitreeview):
        item_sleccionado = mitreeview.focus()
        valor_id = mitreeview.item(item_sleccionado)
        valor = valor_id["text"]
        list = [valor, "_modi", nombre.get(), stock.get(), precio.get(), precio_venta.get()]
        data_serial = pickle.dumps(list)
        data_len = str(len(data_serial))
        message = bytes(f"{data_len:<{HEADER}}",'utf-8')+ data_serial
        server.send(message)
        
    def actualizar_info(self, mitreeview, m):
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
        prueba=["", msg]
        data_serial = pickle.dumps(prueba)
        data_len = str(len(data_serial))
        message = bytes(f"{data_len:<{HEADER}}",'utf-8')+ data_serial
        server.send(message)
    
    def salirr(self, topp):
        self.message("_quit")
        topp.top.destroy()
        topp.parent.destroy()
    
    def minimizar(self, topp):
        topp.top.destroy()
        topp.parent.iconify()
        

                
            

