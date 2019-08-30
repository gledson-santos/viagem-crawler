from src.bd.script import Script


class Parametros(object):

    def __init__(self):
        self.sql = Script()

    def retorna_parametros(self):
        try:
            parametros = self.sql.consulta_parametros()
            resultado = {}

            for parametro in parametros:
                if parametro['tipo_parametro'] == 'site':
                    resultado['site'] = parametro['valor']

                elif parametro['tipo_parametro'] == 'valor_voo':
                    resultado['valor_voo'] = parametro['valor']

                elif parametro['tipo_parametro'] == 'bot_token_telegram':
                    resultado['bot_token_telegram'] = parametro['valor']

                elif parametro['tipo_parametro'] == 'qnt_semanas':
                    resultado['qnt_semanas'] = parametro['valor']

                elif parametro['tipo_parametro'] == 'navegador_handler':
                    resultado['navegador_handler'] = parametro['valor']

            return resultado

        except Exception as exception:
            self.sql.insere_log(exception)
            return
