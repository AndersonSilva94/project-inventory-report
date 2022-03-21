"""
Requisito 6 - Passos:
1 - Criar uma classe abstrata Importer
2 - Essa classe vai ter a assinatura import_data e vai receber
    como parâmetro, o nome do arquivo
3 - Esse método deve lançar uma exceção própria caso a extensão
    passada seja inválida
"""
from abc import ABC, abstractmethod

class Importer(ABC):
    @abstractmethod
    def import_data(path_file):
        raise NotImplementedError
