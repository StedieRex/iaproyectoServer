

def main():

    initial_state =  #lo determina el usuario

if __name__ == "__main__":
    #aqui se implementa la interfaz gráfica
    import tkinter as tk
    from tkinter import messagebox
    from tkinter import scrolledtext
    def main():

        initial_state = (0,0,0,0,0,0,0,0)
        #print(initial_state)
        #print(sucesor(initial_state,False))
        #print(estadoObjetivo((1,2,3,4,5,6,7,0)))
        messagebox.showinfo("Solución",depth_first(initial_state))

    root = tk.Tk()
    root.title("Problema de las 8 reinas")
    root.geometry("825x460")
    #bloquear tamaño de la ventana
    root.resizable(0,0)
    
    button = tk.Button(root, text="Iniciar", command=main)
    button.place(x=20,y=3)

    # Crear un Frame que contendrá la caja de texto y la barra de desplazamiento
    frame_contenedor = tk.Frame(root)
    frame_contenedor.pack()
    frame_contenedor.config(width=55, height=10)
    frame_contenedor.place(x=19,y=32)

    # Crear una caja de texto con barras de desplazamiento vertical
    mostrarLiFo = scrolledtext.ScrolledText(frame_contenedor, height=25, width=97, state="disabled", wrap=tk.NONE)
    mostrarLiFo.pack(side="left", fill="both", expand=True)

    # Crear una barra de desplazamiento horizontal
    scrollbar_horizontal = tk.Scrollbar(frame_contenedor, orient=tk.HORIZONTAL, command=mostrarLiFo.xview)
    scrollbar_horizontal.place(x=0, y=388, relwidth=.98, height=20)

    # Configurar la caja de texto para desplazarse horizontalmente
    mostrarLiFo.config(xscrollcommand=scrollbar_horizontal.set)

    cajaEstadoini= tk.Text(root, height=1, width=25, state="disabled")#caja para numero de grupos 
    cajaEstadoini.place(x=180,y=3)

    initial_state = (0,0,0,0,0,0,0,0)
    cajaEstadoini.config(state="normal")
    cajaEstadoini.insert(tk.END, f"{initial_state}")
    cajaEstadoini.config(state="disabled")

    labelEstadoIni = tk.Label(root, text="Estado inicial:")
    labelEstadoIni.place(x=100,y=3)

    root.mainloop()
    