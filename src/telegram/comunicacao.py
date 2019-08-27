from src.telegram.integracao import Telegram
from src.bd.script import Script


class Comunicacao(object):

    def __init__(self):
        self.sql = Script()
        self.telegram = Telegram()

    def alerta_voos(self, valor, voos):

        msg = '--- CONSULTA: {} ---'.format(voos['data_hora'])
        msg += '\n'
        msg += '\n'
        msg += 'Os seguintes voos estão dentro do valor esperado de R${}: '.format(valor)
        msg2 = ''
        for voo in voos['lista_voos']:
            if voo['valor'] <= float(valor):
                result = '\n\n ORIGEM: {} \n DESTINO: {} \n VALOR: {} \n DATA: {} \n DIA DA SEMANA: {} \n ####################### \n'.format(voos['origem'], voos['destino'], voo['valor'], voo['data'], voo['dia_semana'])
                msg2 += result
        if msg2:
            msg += msg2
            self.telegram.enviar_msg(msg)
