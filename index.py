#Modulo para crear aplicación
from tkinter import ttk
from tkinter import *
#Conexión a BD
import sqlite3
#Creación de clases
class Product:

    def __init__(self, window):
        self.wind = window
        self.wind.title('MobyDick')
    
    #Creación de contenedor
    frame = LabelFrame(self.wind, Text = 'Registra un nuevo producto')
    frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)
    #Crear entrada Nombre
    Label(frame, text = 'Nombre:').grip(row = 1,colimn = 0)
    self.nombre = Entry(Frame)
    self.nombre.focus()
    self.nombre.grid(row = 1, column = 1)
    #Crear entrada Precio
    Label(frame, text = 'Precio:').grid(row = 2, column = 0)
    self.precio = Entry(frame)
    self.precio.grid(row = 2, column = 1)
    #Botón Agregar Producto
    ttk.Button(frame, text = 'Agregar Producto').grid(row = 3, columnspan=2, sticky = W + E)
    #Crear Table
    self.tree = ttk.Treeview(height= 18, column = 2)
    self.tree.grid(row = 4, column = 0, columnspan = 2)


    if __name__ == '__main__':
        window = Tk()
        application = Product(window)
        window.mainloop()