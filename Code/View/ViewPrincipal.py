
import tkinter as tk
from View.ViewSecundary import ViewSecundary
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



class ViewPrincipal:
    cities = [
        "Ciudad de México",
        "Guadalajara",
        "Ciudad Juárez",
        "Tijuana",
        "Zapopan",
        "Monterrey",
        "Chihuahua",
        "Mérida",
        "San Luis Potosí",
        "Aguascalientes",
        "Hermosillo",
        "Saltillo",
        "Mexicali",
        "Culiacán",
        "Acapulco de Juárez"
    ]

    opcions = ["Camino mas Largo", "Camino mas Corto", "Corto y Largo"]

    def __init__(self, ControllerPrincipal):
        self.ControllerPrincipal = ControllerPrincipal
        self.root = tk.Tk()
        self.root.title("Algoritmo Heuristico")
        self.root.config(bg="#ececec")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.frame0 = tk.Frame(self.root, borderwidth=2, relief="ridge", bg="#c2dfdd")
        self.frame0.pack(padx=10, pady=10, side="top")

        # Crea un solo frame para el gráfico
        self.frame_min = tk.Frame(self.root, borderwidth=2, relief="ridge", bg="#c2dfdd")
        self.frame_min.pack(padx=10, pady=10, side="left")
        self.frame_max = tk.Frame(self.root, borderwidth=2, relief="ridge", bg="#c2dfdd")
        self.frame_max.pack(padx=10, pady=10, side="right")

    def iniciar(self):
        self.crearVentanaPrinciapl()

        # Crea la vista secundaria
        self.view_secundary = ViewSecundary()

        self.crearVentanaConGrafo_min()

        self.crearVentanaConGrafo_max()

        self.root.mainloop()

    def crearVentanaPrinciapl(self):
        self.label_eleccion = tk.Label(self.frame0, text="Elige la ciudad de partida")
        self.label_eleccion.grid(row=0, column=0, padx=10, pady=10)

        self.comboBox_ciudades = tk.Spinbox(self.frame0, values=self.cities, bg="#c2dfdd")
        self.comboBox_ciudades.grid(row=0, column=1, padx=10, pady=10)

        self.button_empezar = tk.Button(self.frame0, text="Empezar", command=self.ControllerPrincipal.realizarAccion, bg="#15e295", activebackground="#00ff7f", state="normal")
        self.button_empezar.grid(row=0, column=2)

        self.button_reinicio = tk.Button(self.frame0, text="Volver a elegir", command=self.ControllerPrincipal.reiniciar, bg="#15e295", activebackground="#00ff7f", state="disabled")
        self.button_reinicio.grid(row=1, column=1)

    def crearVentanaConGrafo_min(self):
        # Obtén el grafo de la vista secundaria
        self.G = self.view_secundary.get_graph_min()

        # Dibuja el grafo con la imagen de fondo
        self.view_secundary.draw_graph_in_figure_min(self.G)

        # Crea un lienzo para mostrar la figura en el frame_min
        self.canvas_secundary_min = FigureCanvasTkAgg(self.view_secundary.draw_graph_in_figure_min(self.view_secundary.get_graph_min()), master=self.frame_min)
        self.canvas_secundary_min.get_tk_widget().pack()

    def crearVentanaConGrafo_max(self):
        # Obtén el grafo de la vista secundaria
        self.G = self.view_secundary.get_graph_max()

        # Dibuja el grafo con la imagen de fondo
        self.view_secundary.draw_graph_in_figure_min(self.G)

        # Crea un lienzo para mostrar la figura en el frame_max
        self.canvas_secundary_max = FigureCanvasTkAgg(self.view_secundary.draw_graph_in_figure_max(self.view_secundary.get_graph_max()), master=self.frame_max)
        self.canvas_secundary_max.get_tk_widget().pack()

    def on_closing(self):
        self.root.destroy()

    def obtenerCiudad(self):
        city = str(self.comboBox_ciudades.get())

        self.comboBox_ciudades.config(state="disabled")
        self.button_empezar.config(state="disabled")
        self.button_reinicio.config(state="normal")

        return city

    def reiniciar(self):
        self.button_empezar.config(state="normal")
        self.comboBox_ciudades.config(state="normal")

        # Elimina el lienzo actual del gráfico mínimo
        self.canvas_secundary_min.get_tk_widget().destroy()

        # Crea un nuevo grafo vacío para el gráfico mínimo
        self.view_secundary = ViewSecundary()

        # Vuelve a crear el lienzo con el nuevo grafo mínimo
        self.crearVentanaConGrafo_min()

        # Elimina el lienzo actual del gráfico máximo
        self.canvas_secundary_max.get_tk_widget().destroy()

        # Crea un nuevo grafo vacío para el gráfico máximo
        self.view_secundary = ViewSecundary()

        # Vuelve a crear el lienzo con el nuevo grafo máximo
        self.crearVentanaConGrafo_max()
        
    def generate_lines_min(self, ciudad_origen, ciudad_destino):
        self.view_secundary.generate_lines_min(ciudad_origen, ciudad_destino)
        G = self.view_secundary.get_graph_min()
        self.canvas_secundary_min.get_tk_widget().destroy()
        self.canvas_secundary_min = FigureCanvasTkAgg(self.view_secundary.draw_graph_in_figure_min(G), master=self.frame_min)
        self.canvas_secundary_min.get_tk_widget().pack()

    def generate_lines_max(self, ciudad_origen, ciudad_destino):
        self.view_secundary.generate_lines_max(ciudad_origen, ciudad_destino)
        G = self.view_secundary.get_graph_max()
        self.canvas_secundary_max.get_tk_widget().destroy()
        self.canvas_secundary_max = FigureCanvasTkAgg(self.view_secundary.draw_graph_in_figure_max(G), master=self.frame_max)
        self.canvas_secundary_max.get_tk_widget().pack()