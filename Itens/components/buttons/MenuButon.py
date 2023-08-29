import flet as ft

class MenuButon(ft.UserControl):
    '''Botão Estilizado e dedicado para o Menu principal do projeto.'''
    
    def __init__(self, nome = None, icone = None, funcao = None):

        self.__desiner = ft.OutlinedButton(

                #### Modificando o estilo visual do botão ####
                style= ft.ButtonStyle(
                    color= {
                        ft.MaterialState.DEFAULT: ft.colors.BLACK,
                    },
                    bgcolor= {
                        ft.MaterialState.DEFAULT: ft.colors.GREEN_200,
                        ft.MaterialState.HOVERED: ft.colors.GREEN_400,
                    },
                    shape= ft.RoundedRectangleBorder(radius = 10)
                ),

                #### Itens do Botão ####
                content=ft.Container(
                    content=ft.Column( 
                        [    
                            ft.Icon(name = icone,),
                            ft.Text(value= nome,),
                        ],
                        spacing=0,
                        alignment= ft.MainAxisAlignment.START,
                        horizontal_alignment= ft.CrossAxisAlignment.CENTER,   
                        
                    ),
                    padding=ft.padding.all(2),
                    width=110,
                ),
                on_click= funcao,
            )
        
    def build(self):
        return self.__desiner