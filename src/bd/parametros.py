from src.bd.script import Script
from src.graylog import *

class Parametros(object):

    def __init__(self):
        self.sql = Script()

    def retorna_parametros(self):
        try:
            parametros = self.sql.consulta_parametros()
            resultado = {}

            for parametro in parametros:
                resultado[parametro['tipo_parametro']] = parametro['valor']

            return resultado

        except Exception as exception:
            logger.exception(exception)
            self.sql.insere_log(exception)
            return
