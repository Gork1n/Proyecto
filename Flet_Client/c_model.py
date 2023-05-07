from flet import *
import socket
import pickle

HOST = "127.0.0.1" # Servidor
PORT = 55555
HEADER = 10
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class Abmc:
    def server():
        server.connect((HOST,PORT))

    def addnewdata(self,e):
        list=[]
        for i in range(0,4):
            list.append(self.table_list[i].value)
        data_serial = pickle.dumps(list)
        data_len = str(len(data_serial))
        message = bytes(f"{data_len:<{HEADER}}",'utf-8')+ data_serial
        server.send(message)
        for i in self.table_list:
            i.value = ''
        self.addButton.visible = True
        self.delButton.visible = False
        self.edButton.visible = False
    
    def editindex(e,n,u,p,pv,self):
        self.id = int(e)
        print(self.id)
        self.table_list[0].value = n
        self.table_list[1].value = u
        self.table_list[2].value = p
        self.table_list[3].value = pv
        self.youid.value = int(e)
        self.addButton.visible = False
        self.delButton.visible = True
        self.edButton.visible = True
        self.page.update()

    def removeindex(self,e):
        try:
            valor = self.id
            list = [valor, "_baja"]
            data_serial = pickle.dumps(list)
            data_len = str(len(data_serial))
            message = bytes(f"{data_len:<{HEADER}}",'utf-8')+ data_serial
            server.send(message)
            self.page.snack_bar = SnackBar(Text(f'succes delete you id = {self.id}', color='white'),bgcolor='red',)
            self.page.snack_bar.open = True
            for i in self.table_list:
                i.value = ''
        except:pass
    
    def editandsave(self,e):
        list=[self.id, "_modi"]
        for i in range(0,4):
            list.append(self.table_list[i].value)
        data_serial = pickle.dumps(list)
        data_len = str(len(data_serial))
        message = bytes(f"{data_len:<{HEADER}}",'utf-8')+ data_serial
        server.send(message)
    
    def message(n):
        list = n
        data_serial = pickle.dumps(list)
        data_len = str(len(data_serial))
        message = bytes(f"{data_len:<{HEADER}}",'utf-8')+ data_serial
        server.send(message)
    
    def actualizar_info(self, m):
        if m == 0:
            prueba=0
            data_serial = pickle.dumps(prueba)
            data_len = str(len(data_serial))
            message = bytes(f"{data_len:<{HEADER}}",'utf-8')+ data_serial
            server.send(message)

        while True:
            try:del self.mytable.rows[0]
            except:break
        
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
                    self.mytable.rows.append(
                        DataRow(
                            cells=[
                            DataCell(Text(fin[0])),
                            DataCell(Text(fin[1])),
                            DataCell(Text(fin[2])),
                            DataCell(Text(fin[3])),
                            DataCell(Text(fin[4]))],
                        on_select_changed=lambda e:Abmc.editindex(
                            e.control.cells[0].content.value,
                            e.control.cells[1].content.value,
                            e.control.cells[2].content.value,
                            e.control.cells[3].content.value,
                            e.control.cells[4].content.value,
                            self)))
                    self.page.update()
                    
