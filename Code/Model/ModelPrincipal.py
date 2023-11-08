import pandas as pd

class ModelPrincipal:
    
    def __init__(self):
        self.cities = [
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
        
        self.recorrdioCorto = []
        self.recorrdioLargo = []
        
        # Cargar los datos desde el archivo Excel
        self.df = pd.read_excel('Code/Others/Distances.xlsx', header=0, index_col=0)
    
    def hola(self):
        
        # Mostrar las distancias entre dos ciudades
        distancia_AB = self.df.loc['Ciudad A', 'Ciudad B']
        print(f"Distancia entre Ciudad A y Ciudad B: {distancia_AB} km")

        # Encontrar la ciudad más cercana a una ciudad específica
        ciudad_origen = 'Ciudad A'
        ciudades_cercanas = self.df[ciudad_origen][self.df[ciudad_origen] > 0].idxmin()
        print(f"La ciudad más cercana a {ciudad_origen} es {ciudades_cercanas}.")

        # Calcular la distancia promedio a todas las ciudades
        distancia_promedio = self.df.mean().mean()
        print(f"Distancia promedio entre todas las ciudades: {distancia_promedio} km")
        
    def minimo():
        
        print("gola")
