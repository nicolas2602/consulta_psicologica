import requests
import logging
from Itens.components.MSGBanner import MSGBanner
import flet as ft

class Log:
    def __init__(self,page):
        self.page = page

        self.time = '4SI_GBD_02'
        self.senha = '3bEJxoN8SC'
        self.banco_de_dados = 'consulta_psicologica'
        self.tabela = ''
        self.chave_primaria = 0
        self.crud = ''
        self.usuario = ''

    def _insertCmd(self):
        response_statement = 'insert/{your_team, your_password, your_dbname, your_table, your_table_pk, crud, your_username}'
        response_statement = response_statement + f'?&your_team={self.time}'
        response_statement = response_statement + f'&your_password={self.senha}'
        response_statement = response_statement + f'&your_dbname={self.banco_de_dados}'
        response_statement = response_statement + f'&your_table={self.tabela}'
        response_statement = response_statement + f'&your_table_pk={self.chave_primaria}'
        response_statement = response_statement + f'&crud={self.crud}'
        response_statement = response_statement + f'&your_username={self.usuario}'

        insert_cmd = response_statement

        return insert_cmd
    
    def _postRequest(self):

        logging.basicConfig(format='%(levelname)s:%(message)s @ %(asctime)s', level=logging.DEBUG)
        obj = MSGBanner(self.page)
        
        try:
            response = requests.post('http://54.235.63.166:8000/'+self._insertCmd())

            if response.status_code != 200:
                logging.error(f"Resposta={response.__dict__}")
                obj.setMsg("ERRO - Não foi possivel enviar o dados!",ft.colors.RED_300)
                obj.show_banner()
            else:
                logging.info(f"Content={response.content}")
                obj.setMsg("Dados enviados com Sucesso!!!",ft.colors.GREEN_400)
                obj.show_banner()
                
        except requests.exceptions.RequestException as erro_conexao:
            logging.critical("Error no logging! Tente novamente...")
            obj.setMsg("ERRO - Não foi possivel conectar com a AWS!",ft.colors.RED_300)
            obj.show_banner()
    
    def submit(self, table, pk, crud, user):
        obj = MSGBanner(self.page)
        obj.setMsg("Enviando para a AWS...",ft.colors.BLUE_200)

        obj.show_banner()
        self.tabela = table
        self.chave_primaria = pk
        self.crud = crud
        self.usuario = user
        
        self._postRequest()