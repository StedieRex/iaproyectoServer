import os
import pygame
import sys
from tkinter import ttk

# Obtener el directorio actual del script, para que el directorio este en el mismo lugar que el script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Cambiar el directorio de trabajo actual al directorio del script
os.chdir(script_dir)

class Nodo:
    global posicionXY
    global id
    def __init__(self,id,posicionXY):
        self.posicionXY = posicionXY
        self.id = id
        # self.nodosAdyacentes = nodosAdyacentes
        # self.distanciaNodosAdyacentes = distanciaNodosAdyacentes
        # self.tipoCable_NodosAdyacentes = tipoCable_NodosAdyacentes
        self.siguiente = None
    def obtenerPosicion(self):
        return self.posicionXY
    
    def obtenerId(self):
        return self.id

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def ingresarNuevoNodo(self,id,posicionXY):
        nuevo_nodo = Nodo(id,posicionXY)
        self.posicionXY = posicionXY
        self.id = id
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

# Lista para almacenar las posiciones de los nodos
listaNodos=ListaEnlazada()

def guardarPNGmapa():
# Inicializar Pygame
    pygame.init()

    # Definir el tamaño de la ventana
    window_width = 1000
    window_height = 600
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Sistema de Nodos")

    # Colores
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Cargar la imagen para representar los nodos
    node_image = pygame.image.load("img/nodo.png")  # Reemplaza "nodo.png" con la ruta de tu imagen
    node_image = pygame.transform.scale(node_image, (30, 30))  # Escalar la imagen del nodo si es necesario
                    
    # Dibujar en la ventana
    window.fill(WHITE)  # Llenar la ventana con color blanco
    
    # Dibujar los nodos 
    actual = listaNodos.cabeza
    while actual:
        window.blit(node_image, (actual.posicionXY[0] - 15, actual.posicionXY[1] - 15))  # Dibujar la imagen del nodo en la posición
        # Dibujar el ID del nodo
        font = pygame.font.Font(None, 20)
        text_surface = font.render(str(actual.id), True, BLACK)
        text_rect = text_surface.get_rect(center=(actual.posicionXY[0], actual.posicionXY[1] + 20))
        window.blit(text_surface, text_rect)
        # Mover al siguiente nodo
        actual = actual.siguiente 

    pygame.image.save(window, "mapa_nodos.png")  # Guardar la ventana como imagen

    # Salir del juego
    pygame.quit()

