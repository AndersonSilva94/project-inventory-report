"""
Passos que tenho que seguir:
1 - criar a class SimpleReport
2 - essa class tem um método que se chama generate e recebe uma lista
    de dicts
3 - retornar uma string como relatório

Lógica a se pensar:
1 - Será validado que é possível que o método generate da classe SimpleReport
    retorne a data de fabricação mais antiga
    - Aqui vou percorrer a lista, e verificar qual é a data mais antiga
"""

from datetime import datetime


class SimpleReport:
    """criei o staticmethod para que o método não
    acessasse ou modificasse propridades da classe"""
    @staticmethod
    def search_by_oldest_fabrication(list_products):
        date_fabrication = datetime.now().strftime('%Y-%m-%d')
        for product_element in list_products:
            if product_element['data_de_fabricacao'] < date_fabrication:
                date_fabrication = product_element['data_de_fabricacao']
        return date_fabrication

    """criei o classmethod para que o método pudesse ser
    acessado sem instanciar a classe"""
    @classmethod
    def generate(cls, all_products):
        old_fabrication = cls.search_by_oldest_fabrication(all_products)
        string_return = (
            f"Data de fabricação mais antiga: {old_fabrication}"
        )
        return string_return
