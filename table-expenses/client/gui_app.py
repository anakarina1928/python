#interfaz de usurio de la aplicacion
import tkinter as tk
from tkinter import ttk

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
    def delete_data(self):
        self.entry_date.delete(0, tk.END)
        self.entry_date.insert(0, '')
        self.entry_description.delete(0, tk.END)
        self.entry_description.insert(0, '')
        self.entry_payment_method.delete(0, tk.END)
        self.entry_payment_method.insert(0, '')
        self.entry_quantity.delete(0, tk.END)
        self.entry_quantity.insert(0, '')

    def expense_data(self, root = None):
            self.root=root
            #label de cada campo por llenar
            self.label_payment_method = tk.Label(self, text='Metodo de pago: ')
            self.label_payment_method.config(font=('Arial',12,'bold')) #configuramos el label colocando el tipo de letra, el tamaño, etc...
            self.label_payment_method.grid(row= 0, column=0, padx=10, pady=10)#indicamos en la fila y la columna que indiquemos utilizando grid

            self.label_quantity = tk.Label(self, text='Monto: ')
            self.label_quantity.config(font=('Arial',12,'bold')) 
            self.label_quantity.grid(row= 1, column=0, padx=10, pady=10)

            self.label_date = tk.Label(self, text='fecha: ')
            self.label_date.config(font=('Arial',12,'bold')) 
            self.label_date.grid(row= 2, column=0, padx=10, pady=10)

            self.label_description = tk.Label(self, text='Descripción: ')
            self.label_description.config(font=('Arial',12,'bold'))
            self.label_description.grid(row= 3, column=0, padx=10, pady=10)

            #entrys de cada campo. Los campos de entradas
            self.entry_payment_method = tk.Entry(self)
            self.entry_payment_method.config(width=50, font=('Arial',12))
            self.entry_payment_method.grid(row=0,column=1, padx=10, pady=10, columnspan=2 )

            self.entry_quantity = tk.Entry(self)
            self.entry_quantity.config(width=50, font=('Arial',12))
            self.entry_quantity.grid(row=1,column=1, padx=10, pady=10, columnspan=2)

            self.entry_date = tk.Entry(self)
            self.entry_date.config(width=50, font=('Arial',12))
            self.entry_date.grid(row=2,column=1, padx=10, pady=10, columnspan=2)

            self.entry_description = tk.Entry(self)
            self.entry_description.config(width=50, font=('Arial',12))
            self.entry_description.grid(row=3,column=1, padx=10, pady=10, columnspan=2)

            # Botones guardar , cancelar y nuevo 

            self.button_new = tk.Button(self, text='Nuevo', command= self.enable_fields)
            self.button_new.config(width=20, font=('Arial',12,'bold'), fg='#DAD5D6', bg= '#158645',cursor='hand2', activebackground='#35BD6F')
            self.button_new.grid(row= 4, column=0, padx=10, pady=10 )

            self.button_save = tk.Button(self, text='Guardar', command=self.save_data)
            self.button_save.config(width=20, font=('Arial',12,'bold'), fg='#DAD5D6', bg= '#3586DF',cursor='hand2', activebackground='#3586DF')
            self.button_save.grid(row= 4, column=1, padx=10, pady=10 )

            self.button_cancel = tk.Button(self, text='Cancelar',command=self.disable_fields)
            self.button_cancel.config(width=20, font=('Arial',12,'bold'), fg='#DAD5D6', bg= '#E15370',cursor='hand2', activebackground='#E15370')
            self.button_cancel.grid(row= 4, column=2, padx=10, pady=10 )

            # habilitando los campos 
    
    
    
    def enable_fields(self):
    
        self.entry_payment_method.config(state='normal') 
        self.entry_quantity.config(state='normal') 
        self.entry_date.config(state='normal') 
        self.entry_description.config(state='normal') 

        self.button_save.config(state='normal') 
        self.button_cancel.config(state='normal') 

            
    def disable_fields(self):
        self.delete_data()
        self.entry_payment_method.config(state='disabled') 
        self.entry_quantity.config(state='disabled') 
        self.entry_date.config(state='disabled') 
        self.entry_description.config(state='disabled') 

        self.button_save.config(state='disabled') 
        self.button_cancel.config(state='disabled') 

    def save_data(self):
        self.delete_data()

    def expense_table(self):
         self.table = ttk.Treeview(self, column=('Monto', 'metodo de pago', 'descripción', 'fecha'))

         self.table.grid(row= 5, column= 0, columnspan=4)

         self.table.heading('#0', text='ID')
         self.table.heading('#1', text='MONTO')
         self.table.heading('#2', text='METODO DE PAGO')
         self.table.heading('#3', text='DESCRIPCION')
         self.table.heading('#4', text='FECHA')
         self.table.insert('',0, tex='1', values=('123','visa','mercado','28-0-2023'))
         
         self.button_edit = tk.Button(self, text='Editar')
         self.button_edit.config(width=20, font=('Arial',12,'bold'), fg='#DAD5D6', bg= '#158645',cursor='hand2', activebackground='#35BD6F')
         self.button_edit.grid(row= 6, column=0, padx=10, pady=10 )
         
         self.button_delete = tk.Button(self, text='Eliminar')
         self.button_delete.config(width=20, font=('Arial',12,'bold'), fg='#DAD5D6', bg= '#E15370',cursor='hand2', activebackground='#E15370')
         self.button_delete.grid(row= 6, column=1, padx=10, pady=10 )


              
    
    def __init__(self, root = None):
        super().__init__(root,width= 480, height=320 )
        self.root=root
        self.pack()
        #self.config(bg='blue') # configuramos el tamaño del contenedor que hemos creado en la variable frame
        self.expense_data()
        self.disable_fields()
        self.expense_table()

        #self.disable_fields() 



   
       