import flet as ft 

class PopUp(ft.UserControl):
    '''Barra Estilizada dedicada para infomar uma mensage para o usuario.'''

    def __init__(self, msg = None, cor = ft.colors.GREY_700):

        self.msg = msg
        self.cor = cor

        self.desiner = ft.SnackBar(content=ft.Text(self.msg),bgcolor= self.cor,)

    def build(self):
        return self.desiner
    
    def setPopUp(self, msg, cor):
        self.msg = msg
        self.cor = cor
        