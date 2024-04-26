import os
import pygame
from tkinter import ttk
from PIL import Image, ImageTk
import math
import time
# Obtener el directorio actual del script, para que el directorio este en el mismo lugar que el script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Cambiar el directorio de trabajo actual al directorio del script
os.chdir(script_dir)

# ------------- Estructuras necesarias para beamSearch -----------------
class Node1:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}  # Dictionary to store neighbors and edge information
        self.parent = None  # Parent node in the path
        self.heuristic_value = 0  # Heuristic value for A* search

    def add_neighbor(self, neighbor, speed, distance, retransmission):
        self.neighbors[neighbor] = {'speed': speed, 'distance': distance, 'retransmission': retransmission}

    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return self.name

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.name] = node

    def add_edge(self, node1, node2, speed, distance, retransmission):
        if node1.name in self.nodes and node2.name in self.nodes:
            self.nodes[node1.name].add_neighbor(node2, speed, distance, retransmission)
            self.nodes[node2.name].add_neighbor(node1, speed, distance, retransmission)
        else:
            raise ValueError("Nodes not in graph")

# --------------------- Clases para almacenar los nodos y conexiones ---------------------
class Nodo:
    global posicionXY
    global id
    def __init__(self,id,posicionXY):
        self.posicionXY = posicionXY
        self.id = id
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

