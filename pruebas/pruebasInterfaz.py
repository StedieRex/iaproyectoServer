
import os
import pygame
import sys
# Obtener el directorio actual del script, para que el directorio este en el mismo lugar que el script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Cambiar el directorio de trabajo actual al directorio del script
os.chdir(script_dir)

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
nodes = []

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
                nodes.append(event.pos)
                
    # Dibujar en la ventana
    window.fill(WHITE)  # Llenar la ventana con color blanco
    
    # Dibujar los nodos
    for node_pos in nodes:
        window.blit(node_image, (node_pos[0] - 15, node_pos[1] - 15))  # Dibujar la imagen del nodo en la posición
        
    pygame.display.flip()

# Salir del juego
pygame.quit()
sys.exit()

