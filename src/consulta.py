from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from src.bd.script import Script
from time import sleep

class Consulta(object):

    def __init__(self, driver):
        self.driver = driver
        self.campo_origem = '//div[@class="purchase-box-header-division division-input division-input-origin"]/div/a/div'
        self.campo_destino = '//div[@class="input-destiny division-input-destiny-city active"]/div/a/span'
        self.botao_ida = '//fieldset/div[2]/label[@for="goOrBack"]'
        self.botao_compra = 'btn-box-buy'
        self.lista_voos = "//ul[@class='listDates']/li"
        self.botao_proxima_semana = "ControlGroupSelect2View_AvailabilityInputSelect2View_LinkButtonNextWeek1"
        self.sql = Script()

    def informo_origem(self):
        self.driver.find_element_by_xpath(self.campo_origem).click()

    def informo_destino(self):
        self.driver.find_element_by_xpath(self.campo_destino).click()

    def pesquisa_voo(self, destino):
        actions = ActionChains(self.driver)
        actions.send_keys(destino)
        actions.key_down(Keys.ENTER)
        actions.key_up(Keys.ENTER)
        actions.perform()

    def pesquisar(self):
        self.driver.find_element_by_xpath(self.botao_ida).click()
        self.driver.find_element_by_id(self.botao_compra).click()

        # wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.element_to_be_clickable((By.XPATH, self.botao_proxima_semana)))
        #@TODO: Implementar o wait com base nesse id ""

    def pega_dados_voo(self, qnt_semana = 1):
        try:
            datas = []
            pesquisar = 0

            while pesquisar < qnt_semana:
                voos = self.driver.find_elements_by_xpath(self.lista_voos)

                for voo in voos:
                    datas.append(voo.text)
                try:
                    self.driver.find_element_by_id(self.botao_proxima_semana).click()
                except Exception as exception:
                    self.driver.find_element_by_id(self.botao_proxima_semana).click()
                    self.sql.insere_log(exception.msg)

                pesquisar += 1

            return datas
        except Exception as exception:
            self.sql.insere_log(exception.msg)



