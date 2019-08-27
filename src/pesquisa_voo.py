from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.bd.parametros import Parametros
from src.consulta import Consulta
from src.tratamento import TratamentoVoos
from src.bd.script import Script
from src.telegram.comunicacao import Comunicacao


def pesquisa_voo():
    sql = Script()
    paramentos = Parametros()
    paramento = paramentos.retorna_parametros()

    options = Options()
    options.headless = True
    driver = webdriver.Chrome(
        # chrome_options=options
    )

    driver.maximize_window()

    qnt_destinos = 0
    qnt_erros = 0

    voos = []

    destinos = sql.consulta_destinos()
    for destino in destinos:
        try:
            driver.get(paramento['site'])
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
            voos.append(dados_voos)
            qnt_destinos += 1

        except Exception as exception:
            qnt_erros += 1
            img = driver.get_screenshot_as_base64()
            sql.insere_log(exception.msg, img)

        if qnt_erros > 3:
            break

    try:
        comunicacao = Comunicacao()
        for voo in voos:
            comunicacao.alerta_voos(paramento['valor_voo'], voo)
            for v in voo['lista_voos']:
                sql.insere_voo(voo, v)

    except Exception as exception:
        img = driver.get_screenshot_as_base64()
        sql.insere_log(exception, img)

    driver.quit()
