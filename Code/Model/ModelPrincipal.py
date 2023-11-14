import pandas as pd

class ModelPrincipal:
    
    ciudades = [
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
    
    distancias_min = []
    distancias_max = []
    distancia_final_min=""
    distancia_final_max=""
    
    ciudades_min = ciudades.copy()
    ciudades_max = ciudades.copy()
    
    mensaje_min=""
    mensaje_max=""
    
    def obtencionDistancias(self,ciudad_origen_min,df_min,ciudad_origen_max,df_max):      
               
        if(len(self.ciudades_min)!=1 and len(self.ciudades_max)!=1):
                       
            ciudades_cercanas = df_min[ciudad_origen_min][df_min[ciudad_origen_min]>0].idxmin()
            ciudades_lejanas = df_max[ciudad_origen_max][df_max[ciudad_origen_max]>0].idxmax()
            
            distancia_AB_min = df_min.loc[ciudad_origen_min, ciudades_cercanas]
            distancia_AB_max = df_max.loc[ciudad_origen_max, ciudades_lejanas]
            
            self.mensaje_min += (f"La ciudad mas cercana de  {ciudad_origen_min} es {ciudades_cercanas} con {distancia_AB_min} Km de distancia\n\n")
            self.mensaje_max +=(f"La ciudad mas lejana de  {ciudad_origen_max} es {ciudades_lejanas} con {distancia_AB_max} Km de distancia\n\n")
            
            self.ciudades_min.remove(ciudad_origen_min)
            self.ciudades_max.remove(ciudad_origen_max)
            
            self.ruta_min.append(ciudad_origen_min)
            self.ruta_max.append(ciudad_origen_max)
            
            self.distancias_min.append(distancia_AB_min)
            self.distancias_max.append(distancia_AB_max)
            
            df_min = df_min.drop(ciudad_origen_min,axis='index')
            df_max= df_max.drop(ciudad_origen_max,axis='index')
            
            self.obtencionDistancias(ciudades_cercanas,df_min,ciudades_lejanas,df_max)
            
            self.distancia_final_min = (df_min.loc[self.ruta_min[-1],ciudad_origen_min])
            self.distancia_final_max = (df_max.loc[self.ruta_max[-1],ciudad_origen_max])
            
            
            
        else:
            
            self.ruta_min.append(ciudad_origen_min)
            self.ruta_max.append(ciudad_origen_max)
            
       
    def reiniciar(self):
        
        self.ciudades_min = self.ciudades.copy()
        self.ciudades_max = self.ciudades.copy()
        

        self.ruta_min = []
        self.ruta_max = []
        
        self.distancias_min = []
        self.distancias_max = []
        self.distancia_final_min=""
        self.distancia_final_max=""
        
        self.mensaje_min=""
        self.mensaje_max=""
        
        self.dis_min = []
        self.dis_max = []
        
    
        
    def iniciar(self,eleccion):
        
        df_min = pd.read_excel('code/Others/Distances.xlsx', header=0, index_col=0)
        df_max = pd.read_excel('code/Others/Distances.xlsx', header=0, index_col=0)
        
        self.obtencionDistancias(eleccion ,df_min,eleccion,df_max)
        
        self.mensaje_min += (f"De la ultima ciudad que es {self.ruta_min[-1]} nos regresamos a la ciudad de partida que es {eleccion} con {self.distancia_final_min} Km de distancia\n\n")
        self.mensaje_max +=(f"De la ultima ciudad que es  {self.ruta_max[-1]} nos regresamos a la ciudad de partida que es {eleccion} con {self.distancia_final_max} Km de distancia\n\n")
        
        self.dis_min = self.distancias_min.copy()
        self.dis_max = self.distancias_max.copy()
        
        self.dis_min.append(self.distancia_final_min)
        self.dis_max.append(self.distancia_final_max)
        
        self.mensaje_min +=(f"La distancia total es: {sum(self.dis_min)}")
        self.mensaje_max +=(f"La distancia total es: {sum(self.dis_max)}")
        
        
        
