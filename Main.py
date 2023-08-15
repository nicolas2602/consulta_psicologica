from Formulario import Formulario
from Botao_Menu import *
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


    form = Formulario()

    
    #---- Funções de Cada botão ----
    def click1(e):
        print('Cadastro')
        if (len(janela.controls) > 2):
            janela.controls.pop(2)
            janela.controls.append(form.get_desiner(e))

        else:
            janela.controls.append(form.get_desiner(e))
        page.update()
        

    def click2(e):
        print('Agendamento')
        if (len(janela.controls) > 2):
            janela.controls.pop(2)
            janela.controls.append(ft.Column(controls=[ft.Text('Agendamento',color='#000000')]))
        
        else:
            janela.controls.append(ft.Column(controls=[ft.Text('Agendamento',color='#000000')]))

        page.update()

    
    def click3(e):
        print('Anotações')
        if (len(janela.controls) > 2):
            janela.controls.pop(2)
            janela.controls.append(ft.Column(controls=[ft.Text('Anotações',color='#000000')]))
        
        else:
            janela.controls.append(ft.Column(controls=[ft.Text('Anotações',color='#000000')]))

        page.update()

    def click4(e):
        print('Pagamento')
        if (len(janela.controls) > 2):
            janela.controls.pop(2)
            janela.controls.append(ft.Column(controls=[ft.Text('Pagamento',color='#000000')]))
        
        else:
            janela.controls.append(ft.Column(controls=[ft.Text('Pagamento',color='#000000')]))

        page.update()

    #---- Criação dos botões----
    botao1 = menu_botao(config_botao['txt_botao1'],config_botao['icone_cadasto'],click1)
    botao2 = menu_botao(config_botao['txt_botao2'],config_botao['icone_agenda'],click2)
    botao3 = menu_botao(config_botao['txt_botao3'],config_botao['icone_anotacoes'],click3)
    botao4 = menu_botao(config_botao['txt_botao4'],config_botao['icone_pagamento'],click4)


    # ---- Posicionamento dos itens da janela ----
    janela = ft.Row(
            controls=[
                #----menu----
                ft.Column(
                    [   
                        botao1,
                        botao2,
                        botao3,
                        botao4,
                        
                    ],              
                ),

                ft.VerticalDivider(color=ft.colors.GREEN_900),
                
                #---- body ----

             ],
             expand=True,
        )
    
    #print(janela.controls[2].controls)
    page.add(janela)

ft.app(target=main)