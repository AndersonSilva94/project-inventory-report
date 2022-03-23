"""
Requisito 7: Parte 2
Passos a se seguir:
1 - Criar uma classe InventoryRefactor
2 - Essa classe vai implementar o método __iter__
3 - Essa classe vai cuidar de refatorar o código presente na classe Inventory
4 - Essa classe vai usar as classes definidas no req 6 (que fazem importação)
"""

from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path_file, type_report="simples"):
        report_class = SimpleReport
        if type_report == "simples":
            report_class = CompleteReport
        self.data += self.importer.import_data(path_file)
        return report_class.generate(self.data)
