from dataclasses import dataclass
from copy import deepcopy

TERRA: int = -1

@dataclass
class TipoItem:
    valor: int | float | str | None = None

class Pilha:
    def __init__(self, tamMax: int):
        self._pilha: list[TipoItem] = [ TipoItem() for i in range(tamMax) ]
        self._tamMax: int = tamMax
        self._topo: int = TERRA
        self.rem: TipoItem = TipoItem()

    def estaVazia(self) -> bool:
        return self._topo == TERRA

    def estaCheia(self) -> bool:
        return self._topo == self._tamMax - 1

    def empilhar(self, item: TipoItem) -> bool:
        if self.estaCheia():
            return False

        self._topo += 1
        self._pilha[self._topo] = deepcopy(item)

        return True

    def desempilhar(self) -> bool:
        if self.estaVazia():
            return False

        self.rem = deepcopy(self._pilha[self._topo])
        self._topo -= 1
        return True


    def topo(self) -> TipoItem:
        if self.estaVazia():
            return TipoItem()

        return deepcopy(self._pilha[self._topo])

    def mostrar(self) -> None:
        if self.estaVazia():
            print('\nSituação da Pilha: vazia\n')

        else:
            print('\nSituação da Pilha:')

            for i in range(self._topo + 1, -1, -1):
                print(self._pilha[i].valor)

    def esvaziar(self) -> None:
        self._topo = -1
        self.rem = TipoItem()