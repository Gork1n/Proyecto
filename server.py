import socket
import threading
import pickle
from peewee import SqliteDatabase
from peewee import Model
from peewee import CharField
HOST = "127.0.0.1" # Servidor
PORT = 55555    # puerto de envio
HEADER = 10
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class Entrada:
    def __init__(self):
        print(f"Server running on {HOST}:{PORT}")
        server.bind((HOST, PORT))
        server.listen()
        self.clients = []
        self.conn_ac = []
        self.tuplas = {}
        while True:
            conn, address = server.accept()
            avss, addr = server.accept()
            print(f"Connect: {address}")
            self.clients.append(conn)
            self.conn_ac.append(avss)
            self.tuplas[conn] = avss
            self.objeto = Abmc()
            thread = threading.Thread(target=self.escucha, args=(conn,avss))
            thread.start()

    def escucha(self,conn,avss):
        while True:
            try:
                # 3
                # Espera recibir algun mensaje
                data_len = conn.recv(HEADER)
                if not data_len:
                    conn.close()
                    break
                else:
                    # Deserializa el mensaje y separa el primer mensaje de la lista
                    # Activa el case que sea igual al mensaje
                    datap = b''
                    datap += conn.recv(int(data_len))
                    self.data = pickle.loads(datap)
                    print(self.data)
                    try:
                        list = self.data[1]
                    except:
                        list = self.data
                    match list:
                        case "_quit":
                            self.aviso_qt(conn)
                        case 0:
                            self.objeto.actualizar_tk(conn)
                        case 1:
                            self.aviso_ac(1,conn)
                        case "_baja":
                            print("baja de :", avss)
                            self.objeto.baja(self.data[0])
                            self.aviso_ac(0,conn)
                        case "_modi":
                            print("modi de :", avss)
                            self.objeto.modificar(self.data)
                            self.aviso_ac(0,conn)
                        case _:
                            print("alta de :", avss)
                            self.objeto.alta(self)
                            self.aviso_ac(0,conn)
            except:break
    # Avisa a todos los clientes conectados de actualizar
    
    def aviso_ac(self,m,conn):
        if m == 0:
            for con in self.conn_ac:
                try:
                    con.send("_ac".encode('utf-8'))
                    print("Se ha enviado")
                except:
                    self.conn_ac.remove(con)
        else:
            self.tuplas[conn].send("_ac".encode('utf-8'))
    
    # Si un cliente cierra la conexion lo elimina de la lista
    def aviso_qt(self,conn):
        con = self.tuplas[conn]
        con.send("_quit".encode('utf-8'))
        self.tuplas.pop(conn)
        self.conn_ac.remove(con)
        self.clients.remove(conn)
        self.tupla_nmb.pop(conn)

        print(self.tupla_nmb)
        con.close()
    
class Abmc:
    def __init__(self):
        db = SqliteDatabase("tabla_stock.db")
        class BaseModel(Model):
            class Meta:
                database = db
        class Stock(BaseModel):
            nombre = CharField(unique=True)
            unidades = CharField()
            precio = CharField()
            precio_venta = CharField()
        db.connect()
        db.create_tables([Stock])
        self.stock = Stock

    def alta(self, self2):
        try:
            s = self.stock()
            s.nombre = self2.data[0]
            s.unidades = self2.data[1]
            s.precio = self2.data[2]
            s.precio_venta = self2.data[3]
            s.save()
        except:
            print("Tiene el mismo nombre el producto")
    
    def baja(self, id):
            borrar = self.stock.get(self.stock.id == id)
            borrar.delete_instance()
    
    def actualizar_tk(self,conn):
        for fila in self.stock.select():
            prueba1=fila.id
            prueba2=fila.nombre
            prueba3=fila.unidades
            prueba4=fila.precio
            prueba5=fila.precio_venta
            prueba = [prueba1, prueba2, prueba3, prueba4, prueba5]
            data_serial = pickle.dumps(prueba)
            data_len = str(len(data_serial))
            message = bytes(f"{data_len:<{HEADER}}",'utf-8')+ data_serial
            conn.send(message)
        prueba=0
        data_serial = pickle.dumps(prueba)
        data_len = str(len(data_serial))
        message = bytes(f"{data_len:<{HEADER}}",'utf-8')+ data_serial
        conn.send(message)
    
    def modificar(self,data):
        _valor_id=data[0]
        _nombre=data[2]
        _unidades=data[3]
        _precio=data[4]
        _precio_venta=data[5]
        actualizar=self.stock.update(nombre=_nombre, unidades=_unidades, precio=_precio, precio_venta=_precio_venta).where(self.stock.id==_valor_id)
        actualizar.execute()

Entrada()