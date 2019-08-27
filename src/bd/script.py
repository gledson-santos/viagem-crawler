from src.bd.conect_bd import ConectBd
from datetime import datetime


class Script(object):

    def __init__(self):
        self.conexao = ConectBd()

    def insere_voo(self, dados_trecho, dados_voo):
        sql = 'insert into voos (origem, destino, dia_semana, data, valor, data_consulta) values ("{}", "{}", "{}", "{}", {}, "{}")'.format(dados_trecho['origem'], dados_trecho['destino'], dados_voo['dia_semana'], dados_voo['data'], dados_voo['valor'], dados_trecho['data_hora'])
        return self.conexao.executa(sql)

    def insere_log(self, msg, foto = None):
        data = datetime.now().strftime("%d-%m-%y %h:%m")
        msg = msg.replace('"', '')
        sql = 'insert into log (mensagem_erro, imagem, data_consulta) values ("{}", "{}", "{}")'.format(msg, foto, data)
        return self.conexao.executa(sql)

    def consulta_parametros(self):
        sql = 'select * from parametros'
        return self.conexao.busca(sql)

    def consulta_destinos(self):
        sql = 'select * from destinos where status="ativo";'
        return self.conexao.busca(sql)

    def atualiza_valor_voos(self, valor):
        sql = 'update parametros set valor={} where tipo_parametro="valor_voo";'.format(valor)
        return self.conexao.executa(sql)

    def consulta_menor_valor_passagem(self):
        data = datetime.now().strftime("%d-%m-%y")
        sql = 'SELECT MIN(valor) AS valor FROM voos WHERE data_consulta >= {}'.format(data)
        return self.conexao.busca(sql)