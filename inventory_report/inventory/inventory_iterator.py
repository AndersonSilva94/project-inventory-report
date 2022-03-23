"""
Requisito 7:
Passos a se seguir:
1 - Criar uma classe chamada InventoryIterator que vai implementar uma
interface (Iterator)

Lógica a se seguir:
1 - Utilizei os links a seguir para entender a lógica do Iterator
- https://docs.python.org/pt-br/3/glossary.html#term-iterator
- https://docs.python.org/pt-br/3/library/stdtypes.html#iterator.__next__
- https://docs.python.org/pt-br/3/library/exceptions.html#StopIteration
- https://docs.python.org/pt-br/3/library/functions.html#iter
"""
from collections.abc import Iterator


class InventoryIterator(Iterator):
    # Método constructor
    def __init__(self, report):
        self.position = 0
        self.report = report

    # Método Next (retorna o próximo item do iterador)
    def __next__(self):
        self.position += 1
        if self.position > len(self.report):
            raise StopIteration()
        return self.report[self.position - 1]
