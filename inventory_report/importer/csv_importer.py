"""
Requisito 6.1, 6.4 e 6.7 - Passos a se seguir e lógica
1 - Criar uma classe chamada CsvImporter, ela herdará a classe Importer
2 - O método import_data herdado fará exatamente o que foi implementado
    na classe Inventory, dessa forma, cada Importer retornará seus dados
    já tratados conforme o tipo
3 - Como já existem métodos que fazem essa tratativa, posso acessá-los
    para usar no retorno dos doados
4 - Caso a extensão não seja compatível, lançar uma exceção de arquivo
    - segundo o teste o erro deve ter o valor igual a 'Arquivo Inválido'
"""
from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class CsvImporter(Importer):
    def import_data(path_file):
        if path_file.endswith('csv'):
            return Inventory.get_file_csv(path_file)
        else:
            raise ValueError('Arquivo Inválido')
