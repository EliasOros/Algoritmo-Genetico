import pandas as pd

# Cargar los datos desde el archivo Excel
df = pd.read_excel('Others/ejemplo.xlsx', header=1, index_col=1)

# Mostrar las distancias entre dos ciudades
distancia_AB = df.loc['Ciudad A', 'Ciudad B']
print(f"Distancia entre Ciudad A y Ciudad B: {distancia_AB} km")

# Encontrar la ciudad más cercana a una ciudad específica
ciudad_origen = 'Ciudad A'
ciudades_cercanas = df[ciudad_origen].idxmin()
print(f"La ciudad más cercana a {ciudad_origen} es {ciudades_cercanas}.")

# Calcular la distancia promedio a todas las ciudades
distancia_promedio = df.mean().mean()
print(f"Distancia promedio entre todas las ciudades: {distancia_promedio} km")
