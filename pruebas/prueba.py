import tkinter as tk
import pygame
import sys

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla de Pygame
ANCHO = 400
ALTO = 300

# Función para dibujar un cuadrado en Pygame
def dibujar_cuadrado(surface, x, y):
    pygame.draw.rect(surface, (255, 0, 0), (x, y, 50, 50))

# Función principal de Pygame
def main_pygame(canvas):
    pantalla = pygame.Surface((ANCHO, ALTO))

    x = 0
    y = 0
    velocidad_x = 5

    reloj = pygame.time.Clock()

    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        # Actualizar lógica del juego
        x += velocidad_x
        if x >= ANCHO - 50 or x <= 0:
            velocidad_x *= -1

        # Dibujar en la pantalla de Pygame
        pantalla.fill((0, 0, 0))
        dibujar_cuadrado(pantalla, x, y)

        # Renderizar pantalla de Pygame en el canvas de Tkinter
        imagen = pygame.image.frombuffer(pantalla.get_buffer(), (ANCHO, ALTO), 'RGB')
        canvas.create_image(0, 0, image=imagen, anchor=tk.NW)

        # Actualizar ventana de Tkinter
        ventana.update()

        reloj.tick(30)

    pygame.quit()
    sys.exit()

# Función principal de Tkinter
def main_tkinter():
    ventana = tk.Tk()
    ventana.title("Pygame en Tkinter")

    canvas = tk.Canvas(ventana, width=ANCHO, height=ALTO)
    canvas.pack()

    # Iniciar juego de Pygame en un hilo separado
    import threading
    pygame_thread = threading.Thread(target=main_pygame, args=(canvas,))
    pygame_thread.start()

    ventana.mainloop()

if __name__ == "__main__":
    main_tkinter()
