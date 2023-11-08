
import tkinter as tk
from View.ViewSecundary import ViewSecundary
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



class ViewPrincipal:
    
    cities = [
    "Ciudad de México",
    "Guadalajara",
    "Ciudad Juarez",
    "Tijuana",
    "Zapopan",
    "Monterrey",
    "Chihuahua",
    "Merida",
    "San Luis Potosi",
    "Aguascalientes",
    "Hermosillo",
    "Saltillo",
    "Mexicali",
    "Culiacan",
    "Acapulco de Juarez"
    ]
    
    opcions = ["Camino mas Largo","Camino mas Corto","Corto y Largo"]
    
    def on_closing(self):
        self.root.destroy()

    def __init__(self):
        #self.controlador = controlador  # Asegúrate de que la vista tenga una referencia al controlador
        self.root = tk.Tk()
        self.root.title("Algoritmo Heuristico")
        self.root.config(bg="#ececec")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing )
        
    def iniciar(self):
        
        self.crearVentanaPrinciapl()
        
        # Crea la vista secundaria
        self.view_secundary = ViewSecundary()
        
        self.crearVentanaConGrafo()
        
        self.root.mainloop()
    
    def crearVentanaPrinciapl(self):
        
        self.frame0 = tk.Frame(self.root, borderwidth=2, relief="ridge",bg="#c2dfdd")
        self.frame0.pack(padx=10, pady=10, side="left")
        
        self.label0 = tk.Label(self.frame0, text="Elige la ciudad de partida")
        self.label0.grid(row=0, column=0, padx=10, pady=10)
        
        self.comboBox = tk.Spinbox(self.frame0,values=self.cities,bg="#c2dfdd")
        self.comboBox.grid(row=0,column=1,padx=10,pady=10)
        
        self.button_label0 = tk.Button(self.frame0, text="Elegir", command=self.obtenerCiudad,bg="#15e295",activebackground= "#00ff7f")
        self.button_label0.grid(row=0, column=2)
        
            
        self.label0 = tk.Label(self.frame0, text="Elige que tipo de recorrido quieres hacer")
        self.label0.grid(row=1, column=0, padx=10, pady=10)
        
        self.comboBox1 = tk.Spinbox(self.frame0,values=self.opcions,bg="#c2dfdd",state="disabled")
        self.comboBox1.grid(row=1,column=1,padx=10,pady=10)
        
        self.button_label1 = tk.Button(self.frame0, text="Empezar", command="poner comando",bg="#15e295",activebackground= "#00ff7f",state="disabled")
        self.button_label1.grid(row=1, column=2)
        
    def crearVentanaConGrafo(self):
        
        self.frame1 = tk.Frame(self.root,borderwidth=2, relief="ridge",bg="#c2dfdd")
        self.frame1.pack(padx=10, pady=10, side="right")       
                       
        # Obtén la figura de la vista secundaria
        self.fig_secundary = self.view_secundary.draw_graph_in_figure()

        # Crea un lienzo para mostrar la figura en el frame1
        self.canvas_secundary = FigureCanvasTkAgg(self.fig_secundary, master=self.frame1)
        self.canvas_secundary.get_tk_widget().pack()
        
    def obtenerCiudad(self):
        
        city = self.comboBox.get()
        
        self.comboBox.config(state="disabled")
        self.button_label0.config(state="disabled")
        self.comboBox1.config(state="normal")
        self.button_label1.config(state="normal")
            
           
        return city
    
    
        
    
'''if __name__ == "__main__":
    ventana_emergente = ViewPrincipal() 
    ventana_emergente.iniciar()  '''    
        
    
    