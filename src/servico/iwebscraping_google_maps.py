from abc import abstractmethod, ABC
from selenium.webdriver.chrome.webdriver import WebDriver


class IWebScrapingGoogleMaps(ABC):

    @abstractmethod
    def abrir_navegador(self) -> WebDriver:
        pass

    @abstractmethod
    def digitar_dados(self, navegador: WebDriver, assunto: str):
        pass

    @abstractmethod
    def percorrer_site(self, navegador: WebDriver):
        pass

    @abstractmethod
    def extrair_informacao(self, navegador: WebDriver):
        pass

    @abstractmethod
    def executar_paginacao(self, navegador: WebDriver):
        pass

    @abstractmethod
    def fechar_navegador(self, navegador: WebDriver):
        pass
