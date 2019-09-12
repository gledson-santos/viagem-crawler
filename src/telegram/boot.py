# -*- Coding: UTF-8 -*-
#coding: utf-8

import telebot
from src.bd.script import Script
from src.bd.parametros import Parametros

try:
    parametros = Parametros()
    parametro = parametros.retorna_parametros()
    bot = telebot.TeleBot(parametro['bot_token_telegram'])

    def consulta_menor_valor_voo(message):
        try:
            sql = Script()
            resultado = sql.consulta_menor_valor_passagem()
            valor = round(resultado[0]['valor'], 2)
            return 'O menor valor encontrado é de R$ {}'.format(valor)
        except Exception as e:
            return 'Não há valor válido para a consulta solicitada'


    @bot.message_handler(commands=['menorvalor'], func=consulta_menor_valor_voo)
    def menor_valor_passagens(message):
        bot.reply_to(message, consulta_menor_valor_voo(message))


    def altera_valor_pesquisa(message):
        try:
            valor = int(message.text.replace('/altera', ''))
            sql = Script()
            sql.atualiza_valor_voos(valor)
            return 'Valor da busca pelo preço das passagens foi alterado para R$ {}'.format(valor)

        except Exception as e:
            return 'Informe um valor válido. \nEx.: /altera 250 \nPara alterar o valor do monitoramento das passagens para R$250'


    @bot.message_handler(commands=['altera'], func=altera_valor_pesquisa)
    def echo_all(message):
        bot.reply_to(message, altera_valor_pesquisa(message))


    def consulta_log(message):
        sql = Script()
        ultima_consulta = sql.consulta_data_ultima_verificacao()[0]['data_consulta']
        quantidade_erros = sql.consulta_quantidade_erros()[0]['qnt']
        msg = 'A última consulta aconteceu: {}'.format(ultima_consulta)
        msg += '\n'
        msg += 'A quantidade de erros encontrados até agora foram {} erros'.format(quantidade_erros)
        return msg


    @bot.message_handler(commands=['log'], func=consulta_log)
    def echo_all(message):
        bot.reply_to(message, consulta_log(message))


    def consulta_parametros(message):
        sql = Script()
        paramentros = sql.consulta_paramentros()
        for valores in paramentros:
            parametro[valores['tipo_parametro']] = valores['valor']

        msg = 'Os seguintes parametros estão sendo utilizados:\n\n'
        msg += 'O site consultado é: {}\n'.format(parametro['site'])
        msg += 'O valor da passagem para pesquisa é: {}\n'.format(parametro['valor_voo'])
        msg += 'A quantidade de semanas que estamos analisando é: {}\n'.format(parametro['qnt_semanas'])
        msg += 'O navegar está no modo: {}\n'.format('Não Renderizado' if parametro['qnt_semanas'] == '1' else 'Renderizado')
        return msg


    @bot.message_handler(commands=['parametros'], func=consulta_parametros)
    def echo_all(message):
        bot.reply_to(message, consulta_parametros(message))


    def comandos(message):
        msg = 'Você pode utilizar os seguintes comandos para configurar suas buscas: \n\n'
        msg += '/menorvalor - Esse comando retorna o valor mais baixo da passagem que foi encontrado nas buscas\n\n'
        msg += '/altera "valor" - Esse comando altera o valor da passagem que você deseja ser notificado. \n Ex.: Utilizando /altera 200. Quando encontrarmos alguma passagem abaixo de R$ 200,00, iremos notificá-lo por mensagem\n\n'
        msg += '/log - Esse comando retorna o log do sistema com as informações da última vez que o sistema rodou, e a quantidade de erros gerados até o momento.\n\n'
        msg += '/parametros - Esse comando retorna os paramentros que estão sendo utilizandos nas consultas atuais\n\n'
        return msg


    @bot.message_handler(commands=['help'], func=comandos)
    def echo_all(message):
        bot.reply_to(message, comandos(message))


    bot.polling()

except Exception as exception:
    sql = Script()
    sql.insere_log(exception)
