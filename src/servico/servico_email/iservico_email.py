from abc import ABC, abstractmethod


class IServicoEmail(ABC):
    @classmethod
    def enviar_email(assunto: str):
        pass
