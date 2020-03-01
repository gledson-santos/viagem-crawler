from src.bd.conect_bd import ConectBd


class Script(object):

    def __init__(self):
        self.conexao = ConectBd()

    def insere_voo(self, dados_trecho, dados_voo):
        sql = 'insert into voos (origem, destino, dia_semana, data, valor, data_consulta) values ("{}", "{}", "{}", "{}", {}, "{}")'.format(dados_trecho['origem'], dados_trecho['destino'], dados_voo['dia_semana'], dados_voo['data'], dados_voo['valor'], dados_trecho['data_hora'])
        return self.conexao.executa(sql)

    def consulta_parametros(self):
        sql = 'select * from parametros'
        return self.conexao.busca(sql)

    def consulta_destinos(self):
        sql = 'select * from destinos where status=1;'
        return self.conexao.busca(sql)
