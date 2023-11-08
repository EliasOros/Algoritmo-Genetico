from Model.ModelPrincipal import ModelPrincipal
from View.ViewPrincipal import ViewPrincipal
import threading
class ControllerPrincipal:
    ciudad_elegida = ""

    def __init__(self, modelPrincipal, view_principal):
        self.model = modelPrincipal
        self.view_principal = view_principal

        self.thread1 = None
        self.thread2 = None
        print("hola")

    def iniciar(self):
        self.view_principal.iniciar()

    def realizarAccion(self):
        eleccion = self.ciudadElegida = self.view_principal.obtenerCiudad()

        # Detener los hilos anteriores si existen
        if self.thread1 and self.thread1.is_alive():
            self.thread1.join()
        if self.thread2 and self.thread2.is_alive():
            self.thread2.join()

        # Crear nuevos hilos
        self.thread1 = threading.Thread(target=self.minimo, args=(eleccion,))
        self.thread2 = threading.Thread(target=self.maximo, args=(eleccion,))

        self.thread1.start()
        self.thread2.start()

    def minimo(self, eleccion):
        ruta = self.model.minimo(eleccion)

        for i in range(len(ruta) - 1):
            self.view_principal.generate_lines_min(ruta[i], ruta[i + 1])

    def maximo(self, eleccion):
        ruta = self.model.maximo(eleccion)

        for i in range(len(ruta) - 1):
            self.view_principal.generate_lines_max(ruta[i], ruta[i + 1])

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
        self.view_principal.reiniciar()

if __name__ == "__main__":
    model = ModelPrincipal()
    controller = ControllerPrincipal(model, None)  # None en lugar de view_principal
    view_principal = ViewPrincipal(controller)  # Pasa la instancia de ControllerPrincipal
    controller.view_principal = view_principal  # Asigna la instancia de view_principal a controller
    controller.iniciar()