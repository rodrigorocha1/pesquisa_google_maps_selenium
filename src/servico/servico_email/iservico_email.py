from abc import ABC, abstractmethod


class IServicoEmail(ABC):
    @abstractmethod
    def enviar_email(self):
        pass
