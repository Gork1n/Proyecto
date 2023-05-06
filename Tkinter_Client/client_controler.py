from tkinter import Tk
import client_view
import threading
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "127.0.0.1" # Servidor
PORT = 55555      # puerto de envio
HEADER = 10
n = 0

class Controller:
    def __init__(self, root):
        self.root_controler = root
        self.objeto_vista = client_view.Ventana(self.root_controler)
        self.root_controler.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def on_closing(self):
        client_view.Ventana.aviso(self.objeto_vista, self.root_controler)

    def aviso_ac(root_tk):
        server.connect((HOST, 55555))
        while True:
            data = server.recv(1000).decode('utf-8')
            if data == "_ac":
                objeto_vista = client_view.Ventana(root_tk)
                objeto_vista.actualizar()
            if data == "_quit":
                break

class Con:
    root_tk = Tk()
    application = Controller(root_tk)
    thread23 = threading.Thread(target=Controller.aviso_ac, args=(root_tk,))
    application.objeto_vista.serveer()
    thread23.start()
    application.objeto_vista.mensaje_entrada()
    root_tk.mainloop()

if __name__ == "__main__":
    Con()