def edicionConexiones():
    # Función para manejar la selección de la lista

    def seleccionar():
        seleccion = lista.curselection()
        for i in seleccion:
            opcion_seleccionada.set(lista.get(i))
        print("Opción seleccionada: ", opcion_seleccionada.get())
        global conexcionSeleccionada
        conexcionSeleccionada = opcion_seleccionada.get()
        #actualizar lista de nodos para conectar
        opciones = []
        actual = listaNodos.cabeza
        while actual:
            if str(actual.id) != str(conexcionSeleccionada):
                opciones.append(str(actual.id))
            actual = actual.siguiente
        lista2.delete(0, tk.END)
        for opcion in opciones:
            lista2.insert('end', opcion)
    
    def grupoParaConectar():
        global listaNodosParaConectar
        listaNodosParaConectar = []
        seleccion = lista2.curselection()
        print("Seleccion: ", seleccion)
        for i in seleccion:
            print(lista2.get(i))
            listaNodosParaConectar.append(int(lista2.get(i)))

        print("Opciones seleccionadas: ", listaNodosParaConectar)

        global nodoEnConexion
        nodoEnConexion=listaNodosParaConectar[0]
        listaNodosParaConectar=listaNodosParaConectar[1:]
        cajaEstadoini.config(state="normal")
        cajaEstadoini.delete('1.0', tk.END)
        cajaEstadoini.insert(tk.END, f"{conexcionSeleccionada}->{nodoEnConexion}")
        cajaEstadoini.config(state="disabled")
        

    def conectarNodos():
        global tuplasConexiones
        global nodoEnConexion
        global listaNodosParaConectar
        tuplasConexiones=[]
        # numero al azar para elegir el tipo de cable
        import random
        tipoCable = ['f','c','r']
        tuplasConexiones.append((conexcionSeleccionada,nodoEnConexion,cajaDistancia.get("1.0",tk.END),random.choice(tipoCable)))
        if len(listaNodosParaConectar)>0:
            nodoEnConexion=listaNodosParaConectar[0]
            listaNodosParaConectar=listaNodosParaConectar[1:]
            cajaEstadoini.config(state="normal")
            cajaEstadoini.delete('1.0', tk.END)
            cajaEstadoini.insert(tk.END, f"{conexcionSeleccionada}->{nodoEnConexion}")
            cajaEstadoini.config(state="disabled")
        else:
            cajaEstadoini.config(state="normal")
            cajaEstadoini.delete('1.0', tk.END)
            cajaEstadoini.insert(tk.END, f"Sin conexiones")
            cajaEstadoini.config(state="disabled")
            lista2.delete(0, tk.END)

        print(tuplasConexiones)
        
    # Crear la ventana
    ventana = tk.Tk()
    ventana.title("Ventana con Lista Scrollable")
    ventana.geometry("400x400")

    # Crear un marco para la lista con scroll
    marco = ttk.Frame(ventana)
    marco.pack(fill='both', expand=False)
    marco.place(x=0,y=0)
    marco.config(width=200, height=200)

    # Crear una barra de desplazamiento
    scrollbar = ttk.Scrollbar(marco, orient='vertical')
    scrollbar.pack(side='right', fill='y')

    # Crear una lista
    actual = listaNodos.cabeza
    opciones = []
    while actual:
        opciones.append(str(actual.id))
        actual = actual.siguiente

    lista = tk.Listbox(marco, yscrollcommand=scrollbar.set)
    for opcion in opciones:
        lista.insert('end', opcion)
    lista.pack(side='left', fill='both', expand=True)

    # Configurar la barra de desplazamiento para controlar la lista
    scrollbar.config(command=lista.yview)

    # Variable para almacenar la opción seleccionada
    opcion_seleccionada = tk.StringVar()
    opcion_seleccionada.set("Seleccione una opción")

    # Botón para seleccionar
    boton_seleccionar1 = ttk.Button(ventana, text="Seleccionar", command=seleccionar)
    boton_seleccionar1.place(x=0,y=200)

    # Etiqueta para mostrar la opción seleccionada
    etiqueta_opcion = ttk.Label(ventana, textvariable=opcion_seleccionada)
    etiqueta_opcion.pack()

    # ---------------------------- Lista de seleccion multiple ----------------------------

    # Crear un marco para la lista con scroll
    marco1 = ttk.Frame(ventana)
    marco1.pack(fill='both', expand=False)
    marco1.place(x=200,y=0)
    marco1.config(width=200, height=200)

    # Crear una barra de desplazamiento
    scrollbar = ttk.Scrollbar(marco1, orient='vertical')
    scrollbar.pack(side='right', fill='y')

    # Crear una lista con selección múltiple
    lista2 = tk.Listbox(marco1, yscrollcommand=scrollbar.set, selectmode='multiple')
    # for opcion in opciones:
    #     lista2.insert('end', opcion)
    lista2.pack(side='left', fill='both', expand=True)

    # Configurar la barra de desplazamiento para controlar la lista
    scrollbar.config(command=lista2.yview)

    # Variable para almacenar las opciones seleccionadas
    opciones_seleccionadas = tk.StringVar()

    # Botón para seleccionar
    boton_seleccionar2 = ttk.Button(ventana, text="Conectar grupo", command=grupoParaConectar)
    boton_seleccionar2.place(x=200,y=200)

    # Etiqueta para mostrar las opciones seleccionadas
    etiqueta_opciones = ttk.Label(ventana, textvariable=opciones_seleccionadas)
    etiqueta_opciones.pack()

    # ---------------------------- Caja de texto de la lineas seleccionadas ----------------------------
    # caja donde se muestra la coenxion
    cajaEstadoini= tk.Text(ventana, height=1, width=25, state="disabled")#caja para numero de grupos 
    cajaEstadoini.place(x=0,y=300)
    cajaEstadoini.config(width=16, height=1)

    initial_state = "Sin conexiones"
    cajaEstadoini.config(state="normal")
    cajaEstadoini.insert(tk.END, f"{initial_state}")
    cajaEstadoini.config(state="disabled")

    # etiqueta de dos puntos
    labelDosPuntos = tk.Label(ventana, text=":")
    labelDosPuntos.place(x=140,y=300)
    # caja donde se incerta la distancia
    cajaDistancia= tk.Text(ventana, height=1, width=16, state="normal")#caja para numero de grupos
    cajaDistancia.place(x=150,y=300)
    # boton para guardar la conexion    
    boton_guardar = ttk.Button(ventana, text="Enlazar", command=conectarNodos)
    boton_guardar.place(x=300,y=300)
    # Ejecutar la ventana
    ventana.mainloop()

