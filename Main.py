from Botao import *
from Cadastro import *
import flet as ft

# ----Variaver-----

config_page={
    'color': ft.colors.BROWN_50,
    'width': 800,
    'height':600,
    'min_height': 600,
    'min_width':800,
    'title': "PsicoTeck"
}
config_div = {'color': ft.colors.GREEN_800}


# ----main----

def main(page: ft.Page):

    # Configuração da pagina
    page.bgcolor = config_page['color']
    page.window_height = config_page['height']
    page.window_width = config_page['width']
    page.window_min_height = config_page['min_height']
    page.window_min_width = config_page['min_width']
    page.title = config_page['title']

    #---- Funções de Cada botão ----
    def click1(e):
        print('Cadastro')
        janela.controls[2].controls = cadastro(),
        page.update()
        

    def click2(e):
        print('Agendamento')
        janela.controls[2].controls = ft.Text('Agendamento',color='#000000'),
        page.update()

    
    def click3(e):
        print('Anotações')
        janela.controls[2].controls = ft.Text('Anotações',color='#000000'),
        page.update()

    #---- Criação dos botões----
    botao1 = menu_botao(config_botao['txt_botao1'],config_botao['icone_cadasto'],click1)
    botao2 = menu_botao(config_botao['txt_botao2'],config_botao['icone_agenda'],click2)
    botao3 = menu_botao(config_botao['txt_botao3'],config_botao['icone_anotacoes'],click3)


    # ---- Posicionamento dos itens da janela ----
    janela = ft.Row(
            controls=[
                #----menu----
                ft.Column(
                    [   
                        botao1,
                        botao2,
                        botao3,
                        
                    ],              
                ),

                ft.VerticalDivider(color=ft.colors.GREEN_900),
                
                #---- body ----
                ft.Column(controls=[ ft.Text("Body!",color="#000000")], alignment=ft.MainAxisAlignment.START, expand=True),
            ],
            expand=True,
        )
    
    #print(janela.controls[2].controls)
    page.add(janela)

ft.app(target=main)