from dataclasses import dataclass
from copy import deepcopy

_TERRA: int = -1

@dataclass
class TipoItem:
    valor: int | float | str | None = None

class filaEstDin(): # nesse caso Fila Estática Circular
    def __init__(self, tamMax: int):
        self._fila: list[TipoItem] = [ TipoItem() for i in range(tamMax) ]
        self._tamMax: int = tamMax
        self._inicio: int = 0
        self._fim: int = -1
        self._nItens: int = 0
        self.item: TipoItem = TipoItem()

    def estaVazia(self) -> bool:
        return self._nItens == 0

    def estaCheia(self) -> bool:
        return self._nItens == self._tamMax

    def enfileirar(self, item: TipoItem) -> bool:
        if self.estaCheia():
            return False

        self._fim = (self._fim + 1) % self._tamMax
        self._fila[self._fim] = deepcopy(item)
        self._nItens += 1

        return True

    def desenfileirar(self) -> bool:
        if self.estaVazia():
            self.item = TipoItem()
            return False

        self.item = deepcopy(self._fila[self._inicio])
        self._inicio = (self._inicio + 1) % self._tamMax
        self._nItens -= 1

        return True

    def primeiroItem(self) -> TipoItem:
        if self.estaVazia():
            self.item = TipoItem()
            return self.item

        return deepcopy(self._fila[self._inicio])

    def mostrar(self) -> None:
        if self.estaVazia():
            print("Fila vazia!")

        else:
            print("\nElementos da Fila: do último ao primeiro:")
            aux: int = self._fim

            qtd: int = self._nItens
            while qtd > 0:
                print(self._fila[aux].valor, ",", sep="", end="")
                aux = (aux + 1) % self._tamMax
                qtd -= 1

    def esvaziar(self) -> None:
        self._inicio = 0
        self._fim = -1
        self._nItens = 0
        self.item = TipoItem()