from bd_pagamento.pagamento import pesquisarStatusPagamento,updateStatus
from datetime import datetime, timedelta
from time import sleep

class AtualizarPagamento:
    '''Atualiza os dados das guia em andamento Atrasadas para o status Pendente'''
    def __init__(self):
    
        self.time = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')

        self.listaPg = pesquisarStatusPagamento('Em andamento', self.time)

    def atualizar(self):
        for dados in self.listaPg:
            updateStatus(dados[0],3)
            sleep(0.2)
