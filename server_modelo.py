from peewee import SqliteDatabase
from peewee import Model
from peewee import CharField
import pickle

HOST = "127.0.0.1" # Servidor
PORT = 55555     # puerto de envio
HEADER = 10

# Crea el archivo Sqlite y crea la tabla
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


def alta(_nombre, _unidades, _precio, _precio_venta, conn):
    try:
        stock=Stock()
        stock.nombre=_nombre
        stock.unidades=_unidades
        stock.precio=_precio
        stock.precio_venta=_precio_venta
        stock.save()
    except:
        print("Tiene el mismo nombre el producto")
    
def baja(id):
    try:
        borrar=Stock.get(Stock.id==id)
        borrar.delete_instance()
    except:pass

def actualizar_tk(conn):
    for fila in Stock.select():
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


def modificar(data):
    valor_id=data[0]
    nombre=data[2]
    unidades=data[3]
    precio=data[4]
    precio_venta=data[5]
    actualizar=Stock.update(nombre=nombre, unidades=unidades, precio=precio, precio_venta=precio_venta).where(Stock.id==valor_id)
    actualizar.execute()
