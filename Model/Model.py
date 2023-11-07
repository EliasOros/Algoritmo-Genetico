import pandas as pd

class Model:
    
    ciudades = cities = [
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
    
    def hola():
                
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
        
    def minimo():
        
        
