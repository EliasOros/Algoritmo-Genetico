from Model.ModelPrincipal import ModelPrincipal
from View.ViewPrincipal import ViewPrincipal
import threading

class ControllerPrincipal:
    

    def __init__(self, modelPrincipal, view_principal):
        self.model = modelPrincipal
        self.view_principal = view_principal
        self.ciudad_elegida = ""
        self.thread1 = None
        self.thread2 = None
        

    def iniciar(self):
        self.view_principal.iniciar()

    def realizarAccion(self):
        eleccion = self.ciudadElegida = self.view_principal.obtenerCiudad()

        # Detener los hilos anteriores si existen
        if self.thread1 and self.thread1.is_alive():
            self.thread1.join()
        if self.thread2 and self.thread2.is_alive():
            self.thread2.join()

        thread1 = threading.Thread(target=self.minimo,args=(eleccion,))
        thread2 = threading.Thread(target=self.maximo,args=(eleccion,))
        
        thread1.start()
        thread2.start()

    def minimo(self, eleccion):
        ruta = self.model.minimo(eleccion)
        distancia = self.model.distancias_min 
        
        for i in range(len(ruta) - 1):
            self.view_principal.generate_lines_min(ruta[i], ruta[i + 1],distancia[i])
            
        
        distancia_final = self.model.distancia_final_min
        print (distancia_final)
       
            
        self.view_principal.generate_lines_min(ruta[len(ruta)-1],ruta[0],distancia_final)
       

        

    def maximo(self, eleccion):
        ruta = self.model.maximo(eleccion)
        distancia = self.model.distancias_max

        for i in range(len(ruta) - 1):
            self.view_principal.generate_lines_max(ruta[i], ruta[i + 1],distancia[i])
               
        
        distancia_final = self.model.distancia_final_max
        print (distancia_final)
       
            
        self.view_principal.generate_lines_max(ruta[len(ruta)-1],ruta[0],distancia_final)

    def reiniciar(self):
        self.ciudad_elegida = ""
        self.model.ciudades_min = [
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
        self.model.ciudades_max = [
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
        self.model.ruta_min = []
        self.model.ruta_max = []
        self.model.distancias_min = []
        self.model.distancias_max = []
        self.view_principal.reiniciar()

if __name__ == "__main__":
    model = ModelPrincipal()
    controller = ControllerPrincipal(model, None)  # None en lugar de view_principal
    view_principal = ViewPrincipal(controller)  # Pasa la instancia de ControllerPrincipal
    controller.view_principal = view_principal  # Asigna la instancia de view_principal a controller
    controller.iniciar()