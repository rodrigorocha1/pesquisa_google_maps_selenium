

import os
import smtplib

from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from src.servico.servico_email.iservico_email import IServicoEmail

load_dotenv()


class ServicoEmailGmail(IServicoEmail):
    def __init__(self, destinatario: str, nome_arquivo: str = None, assunto: str = None) -> None:
        self.__rementente = os.environ['from']
        self.__destinatario = destinatario
        self.__msg = MIMEMultipart()
        self.__senha = os.environ['senha']
        self.__caminho_base = os.getcwd()
        self.__nome_arquivo = nome_arquivo
        self.__assunto = assunto

    def __anexar_arquivo(self):
        with open(os.path.join(self.__caminho_base, 'data', 'raw', self.__nome_arquivo), 'rb') as arquivo_axexo:
            anexo = MIMEApplication(arquivo_axexo.read(), _subtype='xlsx')
            anexo.add_header('content-disposition', 'attachment',
                             filename=self.__nome_arquivo)
        self.__msg.attach(anexo)

    def enviar_email(self):
        corpo_email = """
        <p>Parágrafo1</p>
        <p>Parágrafo2</p>
        """

        self.__msg['Subject'] = self.__assunto
        self.__msg['From'] = self.__rementente
        self.__msg['To'] = self.__destinatario

        corpo = MIMEText(corpo_email, 'html')
        self.__msg.attach(corpo)
        self.__anexar_arquivo()
        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()

        s.login(self.__msg['From'], self.__senha)
        s.sendmail(self.__msg['From'], [self.__msg['To']],
                   self.__msg.as_string().encode('utf-8'))
        print('Email enviado')