# --------------------- Funciones para guardar las imagenes que generan los nodos y conexiones ---------------------
def guardarPNGmapa(guardarNodosConConexiones):
# Inicializar Pygame
    pygame.init()
    global tipoImagen

    # Definir el tamaño de la ventana
    window_width = 1000
    window_height = 600
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Sistema de Nodos")

    # Colores
    BLACK = (0, 0, 0)

    # Cargar la imagen para representar los nodos
    node_image = pygame.image.load("img/nodo.png")  # Reemplaza "nodo.png" con la ruta de tu imagen
    node_image = pygame.transform.scale(node_image, (30, 30))  # Escalar la imagen del nodo si es necesario
                    
    # cargar mapa de fondo
    background = pygame.image.load("img/mapaMexico.png")
    background = pygame.transform.scale(background, (window_width, window_height))

    # Dibujar en la ventana
    window.blit(background, (0, 0))
    
    # Dibujar los nodos 
    actual = listaNodos.cabeza
    arregloNodos = []

    while actual:
        # guardar cada nodo en un arreglo con el siguiente formato [id,posicionX,posicionY]
        #print(actual.id)
        #print(actual.posicionXY[0])
        #print(actual.posicionXY[1])
        arregloNodos.append([actual.id,actual.posicionXY[0],actual.posicionXY[1]])
        window.blit(node_image, (actual.posicionXY[0] - 15, actual.posicionXY[1] - 15))  # Dibujar la imagen del nodo en la posición
        # Dibujar el ID del nodo
        font = pygame.font.Font(None, 20)
        text_surface = font.render(str(actual.id), True, BLACK)
        text_rect = text_surface.get_rect(center=(actual.posicionXY[0], actual.posicionXY[1] + 20))
        window.blit(text_surface, text_rect)
        # Mover al siguiente nodo
        actual = actual.siguiente 

    # print(arregloNodos)
    # print("--------------------")
    # print(guadarTuplas)

    # Dibujar las conexiones
    if guardarNodosConConexiones:
        for tupla in guadarTuplas:
            nodoInicial = tupla[0]
            nodoFinal = tupla[1]
            distancia = tupla[2]
            tipoCable = tupla[3]
            # Encontrar las posiciones de los nodos

            encontrado = 0
            for nodo in arregloNodos:
                if nodo[0] == int(nodoInicial):
                    posInicialx = int(nodo[1])
                    posInicialy = int(nodo[2])
                    encontrado+=1
                elif nodo[0] == int(nodoFinal):
                    posFinalx = int(nodo[1])
                    posFinaly = int(nodo[2])
                    encontrado+=1
                if encontrado == 2:
                    break
            print(f"posInicialx: {posInicialx} posInicialy: {posInicialy} posFinalx: {posFinalx} posFinaly: {posFinaly}")
            # Dibujar la línea
            if tipoCable == 'c':
                pygame.draw.line(window, (255,165,0), (posInicialx,posInicialy), (posFinalx,posFinaly), 2)
            elif tipoCable == 'f':
                pygame.draw.line(window, (51,212,255), (posInicialx,posInicialy), (posFinalx,posFinaly), 2)
            elif tipoCable == 'r':
                pygame.draw.line(window, (255,0,0), (posInicialx,posInicialy), (posFinalx,posFinaly), 2)
            # Dibujar la distancia
            font = pygame.font.Font(None, 20)
            text_surface = font.render(distancia, True, BLACK)
            text_rect = text_surface.get_rect(center=((posInicialx+posFinalx) // 2, (posInicialy+posFinaly) // 2 - 20))
            window.blit(text_surface, text_rect)
            # Dibujar el tipo de cable
            text_surface = font.render(tipoCable, True, BLACK)
            text_rect = text_surface.get_rect(center=((posInicialx + posFinalx) // 2, (posInicialy + posFinaly) // 2 + 20))
            window.blit(text_surface, text_rect)
        tipoImagen = 2
        pygame.image.save(window, "mapa_ConConexiones.png")  # Guardar la ventana como imagen
        # Cargar la imagen en un widget Label
        nuevaImagen = Image.open("mapa_ConConexiones.png")
        nuevaImagen = nuevaImagen.resize((750, 500))
        nuevaImagen_tk = ImageTk.PhotoImage(nuevaImagen)
        label_imagen.configure(image=nuevaImagen_tk)
        label_imagen.image = nuevaImagen_tk
        
    else:
        tipoImagen = 1
        pygame.image.save(window, "mapa_SinConexiones.png")  # Guardar la ventana como imagen
        nuevaImagen = Image.open("mapa_SinConexiones.png")
        nuevaImagen = nuevaImagen.resize((750, 500))
        nuevaImagen_tk = ImageTk.PhotoImage(nuevaImagen)
        label_imagen.configure(image=nuevaImagen_tk)
        label_imagen.image = nuevaImagen_tk      
    # Salir del juego
    pygame.quit()

# --------------------- Funciones para la edición de conexiones ---------------------
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
        global nodoEnConexion
        global listaNodosParaConectar
        global conexcionSeleccionada
        global tuplasConexiones

        tuplasConexiones = []
        listaNodosParaConectar = []
        seleccion = lista2.curselection()
        #print("Seleccion: ", seleccion)
        for i in seleccion:
            #print(lista2.get(i))
            listaNodosParaConectar.append(int(lista2.get(i)))

        #print("Opciones seleccionadas: ", listaNodosParaConectar)

        #verificacion de que no existan duplas duplicadas
        if len(tuplasConexiones)>0:
            for tupla in tuplasConexiones:
                if int(conexcionSeleccionada) == tupla[0]:
                    if int(nodoEnConexion) == tupla[1]:
                        print("dupla encontrada")
                        cajaEstadoini.config(state="normal")
                        cajaEstadoini.delete('1.0', tk.END)
                        cajaEstadoini.insert(tk.END, f"dupla encontrada")
                        cajaEstadoini.config(state="disabled")
                        return
                    else:
                        print("dupla no encontrada")
                else:
                    print("dupla no encontrada")
        else:
            print("no hay duplas")
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
        # numero al azar para elegir el tipo de cable
        import random
        tipoCable = ['f','c','r']
        cable = random.choice(tipoCable)
        if cable == 'f':
            tuplasConexiones.append((conexcionSeleccionada,nodoEnConexion,cajaDistancia.get(),cable,'500','3000000000')) # nodo1,nodo2,distancia,tipoCable,retransmision(cada cuando se hace, en metros),velocidad
        elif cable == 'c':
            tuplasConexiones.append((conexcionSeleccionada,nodoEnConexion,cajaDistancia.get(),cable,'750','10000000000'))
        elif cable == 'r':
            tuplasConexiones.append((conexcionSeleccionada,nodoEnConexion,cajaDistancia.get(),cable,'200','2000000000'))
        
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
            for conexion in tuplasConexiones:
                guadarTuplas.append(conexion)
        #print(tuplasConexiones)
        #probando = tuplasConexiones[0]
        #print(probando[0])
        #print(probando[1])
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

    # caja para ingresar la distancia
    cajaDistancia = tk.Entry(ventana, width=25)#caja para numero de grupos
    cajaDistancia.place(x=150,y=300)

    boton_conectar = ttk.Button(ventana, text="Conectar", command=conectarNodos)
    boton_conectar.place(x=310,y=295)

    # boton de guardado
    boton_guardar = ttk.Button(ventana, text="Guardar", command= lambda: guardarPNGmapa(True))
    boton_guardar.place(x=310,y=330)

    # Ejecutar la ventana
    ventana.mainloop()

def editorMapaNodos():
    #variables para controlar nodos
    global comprobarContador
    global contadorID
    if comprobarContador==0:
        contadorID = 0
    # Inicializar Pygame
    pygame.init()

    # Definir el tamaño de la ventana
    window_width = 1000
    window_height = 600
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Sistema de Nodos")

    # Colores
    BLACK = (0, 0, 0)

    # Cargar la imagen para representar los nodos
    node_image = pygame.image.load("img/nodo.png")  # Reemplaza "nodo.png" con la ruta de tu imagen
    node_image = pygame.transform.scale(node_image, (30, 30))  # Escalar la imagen del nodo si es necesario

    # cargar mapa de fondo
    background = pygame.image.load("img/mapaMexico.png")
    background = pygame.transform.scale(background, (window_width, window_height))

    
    button_rect = pygame.Rect(10, 500, 150, 40)  # Rectángulo para el botón de guardar, (x, y, ancho, alto)

    # Bucle principal
    running = True
    while running:
        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and button_rect.collidepoint(event.pos):
                    guardarPNGmapa(False)
                    print("Guardando nodos")
                    pygame.quit()

                elif event.button == 1:  # Click izquierdo
                    # Crear un nuevo nodo en la posición del clic
                    contadorID += 1
                    listaNodos.ingresarNuevoNodo(contadorID,event.pos)
                    
        # Dibujar en la ventana
        window.blit(background, (0, 0))

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
        # El boton de guardar se dibuja en la esquina inferior izquierda
        pygame.draw.rect(window, (51, 255, 144), button_rect)  # Rectángulo verde
        font = pygame.font.Font(None, 30)
        text_surface = font.render("Guardar Nodos", True, BLACK)
        text_rect = text_surface.get_rect(center=button_rect.center)
        window.blit(text_surface, text_rect)

        pygame.display.flip()# Actualizar la ventana
   
    # Salir del juego
    pygame.quit()

# --------------------- Guardar y cargar nodos y conexiones ---------------------
def guardarNodosyConexiones():
    print("Guardando nodos y conexiones")
    print(guadarTuplas)
    # Crear un archivo de texto
    with open("nodos_conexiones.txt", "w") as archivo:
        for tupla in guadarTuplas:
            archivo.write(f"{tupla[0]} {tupla[1]} {tupla[2]} {tupla[3]} {tupla[4]} {tupla[5]}\n")
    print("Nodos y conexiones guardados en nodos_conexiones.txt")
    with open("nodos.txt", "w") as archivo:
        actual = listaNodos.cabeza
        while actual:
            archivo.write(f"{actual.id} {actual.posicionXY[0]} {actual.posicionXY[1]}\n")
            actual = actual.siguiente

def cargarNodosyConexiones():
    global contadorID
    global guadarTuplas
    global listaNodos
    global comprobarContador
    comprobarContador = 1
    guadarTuplas = []
    listaNodos = ListaEnlazada()
    print("Cargando nodos y conexiones")
    # Leer el archivo de texto
    with open("nodos_conexiones.txt", "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            datos = linea.split()
            guadarTuplas.append((datos[0], datos[1], datos[2], datos[3], datos[4], datos[5]))
    print("Nodos y conexiones cargados")
    print(guadarTuplas)
    with open("nodos.txt", "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            datos = linea.split()
            ingresandoPosicion = (int(datos[1]), int(datos[2]))
            listaNodos.ingresarNuevoNodo(int(datos[0]), ingresandoPosicion)
    print("Nodos cargados")
    cabeza = listaNodos.cabeza
    while cabeza:
        global contadorID
        contadorID += 1
        print(cabeza.id)
        print(cabeza.posicionXY)
        cabeza = cabeza.siguiente
    print(contadorID)

    # actualizando la imagen
    nuevaImagen = Image.open("mapa_ConConexiones.png")
    nuevaImagen = nuevaImagen.resize((750, 500))
    nuevaImagen_tk = ImageTk.PhotoImage(nuevaImagen)
    label_imagen.configure(image=nuevaImagen_tk)
    label_imagen.image = nuevaImagen_tk

#--------------------- Funciones del algoritmo de beam search ---------------------
def heuristic(edge_info, parent_node):
    global M
    M = int(caja_insertarPaquete.get())
    def serverLatency(speed, distance, retransmission):
        s1 = float(M)/float(speed)
        s2 = math.floor(distance/retransmission)
        return s1 + s2
    suma = parent_node.heuristic_value + serverLatency(edge_info['speed'], edge_info['distance'] , edge_info['retransmission'])
    return suma

def BeamSearch(graph, start, goal, beam):
    open_set = [start]
    closed_set = []
    counter = 0
    while open_set:
        print(f"open_set={open_set}")
        current_node = open_set.pop(0)
        if current_node == goal:
            path = []
            while current_node is not None:
                path.insert(0, current_node)
                current_node = current_node.parent
            return path
            
        else:
            # Generate children of current_node

            for neighbor, edge_info in graph.nodes[current_node.name].neighbors.items():
                # print(neighbor)
                if neighbor not in open_set and neighbor not in closed_set:
                    # print("not in open set neitheer close_set")
                    neighbor.parent = current_node
                    # print("current Node")
                    neighbor.heuristic_value = heuristic(edge_info, current_node)
                    # print("heuristic")
                    open_set.append(neighbor)
                    # print("open_set append")
                elif neighbor in open_set:
                    # print("in open Set")
                    # Check if the path to this neighbor from the current node is shorter
                    if neighbor.heuristic_value > heuristic(neighbor, current_node):
                        neighbor.parent = current_node
                        neighbor.heuristic_value = heuristic(neighbor, current_node)
                # elif neighbor in closed_set:
                #     print("in closed list")
                #     # Check if the path to this neighbor from the current node is shorter
                #     if neighbor.heuristic_value > heuristic(neighbor, goal):
                #         closed_set.remove(neighbor)
                #         open_set.append(neighbor)
        # print("Before close_append")
        closed_set.append(current_node)
        # print("after close_append current node")
        print(closed_set)
        print("\t",[(h, h.heuristic_value) for h in open_set])
        open_set.sort(key=lambda x: x.heuristic_value)
        print("\t",[(h, h.heuristic_value) for h in open_set])
        open_set = open_set[:beam]
        counter += 1
        print(counter)
        time.sleep(2)

    return "FAIL"


def iniciarBeamSearch():
    def miHeuristica(tupla):
        global M
        speed = int(tupla[5])
        distance = int(tupla[2])
        retransmission =  math.floor((int(tupla[2])*1000)/int(tupla[4]))
        s1 = float(M)/float(speed)
        s2 = math.floor(distance/retransmission)
        return s1 + s2
    
    def nodosHijos(np):
        hijos = [] #costo despues de pasar por heuristica, nodo padre
        for tupla in guadarTuplas:
            if int(tupla[0]) == np or int(tupla[1]) == np:
                costo = miHeuristica(tupla)
                hijos.append((costo,np))
        return hijos
    visitados = []
    inicio = 1
    fin = 5
    nodoPresente=inicio
    while nodoPresente != fin:
        visitados.append(nodoPresente)
        hijosSinOrdenar=nodosHijos(nodoPresente)




#--------------------- Crear la ventana principal ---------------------
import tkinter as tk
guadarTuplas = []

# Función para salir de la aplicación
def salir():
    ventana.destroy()

def cargar_imagen(ruta, ancho, alto):
    imagen_original = Image.open(ruta)
    imagen_redimensionada = imagen_original.resize((ancho, alto))
    imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
    return imagen_tk

# Inicializar variables
comprobarContador = 0
contadorID = 0
tipoImagen = 0
M = 0 # M es el tamano de dato que enviaremos

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana con Menú")
ventana.geometry("1200x600")

#--------------------- Crear el menú ---------------------
# Crear el menú
menu_principal = tk.Menu(ventana)
ventana.config(menu=menu_principal)
# Crear el menú "Archivo"
menu_archivo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Crear Nodos", command=editorMapaNodos)
menu_archivo.add_command(label="Enlazar Nodos", command=edicionConexiones)
menu_archivo.add_command(label="Guardar", command= guardarNodosyConexiones)
menu_archivo.add_command(label="Cargar", command=cargarNodosyConexiones)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)
# Crear el menú "Ayuda"
menu_ayuda = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Ayuda", menu=menu_ayuda)


#--------------------- Cargar imagen ---------------------
# Definir el tamaño deseado para la imagen
ancho_deseado = 750
alto_deseado = 500
# Cargar y redimensionar la imagen

imagen_tk = cargar_imagen("img/mapaMexico.png", ancho_deseado, alto_deseado)
# Mostrar la imagen en un widget Label
label_imagen = tk.Label(ventana, image=imagen_tk)
label_imagen.place(x=10, y=40)



#--------------------- Crear la lista de nodos ---------------------
#Etiqueta para la lista de nodos
etiqueta_lista = tk.Label(ventana, text="Mostrando ejecucion del algoritmo:")
etiqueta_lista.place(x=800,y=10)
#caja para mostrar como funciona el algortimo
caja_mostrarCamino = tk.Text(ventana, height=25, width=25,state="disabled")#caja para numero de grupos
caja_mostrarCamino.place(x=800,y=40)

#--------------------- insertar tam del paquete ---------------------

caja_insertarPaquete = tk.Entry(ventana, width=25)#caja para numero de grupos
caja_insertarPaquete.place(x=825,y=500)

etiqueta_insertarPaquete = tk.Label(ventana, text="Insertar tamaño del paquete:")
etiqueta_insertarPaquete.place(x=800,y=470)

boton_Comenzar = ttk.Button(ventana, text="Comenzar", command=iniciarBeamSearch)
boton_Comenzar.place(x=825,y=530)
# Mostrar la ventana
ventana.mainloop()