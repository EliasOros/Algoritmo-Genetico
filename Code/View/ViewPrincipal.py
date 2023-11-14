import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from View.ViewSecundary import ViewSecundary
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ViewPrincipal:
    
    

    opcions = ["Camino mas Largo", "Camino mas Corto", "Corto y Largo"]

    def __init__(self, ControllerPrincipal):
        self.ControllerPrincipal = ControllerPrincipal
        self.root = tk.Tk()
        self.root.title("Algoritmo Heuristico")
        self.root.config(bg="#062720")
        self.root.geometry("1060x505")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
       
    def iniciar(self):
        self.crearVentanaPrinciapl()

        # Crea la vista secundaria
        self.view_secundary = ViewSecundary()

        self.crearVentanaConGrafo()

        self.root.mainloop()

    def crearVentanaPrinciapl(self):
        
        self.frame0 = tk.Frame(self.root, borderwidth=2, relief="ridge", bg="#c2dfdd")
        self.frame0.pack(padx=10, pady=10, side="left" )
        
        self.frame1 = tk.Frame(self.frame0, borderwidth=2, relief="ridge", bg="#03b964")
        self.frame1.grid(row=0,column=0,padx=10, pady=10, )
        
        #--------------------------------------------------------------------------------------------------
        frame_ciudad = tk.Frame(self.frame1, bg="#ffb750", borderwidth=2, relief="ridge")
        frame_ciudad.pack(padx=10, pady=10, side="top")

        self.label_ciudades = tk.Label(frame_ciudad, text="Elige la ciudad de partida", bg="#ffb750")
        self.label_ciudades.pack(side="left", padx=10)
        
        cities = self.ControllerPrincipal.model.ciudades

        self.comboBox_ciudades = tk.Spinbox(frame_ciudad, values=cities, bg="#ffc700")
        self.comboBox_ciudades.pack(side="left", padx=10)
        #--------------------------------------------------------------------------------------------------
        frame_ruta = tk.Frame(self.frame1, bg="#ffb750", borderwidth=2, relief="ridge")
        frame_ruta.pack(padx=10, pady=10, side="top")

        self.label_ruta = tk.Label(frame_ruta, text="Elige la ruta de preferencia", bg="#ffb750")
        self.label_ruta.pack(side="left", padx=10)

        self.opciones = ["Corto", "Largo"]
        
        self.comboBox_ruta = tk.Spinbox(frame_ruta, values=self.opciones, bg="#ffc700")
        self.comboBox_ruta.pack(side="left", padx=10)
        #--------------------------------------------------------------------------------------------------
        self.button_empezar = tk.Button(self.frame1, text="Empezar", command=self.ControllerPrincipal.realizarAccion, bg="#15e295", activebackground="#ffc700", state="normal")
        self.button_empezar.pack(pady=10, side="top", ipadx=20)  # Ajusta ipadx según tus preferencias
        #--------------------------------------------------------------------------------------------------
        self.frame_text = tk.Frame(self.frame0,bg="#03b964", borderwidth=2, relief="ridge")
        self.frame_text.grid(row=1,column=0,padx=10, pady=10)
        
        self.scroll_text = scrolledtext.ScrolledText(self.frame_text, wrap=tk.WORD, width=40, height=18, state="disabled",bg="#15e295")
        self.scroll_text.pack(padx=5, pady=5, side="top")
        #--------------------------------------------------------------------------------------------------
            
        self.mensaje_bienvenida = messagebox.showinfo("Bienvenida","Este programa esta basado en Algoritmos Heuristicos \nEl programa genera de la ruta mas corta o mas larga, pasando entre 15 ciudades de mexico (origen a origen)")
        #--------------------------------------------------------------------------------------------------
      
        self.frame_grafo = tk.Frame(self.root,bg="#ffc700", borderwidth=2, relief="ridge" )
        self.frame_grafo.pack(padx=10, pady=10)
        
    def crearVentanaConGrafo (self):
        
        self.G = self.view_secundary.get_graph
        
        self.view_secundary.draw_graph_in_figure(self.G)
        
        self.canvas_secundary = FigureCanvasTkAgg(self.view_secundary.draw_graph_in_figure(self.view_secundary.get_graph()), master=self.frame_grafo)
        self.canvas_secundary.get_tk_widget().pack()

    def on_closing(self):
        self.root.destroy()
        self.view_secundary.close_figures()

    def obtenerCiudad(self):
        city = str(self.comboBox_ciudades.get())

        option = str(self.comboBox_ruta.get())
        
        return city,option

    def reiniciar(self):
        
        # Elimina el lienzo actual del gráfico mínimo
        self.canvas_secundary.get_tk_widget().destroy()

        # Crea un nuevo grafo vacío para el gráfico mínimo
        self.view_secundary = ViewSecundary()

        # Vuelve a crear el lienzo con el nuevo grafo mínimo
        self.crearVentanaConGrafo()
        
    
           
    def generate_lines(self, ciudad_origen, ciudad_destino,text):
        self.view_secundary.generate_lines(ciudad_origen, ciudad_destino,text)
        G = self.view_secundary.get_graph()
        self.canvas_secundary.get_tk_widget().destroy()
        self.canvas_secundary = FigureCanvasTkAgg(self.view_secundary.draw_graph_in_figure(G), master=self.frame_grafo)
        self.canvas_secundary.get_tk_widget().pack()
        
    def imprimir_en_scroll(self, mensaje):
        self.scroll_text.config(state=tk.NORMAL)  # Habilita la edición del widget
        self.scroll_text.delete(1.0, tk.END)  # Borra el contenido actual del widget
        self.scroll_text.insert(tk.END, mensaje)  # Inserta el nuevo mensaje al final del widget
        self.scroll_text.see(tk.END)  # Hace que el widget muestre automáticamente el contenido nuevo
        self.scroll_text.config(state=tk.DISABLED)  # Deshabilita la edición del widget después de imprimir
        
        
        
if __name__ == "__main__":
    
    vw = ViewPrincipal()
    
    vw.iniciar()