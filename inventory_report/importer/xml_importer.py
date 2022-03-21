"""
Requisito 6.3, 6.6 e 6.9 - Passos a se seguir e lógica
1 - Criar uma classe chamada XmlImporter, ela herdará a classe Importer
2 - Seguirá toda a mesma lógica de implementação da classe CsvImporter
"""
from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class XmlImporter(Importer):
    def import_data(path_file):
        if path_file.endswith('xml'):
            return Inventory.get_file_xml(path_file)
        else:
            raise ValueError('Arquivo inválido')
