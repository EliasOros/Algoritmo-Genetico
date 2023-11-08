from Model.ModelPrincipal import ModelPrincipal
from View.ViewPrincipal import ViewPrincipal


class ControllerPrincipal:
    
    def __init__(self, modelPrincipal, view_principal):
        self.model = modelPrincipal
        self.view_principal = view_principal

    def iniciar(self):
        self.view_principal.iniciar()

if __name__ == "__main__":
    model = ModelPrincipal()
    view_principal = ViewPrincipal()
    controller = ControllerPrincipal(model, view_principal)
    controller.iniciar()



