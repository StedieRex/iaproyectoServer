import os
import pygame
import sys
class Nodo:
    global posicionXY
    global id
    global nodosAdyacentes
    global distanciaNodosAdyacentes
    global tipoCable_NodosAdyacentes
    def __init__(self,id,posicionXY):
        self.posicionXY = posicionXY
        self.id = id
        # self.nodosAdyacentes = nodosAdyacentes
        # self.distanciaNodosAdyacentes = distanciaNodosAdyacentes
        # self.tipoCable_NodosAdyacentes = tipoCable_NodosAdyacentes
        self.siguiente = None

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

    def obtenerPosicion(self):
        return self.posicionXY
    
    def obtenerId(self):
        return self.id



# Obtener el directorio actual del script, para que el directorio este en el mismo lugar que el script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Cambiar el directorio de trabajo actual al directorio del script
os.chdir(script_dir)

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




# Lista para almacenar las posiciones de los nodos
listaNodos = ListaEnlazada()

# Bucle principal
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Click izquierdo
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

    pygame.display.flip()# Actualizar la ventana

# Salir del juego
pygame.quit()
sys.exit()

