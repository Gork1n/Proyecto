import socket
import threading
import pickle
from server_modelo import alta
from server_modelo import actualizar_tk
from server_modelo import baja
from server_modelo import modificar

HOST = "127.0.0.1" # Servidor
PORT = 55555    # puerto de envio
HEADER = 10
clients = []
conn_ac = []
tuplas = {}

#1
#Se abre el puerto y se espera a una conexion
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"Server running on {HOST}:{PORT}")
server.bind((HOST, PORT))
server.listen()

def Entrada(conn, addrs):
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
                data = b''
                data += conn.recv(int(data_len))
                data_deserial = pickle.loads(data)
                data_deserial
                try:
                    list = data_deserial[1]
                except:
                    list = data_deserial
                match list:
                    case "_quit":
                        aviso_qt(conn)
                    case 0:
                        actualizar_tk(conn)
                    case "_baja":
                        print("baja de :", addrs)
                        baja(data_deserial[0])
                        aviso_ac()
                    case "_modi":
                        print("modi de :", addrs)
                        modificar(data_deserial)
                        aviso_ac()
                    case _:
                        print("alta de :", addrs)
                        altas(data_deserial, conn)
                        aviso_ac()
        except:break


# Avisa a todos los clientes conectados de actualizar
def aviso_ac():
    server.setblocking(False)
    for con in conn_ac:
        try:
            con.send("_ac".encode('utf-8'))
            print("Se ha enviado")
        except:
            conn_ac.remove(con)
    server.setblocking(True)

# Si un cliente cierra la conexion lo elimina de la lista
def aviso_qt(client):
    con = tuplas[client]
    con.send("_quit".encode('utf-8'))
    tuplas.pop(client)
    conn_ac.remove(con)
    clients.remove(client)
    con.close()


def altas(data, conn):
    nombre = data[0]
    stock = data[1]
    precio = data[2]
    precio_venta = data[3]
    alta(nombre, stock, precio, precio_venta, conn)

# 2
# Acepta las 2 conexiones del Cliente e inicia un Thread con la funcion Entrada
# Las dos conexiones del Cliente se relacionan con una tupla 
def receive_connections():
    while True:
        client, address = server.accept()
        avss, addr = server.accept()
        print(f"Connect: {addr}")
        clients.append(client)
        conn_ac.append(avss)
        tuplas[client] = avss

        thread = threading.Thread(target=Entrada, args=(client, address))
        thread.start()

receive_connections()