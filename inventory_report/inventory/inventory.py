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

Requisito 5 - Passos a se seguir:
1 - Criar dentro da classe Inventory uma estrutura capaz de ler um
    arquivo XML.
2 - Os demais pontos seguem o mesmo princípio dos requisitos anteriores

Lógica:
1 - consultei os seguintes links para saber como ler arquivos xml:
https://raccoon.ninja/pt/dev-pt/manipulando-xml-com-python/
https://docs.python.org/3/library/xml.etree.elementtree.html
2 - Basicamente ler o arquivo utilizando o parse()
3 - Pegando o elemento raiz da variável convertida anteriormente usando
    getroot()
4 - Criar uma variável que vai retornar a lista formatada
5 - Para cada linha do root, criar uma dict que vai ser a tag (chave)
    e text (valor)
6 - Adicionar a dict à variável da lista formatada
7 - Retornar a lista
"""
import csv
import json
import xml.etree.ElementTree as ElementTree
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

    @staticmethod
    def get_file_xml(path_file):
        with open(path_file) as xml_file:
            element = ElementTree.parse(xml_file)
            root = element.getroot()
            data = []
            for child in root:
                item = {}
                for element_child in child:
                    item[element_child.tag] = element_child.text
                data.append(item)
            return data

    @classmethod
    def import_data(cls, path_file, type_report):
        if path_file.endswith('csv'):
            data_converted = cls.get_file_csv(path_file)
        elif path_file.endswith('json'):
            data_converted = cls.get_file_json(path_file)
        else:
            data_converted = cls.get_file_xml(path_file)

        if type_report == 'simples':
            return SimpleReport.generate(data_converted)
        elif type_report == 'completo':
            return CompleteReport.generate(data_converted)
