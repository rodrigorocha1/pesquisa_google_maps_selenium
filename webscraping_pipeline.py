from time import sleep
from src.armazem.excel_armazem import ArmazemExcel
from src.armazem.iarmazem import Iarmazem
from src.armazem.operacoes_arquivo import OperacaoArquivo
from src.servico.webscraping_selenium import WebScrapingSeleniun
from src.servico.iwebscraping_google_maps import IWebScrapingGoogleMaps
from src.servico.servico_email.iservico_email import IServicoEmail
from src.servico.servico_email.servico_email_gmail import ServicoEmailGmail


class WebScrapingPipeline():

    def __init__(self, armazem: Iarmazem | OperacaoArquivo, servico: IWebScrapingGoogleMaps, email: IServicoEmail) -> None:

        self.__amarzem = armazem
        self.__servico = servico
        self.__email = email

    def rodar_servico(self, assunto: str):
        navegador = self.__servico.abrir_navegador()

        self.__servico.digitar_dados(
            navegador=navegador,
            assunto=assunto
        )
        self.__servico.percorrer_site(navegador=navegador)
        flag = True
        i = 1
        while flag:
            dados = self.__servico.extrair_informacao(navegador=navegador)

            if not self.__amarzem.verificar_arquivo():
                self.__amarzem.salvar_dados(dados=dados)
            else:
                self.__amarzem.atualizar_dados(dados=dados)
            flag = self.__servico.executar_paginacao(navegador=navegador)
            sleep(4)
            i += 1
            if i == 4:
                break
        self.__servico.fechar_navegador(navegador=navegador)
        self.__email.enviar_email()


if __name__ == '__main__':
    wsp = WebScrapingPipeline(
        armazem=ArmazemExcel(
            nome_aba='escolas',
            nome_arquivo='anuncio.xlsx'
        ),
        servico=WebScrapingSeleniun(
            url='https://www.google.com/',

        ),
        email=ServicoEmailGmail(
            assunto='Envio das Escolas',
            destinatario='silva.rodrigo31@gmail.com',
            nome_arquivo='anuncio.xlsx'
        )
    )
    wsp.rodar_servico(assunto='Escolas em Ribeirão Preto')
