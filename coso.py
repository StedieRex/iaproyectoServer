import tkinter as tk
from tkinter import ttk

# Función para manejar la selección de la lista
def seleccionar():
    seleccion = lista.curselection()
    opciones_seleccionadas.set([lista.get(i) for i in seleccion])

# Crear la ventana
ventana = tk.Tk()
ventana.title("Ventana con Lista Scrollable (Selección Múltiple)")

# Crear un marco para la lista con scroll
marco = ttk.Frame(ventana)
marco.pack(fill='both', expand=True)

# Crear una barra de desplazamiento
scrollbar = ttk.Scrollbar(marco, orient='vertical')
scrollbar.pack(side='right', fill='y')

# Crear una lista con selección múltiple
opciones = ["Opción 1", "Opción 2", "Opción 3", "Opción 4", "Opción 5", "Opción 6", "Opción 7", "Opción 8", "Opción 9", "Opción 10"]
lista = tk.Listbox(marco, yscrollcommand=scrollbar.set, selectmode='multiple')
for opcion in opciones:
    lista.insert('end', opcion)
lista.pack(side='left', fill='both', expand=True)

# Configurar la barra de desplazamiento para controlar la lista
scrollbar.config(command=lista.yview)

# Variable para almacenar las opciones seleccionadas
opciones_seleccionadas = tk.StringVar()

# Botón para seleccionar
boton_seleccionar = ttk.Button(ventana, text="Seleccionar", command=seleccionar)
boton_seleccionar.pack()

# Etiqueta para mostrar las opciones seleccionadas
etiqueta_opciones = ttk.Label(ventana, textvariable=opciones_seleccionadas)
etiqueta_opciones.pack()

# Ejecutar la ventana
ventana.mainloop()
