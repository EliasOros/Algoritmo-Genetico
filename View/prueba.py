import networkx as nx
import matplotlib.pyplot as plt

# Crea un grafo vacío
G = nx.Graph()

# Agrega nodos que representen ciudades o estados
G.add_node("Ciudad de México", pos=(2.86, -0.815))    
G.add_node("Guadalajara", pos=(2.270, -0.625))   
G.add_node("Ciudad Juarez", pos=(1.700, 1.180))
G.add_node("Tijuana", pos=(0.425,1.430 ))
G.add_node("Zapopan", pos=(2.145, -0.555))      
G.add_node("Monterrey", pos=(2.680,0.235))
G.add_node("Chihuahua", pos=(1.800, 0.720))
G.add_node("Merida", pos=(4.300, -0.440)) 
G.add_node("San Luis Potosi", pos=(2.600, -0.300)) 
G.add_node("Aguascalientes", pos=(2.385, 0.365))
G.add_node("Hermosillo", pos=(1.200, 0.715))
G.add_node("Saltillo", pos=(2.574, 0.100))
G.add_node("Mexicali", pos=(0.650, 1.330))
G.add_node("Culiacan", pos=(1.700, 0.020))
G.add_node("Acapulco de Juarez", pos=(2.710,-1.140))

'''# Conecta los nodos para formar una ruta
G.add_edge("Ciudad A", "Ciudad B")
G.add_edge("Ciudad B", "Ciudad C")
G.add_edge("Ciudad B", "Ciudad D")'''

# Obtiene las posiciones de los nodos
pos = nx.get_node_attributes(G, 'pos')

# Carga la imagen de fondo
background_image = plt.imread("Others/Images/republica.jpg")

# Dibuja el grafo con la imagen de fondo
fig, ax = plt.subplots()
ax.imshow(background_image, extent=[0, 5, -2, 2])  # Ajusta los límites para la imagen de fondo
nx.draw(G, pos, with_labels=False, node_size=0)  # Con with_labels=False, no se mostrarán etiquetas en los nodos

nx.draw(G, pos, with_labels=True, node_color ='blue', node_size = 8, font_size = 5 , font_color = 'black')

# Muestra el gráfico
plt.axis('off')


def generarLineas(ciudadA,ciudadB):
    
    G.add_edge("ciudadA","ciudadB")


generarLineas("Ciudad de México","Zapopan")

'''# Añade etiquetas como texto en el gráfico
for nodo, (x, y) in pos.items():
    plt.text(x, y, nodo, fontsize=10, ha='center', va='center', color='white')'''

plt.show()





# Cargar los datos desde el archivo Excel
df = pd.read_excel('Others/Distances.xlsx', header=0, index_col=0)

# Mostrar las distancias entre dos ciudades
distancia_AB = df.loc['Ciudad A', 'Ciudad B']
print(f"Distancia entre Ciudad A y Ciudad B: {distancia_AB} km")

# Encontrar la ciudad más cercana a una ciudad específica
ciudad_origen = 'Ciudad A'
ciudades_cercanas = df[ciudad_origen][df[ciudad_origen] > 0].idxmin()
print(f"La ciudad más cercana a {ciudad_origen} es {ciudades_cercanas}.")

# Calcular la distancia promedio a todas las ciudades
distancia_promedio = df.mean().mean()
print(f"Distancia promedio entre todas las ciudades: {distancia_promedio} km")