#interfaz de usurio de la aplicacion
import tkinter as tk


#funcion para crear barra de menu
def menu_bar(root):
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar,width= 300, height=300)#anclamos la barra de menu de la libreria tk a la interfaz

    menu_home=tk.Menu(menu_bar,tearoff=0)
    menu_bar.add_cascade(label= 'Inicio',menu= menu_home)
    
    menu_home.add_command(label = 'crear registro en base de datos')
    menu_home.add_command(label = 'Eliminar registro DB')
    menu_home.add_command(label = 'Salir', command= root.destroy)#es un método de tk que se utiliza para agregar un elemento de tipo 
    #comando a un menú. Un elemento de comando en un menú es una opción que el usuario puede seleccionar 
    #y que ejecutará una función específica cuando se haga clic en ella.
    
class Frame(tk.Frame):# utilizo la clase Frame de la libreria tk y creo una subclase
    def expense_data(self, root = None):
            self.root=root
            #label de cada campo por llenar
            self.label_payment_method = tk.Label(self, text='Metodo de pago: ')
            self.label_payment_method.grid(row= 0, column=0)#indicamos en la fila y la columna que indiquemos utilizando grid
    
    def __init__(self, root = None):
        super().__init__(root,width= 480, height=320 )
        self.root=root
        self.pack()
        self.config(bg='blue') # configuramos el tamaño del contenedor que hemos creado en la variable frame
        self.expense_data()

   
       