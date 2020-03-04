from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.bd.parametros import Parametros
from src.consulta import Consulta
from src.tratamento import TratamentoVoos
from src.bd.script import Script
from src.telegram.comunicacao import Comunicacao
from src.graylog import *


def pesquisa_voo():
    sql = Script()
    paramentos = Parametros()
    paramento = paramentos.retorna_parametros()
    comunicacao = Comunicacao()

    options = Options()
    options.headless = False

    if int(paramento['navegador_handler']):
        options.headless = True

    driver = webdriver.Chrome(chrome_options=options)
    driver.maximize_window()

    destinos = sql.consulta_destinos()
    for destino in destinos:
        try:
            driver.get(paramento['site'])
            driver.delete_all_cookies()
            driver.refresh()
            consulta_ida = Consulta(driver)
            consulta_ida.informo_origem()
            consulta_ida.pesquisa_voo(destino['origem'])
            consulta_ida.pesquisa_voo(destino['destino'])
            consulta_ida.pesquisar()
            lista_voos = consulta_ida.pega_dados_voo()

            if lista_voos is None:
                continue

            tratar_voos = TratamentoVoos()
            dados_voos = tratar_voos.cria_json(lista_voos, destino['origem'], destino['destino'])

            comunicacao.alerta_voos(paramento['valor_voo'], dados_voos)

            for voo in dados_voos['lista_voos']:
                sql.insere_voo(dados_voos, voo)

        except Exception as exception:
            try:
                img = None
                img = driver.get_screenshot_as_base64()
            except Exception:
                pass
            logger.exception(exception, img)
            # sql.insere_log(exception, img)

    driver.quit()

pesquisa_voo()