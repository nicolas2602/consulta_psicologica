import flet as ft

config_botao={
    'color': ft.colors.GREEN_800,
    'bgcolor_hover':ft.colors.GREEN_200,
    'width_botao': 110,

    # txt/icon
    'icone_cadasto': ft.icons.PERSON,
    'icone_agenda': ft.icons.CALENDAR_MONTH,
    'icone_anotacoes': ft.icons.EVENT_NOTE,
    'txt_botao1': 'Cadastro',
    'txt_botao2': 'Agendamentos',
    'txt_botao3': 'Anotações',
}


def menu_botao(txt,icone,funcao):
    '''txt é o texto que aparecerá no botão,
        icone é o ico que aparecerá no botão, 
        funcao é a função que será chamada ao clicar no botão.
    '''
    b = ft.Container(
            ft.OutlinedButton(
            style= ft.ButtonStyle(
                color= {
                    ft.MaterialState.DEFAULT: config_botao['color'],
                },
                bgcolor= {
                    ft.MaterialState.HOVERED: config_botao['bgcolor_hover'],

                },
                
            ),

            content=ft.Container(
                content=ft.Column( 
                    [    
                        ft.Icon(name = icone,),
                        ft.Text(value= txt,),
                    ],
                    spacing=0,
                    alignment= ft.MainAxisAlignment.START,
                    horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                
                    
                    
                ),
                padding=ft.padding.all(2),
                width=config_botao['width_botao'],
            ),
            on_click= funcao,
        ),
    )
    return b