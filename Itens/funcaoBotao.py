
import flet as ft

class FuncaoBotao(ft.UserControl):
    
    def __init__(self, id, função):
        self.id = id
        self.funcao = função

    def on_click(self):
        print(self.id)
        #self.funcao(self.id)
        
        