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
2 - Será validado que é possível que o método generate da classe SimpleReport
    retorne a validade mais próxima
    - Percorrer a lista, trazendo o valor mais próximo
"""

from datetime import datetime


class SimpleReport:
    """criei o staticmethod para que o método não
    acessasse ou modificasse propridades da classe"""
    @staticmethod
    def search_by_oldest_fabrication(list_products):
        date_now = datetime.now().strftime('%Y-%m-%d')
        for product_element in list_products:
            if product_element['data_de_fabricacao'] < date_now:
                date_now = product_element['data_de_fabricacao']
        return date_now

    @staticmethod
    def search_by_nearest_fabrication(list_products):
        date_now = datetime.now().strftime('%Y-%m-%d')
        date_list = []
        for product_element in list_products:
            if product_element['data_de_validade'] > date_now:
                date_list.append(product_element['data_de_validade'])
        date_list.sort()
        return date_list

    """criei o classmethod para que o método pudesse ser
    acessado sem instanciar a classe"""
    @classmethod
    def generate(cls, all_products):
        old_fabrication = cls.search_by_oldest_fabrication(all_products)
        near_fabrication = cls.search_by_nearest_fabrication(all_products)[0]
        string_return = (
            f"Data de fabricação mais antiga: {old_fabrication}\n"
            f"Data de validade mais próxima: {near_fabrication}\n"
        )
        return string_return
