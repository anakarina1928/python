# activavion de nuestro entorno virtual: env\Scripts\activate.bat // para desactivar: env\Scripts\desactivate.bat
# Un entorno virtual es un espacio aislado donde se gestionan las bibliotecas y dependencias de un proyecto.
import tkinter as tk
"""biblioteca de interfaz gráfica de usuario (GUI) queforma parte de la librería estándar de Python. Permite
 crear ventanas, botones, campos de entrada, menús y otroscomponentes visuales en aplicaciones de escritorio de manera sencilla"""
from client.gui_app import Frame 

def main():  # definicion de una funcion
    root = tk.Tk()  # mi ventana, la raiz
    root.title('Tabla de gastos')
    root.iconbitmap('img/gastos.ico')
  # root.resizable(0,0)
    app = Frame(root=root)
    app.mainloop()  # indocamos el final de la ejecucion de la aplicacion (de nuestro bucle)


if __name__ == '__main__':
    main()
