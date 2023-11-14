from Model.ModelPrincipal import ModelPrincipal
from View.ViewPrincipal import ViewPrincipal


class ControllerPrincipal:
    

    def __init__(self, modelPrincipal, view_principal):
        self.model = modelPrincipal
        self.view_principal = view_principal
        
        
    def iniciar(self):
        self.view_principal.iniciar()

    def realizarAccion(self):
        self.reiniciar()
        
        eleccion,opcion = self.view_principal.obtenerCiudad()
        
        
        if opcion == "Corto":
            
            self.model.iniciar(eleccion)
            
            distancia = self.model.distancias_min
            
            ruta = self.model.ruta_min
            
            for i in range(len(ruta) - 1):
                
                self.view_principal.generate_lines(ruta[i], ruta[i + 1],distancia[i])
                
            distancia_final = self.model.distancia_final_min
            
            
            self.view_principal.generate_lines(ruta[len(ruta)-1],ruta[0],distancia_final)
            
            print (self.model.mensaje_min )
            self.view_principal.imprimir_en_scroll(self.model.mensaje_min)
            
            print (self.model.distancias_min)
            
        if opcion == "Largo":
        
            self.model.iniciar(eleccion)
            
            distancia = self.model.distancias_max
            
            ruta = self.model.ruta_max
            
            for i in range(len(ruta) - 1):
                
                self.view_principal.generate_lines(ruta[i], ruta[i + 1],distancia[i])
                
            distancia_final = self.model.distancia_final_max
            
            self.view_principal.generate_lines(ruta[len(ruta)-1],ruta[0],distancia_final)
            
            print (self.model.mensaje_max)
            self.view_principal.imprimir_en_scroll(self.model.mensaje_max)
        

    def reiniciar(self):
        self.model.reiniciar()
        self.view_principal.reiniciar()

if __name__ == "__main__":
    model = ModelPrincipal()
    controller = ControllerPrincipal(model, None)  # None en lugar de view_principal
    view_principal = ViewPrincipal(controller)  # Pasa la instancia de ControllerPrincipal
    controller.view_principal = view_principal  # Asigna la instancia de view_principal a controller
    controller.iniciar()