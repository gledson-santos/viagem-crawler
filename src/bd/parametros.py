from src.bd.script import Script


class Parametros(object):

    def __init__(self):
        self.sql = Script()

    def retorna_parametros(self):
        parametros = self.sql.consulta_parametros()
        resultado = {}

        for parametro in parametros:
            if parametro['tipo_parametro'] == 'site':
                resultado['site'] = parametro['valor']
            elif parametro['tipo_parametro'] == 'valor_voo':
                resultado['valor_voo'] = parametro['valor']
            elif parametro['tipo_parametro'] == 'bot_token_telegram':
                resultado['bot_token_telegram'] = parametro['valor']

        return resultado
