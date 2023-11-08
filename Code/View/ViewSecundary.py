import networkx as nx
import matplotlib.pyplot as plt

class ViewSecundary:
    def __init__(self):
        # Crea un grafo vacío
        self.G = nx.Graph()

        # Agrega nodos que representen ciudades o estados
        self.add_city("Ciudad de México", 2.86, -0.815)
        self.add_city("Guadalajara", 2.270, -0.625)   
        self.add_city("Ciudad Juarez", 1.700, 1.180)
        self.add_city("Tijuana", 0.425,1.430 )
        self.add_city("Zapopan", 2.145, -0.555)      
        self.add_city("Monterrey", 2.680,0.235)
        self.add_city("Chihuahua", 1.800, 0.720)
        self.add_city("Merida", 4.300, -0.440)
        self.add_city("San Luis Potosi",2.600, -0.300)
        self.add_city("Aguascalientes", 2.385, 0.365)
        self.add_city("Hermosillo", 1.200, 0.715)
        self.add_city("Saltillo", 2.574, 0.100)
        self.add_city("Mexicali", 0.650, 1.330)
        self.add_city("Culiacan", 1.700, 0.020)
        self.add_city("Acapulco de Juarez", 2.710,-1.140)

        # Obtiene las posiciones de los nodos
        self.pos = nx.get_node_attributes(self.G, 'pos')

        # Carga la imagen de fondo
        self.background_image = plt.imread("Code/Others/Images/republica.jpg")
        print("Imagen cargada correctamente")

    def add_city(self, name, x, y):
        self.G.add_node(name, pos=(x, y))

    def generate_lines(self, cityA, cityB):
        self.G.add_edge(cityA, cityB)

    def draw_graph_in_figure(self):
        # Dibuja el grafo con la imagen de fondo
        fig, ax = plt.subplots()
        ax.imshow(self.background_image, extent=[0, 5, -2, 2])

        # Dibuja los nodos
        nx.draw(self.G, self.pos, with_labels=True, node_color='blue', node_size=8, font_size=5, font_color='black')

        # No muestres el gráfico aquí, solo devuélvelo
        return fig

if __name__ == "__main__":
    view = ViewSecundary()
    view.generate_lines("Ciudad de México", "Guadalajara")
    view.draw_graph_in_figure
