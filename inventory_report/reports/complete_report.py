"""
Passos que tenho que seguir:
1 - criar a class CompleteReport
2 - essa class tem um método que se chama generate e recebe uma lista
    de dicts
3 - retornar uma string como relatório
4 - aproveitar métodos que utilizei na criação da classe SimpleReport

Lógica a se pensar:
1 - obter a string retornada na classe SimpleReport
2 - criar uma variável responsável por armazenar uma list com os valores de:
    - nomes da empresa
3 - criar uma variável que vai ser responsável por armazenar um dict de:
    - nome da empresa: qtdade de produtos por empresa
4 - percorrer a lista de nomes usando a lógica:
    - caso a empresa não exista no dict, inserir o valor 1 para ela
    - caso exista, inserir +1 para cada vez que é encontrado
5 - criar uma variável que vai ser responsável por armazenar uma string de:
    - nomes das empresas: qtdades
6 - percorrer o dict, e para cada chave, atribuir ao nome, e cada valor
    a quantidade
7 - somar essa string com a string obtida ao herder o SimpleReport
"""
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(all_products):
        value_simple_report = SimpleReport.generate(all_products)
        list_companies = [product_element['nome_da_empresa']
                          for product_element in all_products]
        dict_companies = {}

        for element in list_companies:
            if element in dict_companies:
                dict_companies[element] += 1
            else:
                dict_companies[element] = 1

        string_companies = ""
        for key, value in dict_companies.items():
            string_companies += f"- {key}: {value}\n"

        string_return = (
            f"{value_simple_report}\n"
            f"Produtos estocados por empresa: \n"
            f"{string_companies}"
        )
        return string_return
