"""
Requisito 6.2, 6.5 e 6.8 - Passos a se seguir e lógica
1 - Criar uma classe chamada JsonImporter, ela herdará a classe Importer
2 - Seguirá toda a mesma lógica de implementação da classe CsvImporter
"""
from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class JsonImporter(Importer):
    def import_data(path_file):
        if path_file.endswith('json'):
            return Inventory.get_file_json(path_file)
        else:
            raise ValueError('Arquivo inválido')
