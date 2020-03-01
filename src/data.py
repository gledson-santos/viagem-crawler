from datetime import datetime, timedelta
from src.graylog import logger


class Data(object):

    def __init__(self, driver):
        self.driver = driver

    def seleciona_mes(self, mes):
        try:
            elemento = 'datepickerGo'

            calendario = self.driver.find_element_by_id(elemento)
            calendario.click()

            dados_calendario  = self.driver.find_element_by_id('ui-datepicker-div')

            while True:
                bloco = 0
                meses = dados_calendario.find_elements_by_xpath('//div[@class="ui-datepicker-title"]')
                for _mes in meses:
                    if mes in _mes.text:
                        bloco += 1
                        return bloco
                    bloco += 1

                avancar = self.driver.find_element_by_xpath('//a[@title="Próximo"]')
                avancar.click()

            return bloco

        except Exception as exception:
            img = self.driver.get_screenshot_as_base64()
            logger.exception(img)

    def seleciona_dia(self, dia, bloco):
        try:
            bloco_mes = self.driver.find_element_by_xpath('//div[@id="ui-datepicker-div"]/div[{}]'.format(bloco))

            lista_semanas = bloco_mes.find_element_by_xpath('table/tbody')
            semanas = lista_semanas.find_elements_by_tag_name('tr')

            for semana in semanas:
                dias = semana.find_elements_by_tag_name('td')
                for _dia in dias:
                    if str(dia) == _dia.text:
                        _dia.click()
                        return 'OK'

        except Exception as exception:
            img = self.driver.get_screenshot_as_base64()
            logger.exception(img)

    def converte_data_consulta(self, dia):
        try:
            dia = datetime.strptime(dia, '%d/%m/%Y').date()
            dia = dia - timedelta(days=7)
            if dia < datetime.now().date():
                dia = datetime.now().date()

            return dia

        except Exception as exception:
            img = self.driver.get_screenshot_as_base64()
            logger.exception(img)

    def retorna_nome_mes(self, mes):
        try:
            Meses = ('Sem Mês', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
            return Meses[mes]
        except Exception as exception:
            img = self.driver.get_screenshot_as_base64()
            logger.exception(img)