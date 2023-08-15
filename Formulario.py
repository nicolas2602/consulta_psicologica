import flet as ft

config_form = {
    'color': ft.colors.BLACK,
    'bg': ft.colors.GREEN_700

}


class Formulario(ft.UserControl):
    def __init__(self):
        self.__nome = ''
        self.__email = ''
        self.__telefone = ''

        self.__form1 = ft.TextField(label="Nome",value='', color= config_form['color'],)
        self.__form2 = ft.TextField(label="E-mail",value='', color= config_form['color'],)
        self.__form3 = ft.TextField(label="Telefone",value='', color= config_form['color'],)
        self.__bSubmit = ft.ElevatedButton(text="Submit", on_click= self.set_value)

        self.__desiner = ft.Column(controls=[
            self.__form1,
            self.__form2,
            self.__form3,
            self.__bSubmit,
        ])

    def set_value(self,e):
        self.__nome = self.__form1.value
        self.__email = self.__form2.value
        self.__telefone = self.__form3.value 
        print(self.__nome)
        print(self.__email)
        print(self.__telefone)

    def get_value(self,e):
        return {
            'nome': self.__nome,
            'email': self.__email,
            'telefone':self.__telefone,
        }
    
    def get_desiner(self,e):
        return self.__desiner