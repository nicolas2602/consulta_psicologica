import flet as ft
class Mostra(ft.UserControl):

    def __init__(self,id_cadastro = None):
        self.__id = id_cadastro

    def editar(self,e):
        print(f"Editar o id:{self.__id}")


    def deletar(self,e):
        print(f"Deletar o id:{self.__id}")