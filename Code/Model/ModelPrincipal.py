import pandas as pd

class ModelPrincipal:
    
    ciudades_min = [
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
    
    
    ciudades_max = [
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
    

    ruta_min = []
    ruta_max = []
    
    
    def obtenerMin(self,origen,df):
               
        if(len(self.ciudades_min)!=1):
            ciudad_origen = origen
            ciudades_cercanas = df[ciudad_origen][(df[ciudad_origen] > 0)].idxmin()
            print(f"La ciudad más cercana a {ciudad_origen} es {ciudades_cercanas}.")
            self.ciudades_min.remove(ciudad_origen)
            self.ruta_min.append(ciudad_origen)
          
            df = df.drop(ciudad_origen,axis='index')

            a = self.obtenerMin(ciudades_cercanas,df)
            return a
        else:
            self.ruta_min.append(origen)

            return origen
        
    def obtenerMax(self,origen,df):
        
        if(len(self.ciudades_max)!=1):
            ciudad_origen = origen
            ciudades_cercanas = df[ciudad_origen][(df[ciudad_origen] > 0)].idxmax()
            print(f"La ciudad más lejana a {ciudad_origen} es {ciudades_cercanas}.")
            
                    
            self.ciudades_max.remove(ciudad_origen)
            self.ruta_max.append(ciudad_origen)
                    
            df = df.drop(ciudad_origen,axis='index')
            
            a = self.obtenerMax(ciudades_cercanas,df)
            return a
        else:
            self.ruta_max.append(origen)

            return origen
    def minimo(self, origen):
        # Cargar los datos desde el archivo Excel
        df = pd.read_excel('code/Others/Distances.xlsx', header=0, index_col=0)
        ciudad_final = self.obtenerMin(origen,df)
        print(ciudad_final)
        print("ruta minimo",self.ruta_min)
        
        return self.ruta_min
        

    def maximo(self, origen):
        # Cargar los datos desde el archivo Excel
        df = pd.read_excel('code/Others/Distances.xlsx', header=0, index_col=0)
        ciudad_final = self.obtenerMax(origen,df)
        print(ciudad_final)
        print("ruta maximo",self.ruta_max)
        
        return self.ruta_max
        
