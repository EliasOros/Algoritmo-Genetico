import networkx as nx
import matplotlib.pyplot as plt

# Crea un grafo vacío
G = nx.Graph()

# Agrega nodos que representen ciudades o estados
G.add_node("Ciudad A", pos=(0, 0))
G.add_node("Ciudad B", pos=(2, 1))
G.add_node("Ciudad C", pos=(4, 0))
G.add_node("Ciudad D", pos=(2, -1))

# Conecta los nodos para formar una ruta
G.add_edge("Ciudad A", "Ciudad B")
G.add_edge("Ciudad B", "Ciudad C")
G.add_edge("Ciudad B", "Ciudad D")

# Obtiene las posiciones de los nodos
pos = nx.get_node_attributes(G, 'pos')

# Carga la imagen de fondo
background_image = plt.imread("Others/Images/mexico.png")

# Dibuja el grafo con la imagen de fondo
fig, ax = plt.subplots()
ax.imshow(background_image, extent=[0, 5, -2, 2])  # Ajusta los límites para la imagen de fondo
nx.draw(G, pos, with_labels=False, node_size=0)  # Con with_labels=False, no se mostrarán etiquetas en los nodos

# Muestra el gráfico
plt.axis('off')

# Añade etiquetas como texto en el gráfico
for nodo, (x, y) in pos.items():
    plt.text(x, y, nodo, fontsize=10, ha='center', va='center', color='white')

plt.show()
