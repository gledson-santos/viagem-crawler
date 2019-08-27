from datetime import datetime


class TratamentoVoos(object):

    def cria_json(self, voos, origem, destino):

        lista_voos = {
            'data_hora': datetime.now().strftime("%d-%m-%Y %H:%M"),
            'origem': origem,
            'destino': destino,
            'lista_voos': []
        }

        for data in voos:
            if 'Indisponível' in data:
                continue

            dados = data.split('\n')

            obj = {
                'dia_semana': dados[0],
                'data': dados[1],
                'valor': float(dados[2].replace('a partir de R$ ', '').replace(',', '').replace('.', ''))/100
            }

            lista_voos['lista_voos'].append(obj)

        return lista_voos
