import c_view
import flet
from flet import *

class Controller:
    def __init__(self):
        self.objeto = c_view.Ventana
        flet.app(target=c_view.Ventana)
            
if __name__ == "__main__":
    c_view.Ventana.server()
    Controller()
    c_view.Ventana.mensaje()