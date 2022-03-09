"""
Requisito 3 - Passos a se seguir:
1 - Criar a classe Inventory
2 - Dentro da classe Inventory, criar um método chamado import_data
3 - Ele recebe dois parâmetros: caminho para o arquivo e tipo de relatório
4 - Os tipos de relatório podem ser "simples" ou "completo" e
    chamam os generates respectivos de cada classe

Lógica:
1 - Importar o módulo csv
2 - Usar a função dictReader para recuperar os dados no arquivo passado
3 - Criar uma variável que vai armazenar uma lista de dicionários com
    as linhas dos dados recuperados anteriormente
4 - Criar uma condição:
    - quando o tipo for 'simples', retorne o método generate de SR
    - quando for ćomposto, retorne generate de CR
5 - passar a variável com a lista como parâmetro
"""
import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def import_data(path_file, type_report):
        with open(path_file) as csv_file:
            file_data = csv.DictReader(csv_file, delimiter=',', quotechar='"')
            list_result = [data_element for data_element in file_data]

        if type_report == 'simples':
            return SimpleReport.generate(list_result)
        elif type_report == 'completo':
            return CompleteReport.generate(list_result)
