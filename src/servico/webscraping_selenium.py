from selenium.webdriver.chrome.webdriver import WebDriver
from src.servico.iwebscraping_google_maps import IWebScrapingGoogleMaps
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from typing import List, Dict
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebScrapingSeleniun(IWebScrapingGoogleMaps):

    def __init__(self, url: str) -> None:
        self.__servico = Service(ChromeDriverManager().install())
        self.__url = url

    def abrir_navegador(self) -> WebDriver:
        navegador = webdriver.Chrome(service=self.__servico)
        navegador.get(self.__url)
        navegador.maximize_window()
        return navegador

    def digitar_dados(self, navegador: WebDriver, assunto: str):
        barra_busca = navegador.find_element(By.CLASS_NAME, 'gLFyf')
        barra_busca.send_keys(assunto)
        barra_busca.send_keys(Keys.ENTER)

    def percorrer_site(self, navegador: WebDriver):
        navegador.find_element(By.CLASS_NAME, 'pYouzb').click()

    def extrair_informacao(self, navegador: WebDriver) -> List[Dict[str, str]]:
        lojas = navegador.find_elements(By.XPATH, '//span[@class="OSrXXb"]')
        enderecos = navegador.find_elements(
            By.XPATH, '//div[@class="rllt__details"]/div[3]')
        dados = [
            {
                'loja': loja.text,
                'endereco': endereco.text
            } for loja, endereco in zip(lojas, enderecos)
        ]
        return dados

    def executar_paginacao(self, navegador: WebDriver) -> bool:
        try:
            WebDriverWait(navegador, 10).until(EC.element_to_be_clickable(
                (By.ID, 'pnnext'))).click()
            return True
        except NoSuchElementException:
            return False

    def fechar_navegador(self, navegador: WebDriver):
        navegador.quit()