def editorMapaNodos():
    #variables para controlar nodos
    id = 0

    # Inicializar Pygame
    pygame.init()

    # Definir el tamaño de la ventana
    window_width = 1000
    window_height = 600
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Sistema de Nodos")

    # Colores
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Cargar la imagen para representar los nodos
    node_image = pygame.image.load("img/nodo.png")  # Reemplaza "nodo.png" con la ruta de tu imagen
    node_image = pygame.transform.scale(node_image, (30, 30))  # Escalar la imagen del nodo si es necesario
    
    button_rect = pygame.Rect(150, 100, 100, 50)  # Rectángulo para el botón de guardar

    # Bucle principal
    running = True
    while running:
        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and button_rect.collidepoint(event.pos):
                    pygame.quit()

                elif event.button == 1:  # Click izquierdo
                    # Crear un nuevo nodo en la posición del clic
                    id += 1
                    listaNodos.ingresarNuevoNodo(id,event.pos)
                    
        # Dibujar en la ventana
        window.fill(WHITE)  # Llenar la ventana con color blanco
        
        # Dibujar los nodos 
        actual = listaNodos.cabeza
        while actual:
            window.blit(node_image, (actual.posicionXY[0] - 15, actual.posicionXY[1] - 15))  # Dibujar la imagen del nodo en la posición
            # Dibujar el ID del nodo
            font = pygame.font.Font(None, 20)
            text_surface = font.render(str(actual.id), True, BLACK)
            text_rect = text_surface.get_rect(center=(actual.posicionXY[0], actual.posicionXY[1] + 20))
            window.blit(text_surface, text_rect)
            # Mover al siguiente nodo
            actual = actual.siguiente 

        # Dibujar el botón de guardar
        pygame.draw.rect(window, (0, 255, 0), button_rect)  # Rectángulo verde
        font = pygame.font.Font(None, 30)
        text_surface = font.render("Crear conexiones", True, BLACK)
        text_rect = text_surface.get_rect(center=button_rect.center)
        window.blit(text_surface, text_rect)

        pygame.display.flip()# Actualizar la ventana

    # Salir del juego
    pygame.quit()
    sys.exit()

import tkinter as tk

def opcion2():
    print("Opción 2 seleccionada")

def opcion3():
    print("Opción 3 seleccionada")

# Función para salir de la aplicación
def salir():
    ventana.destroy()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana con Menú")

# Crear el menú
menu_principal = tk.Menu(ventana)
ventana.config(menu=menu_principal)

# Crear el menú "Archivo"
menu_archivo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Crear Nodos", command=editorMapaNodos)
menu_archivo.add_command(label="Enlazar Nodos", command=edicionConexiones)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)

# Crear el menú "Ayuda"
menu_ayuda = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Ayuda", menu=menu_ayuda)
menu_ayuda.add_command(label="Opción 3", command=opcion3)

# Mostrar la ventana
ventana.mainloop()