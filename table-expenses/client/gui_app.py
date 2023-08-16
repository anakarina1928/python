#interfaz de usurio de la aplicacion
import tkinter as tk
#from tkinter import _Cursor, _Relief, _ScreenUnits, _TakeFocusValue, Misc
#from typing import Any
#from typing_extensions import Literal 
#from tkinter import *


class Frame(tk.Frame):# utilizo la clase Frame de la libreria tk y creo una subclase
    def __init__(self, root = None):
        super().__init__(root,width= 480, height=320 )
        self.root=root
        self.pack()
        self.config(bg='blue') # configuramos el tamaño del contenedor que hemos creado en la variable frame