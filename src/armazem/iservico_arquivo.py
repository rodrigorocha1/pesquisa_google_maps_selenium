from abc import ABC, abstractmethod


class IServicoArquivo(ABC):

    @abstractmethod
    def verificar_arquivo(self):
        pass
