"""
Requisito 8:
Passos a se seguir:
1 - No terminal o comando deve receber dois parâmetros:
    - caminho do arquivo
    - tipo de relatório
2 - Buscar a classe InventoryRefactor para retornar os dados formatados
    e gerar o relatório

Lógica:
1 - Verificar se existem três argumentos passodos (nome + dois parâmetros)
    - Caso não exista exibir "Verifique os argumentos"
2 - Essa verificação deve acontecer usando stderr
3 - Usar o sys.argv para receber os dados do usuário
4 - Imprimir o relatório formatado seguindo os modelos dos requisitos 1
    (SimpleReport) e 2 (CompleteReport)

Lógic a se seguir:
1 - Utilizei esse link para entender a lógica do parâmetro end do print():
https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/
"""
import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    if len(sys.argv) != 3:
        return sys.stderr.write("Verifique os argumentos\n")
    path_file = sys.argv[1]
    type_report = sys.argv[2]

    if sys.argv[1].endswith('csv'):
        report = InventoryRefactor(CsvImporter)
        print(report.import_data(path_file, type_report), end="")
    elif sys.argv[1].endswith('json'):
        report = InventoryRefactor(JsonImporter)
        print(report.import_data(path_file, type_report), end="")
    else:
        report = InventoryRefactor(XmlImporter)
        print(report.import_data(path_file, type_report), end="")
