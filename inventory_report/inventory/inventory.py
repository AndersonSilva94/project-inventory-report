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

Requisito 4 - Passos a se seguir:
1 - Criar dentro da classe Inventory uma estrutura capaz de ler um
    arquivo JSON.
2 - Os demais pontos seguem o mesmo princípio do requisito anterior

Lógica:
1 - Primeiro criar uma def para cada fazer a tratativa de recuperar cada
    tipo de arquivo que vier (fazer uma refatoração aplicando princípios
    de solid)
2 - O def import_data vai receber os valores de caminho do arquivo e tipo
    e verificar qual o tipo, chamando a def correspondente que importa
    aquele tipo de arquivo.
3 - No caso do JSON , importar o json.load para tratar arquivos
"""
import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def get_file_csv(path_file):
        with open(path_file) as csv_file:
            file_data = csv.DictReader(csv_file, delimiter=',', quotechar='"')
            list_result = [data_element for data_element in file_data]
            return list_result

    @staticmethod
    def get_file_json(path_file):
        with open(path_file) as json_file:
            file_data = json.load(json_file)
            return file_data

    @classmethod
    def import_data(cls, path_file, type_report):
        data_converted = []
        if path_file.endswith('csv'):
            data_converted = cls.get_file_csv(path_file)
        elif path_file.endswith('json'):
            data_converted = cls.get_file_json(path_file)

        if type_report == 'simples':
            return SimpleReport.generate(data_converted)
        elif type_report == 'completo':
            return CompleteReport.generate(data_converted)
