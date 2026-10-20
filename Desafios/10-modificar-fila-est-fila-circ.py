from dataclasses import dataclass
from copy import deepcopy

@dataclass
class tipoItem:
    valor: str | int | float | None = None


@dataclass
class tipoNo:
    item: tipoItem
    prox: "tipoNo | None" = None


class filaEstDin:
    def __init__(self, maxTam=None):
        self._primeiro: tipoNo | None = None
        self._ultimo: tipoNo | None = None
        self._numItens: int = 0
        self.item: tipoItem | None = None

    def vazia(self) -> bool:
        return self._primeiro is None

    def cheia(self) -> bool:
        return False

    def enfileira(self, item: tipoItem) -> bool:
        novo = tipoNo(deepcopy(item))

        if self.vazia():
            self._primeiro = novo
        else:
            self._ultimo.prox = novo

        self._ultimo = novo
        self._numItens += 1
        return True

    def desenfileira(self) -> bool:
        if self.vazia():
            self.item = None
            return False

        self.item = deepcopy(self._primeiro.item)
        self._primeiro = self._primeiro.prox
        self._numItens -= 1

        if self._primeiro is None:
            self._ultimo = None

        return True

    def itemPrimeiro(self) -> tipoItem | None:
        if self.vazia():
            return None

        return deepcopy(self._primeiro.item)

    def mostra(self) -> None:
        if self.vazia():
            print("\nSituação da Fila: Vazia!")
            return

        print("\nSituação da Fila: ", end="")

        atual = self._primeiro

        while atual is not None:
            print(atual.item.valor, end="")
            atual = atual.prox

            if atual is not None:
                print(", ", end="")

        print("\n")

    def esvazia(self) -> None:
        self._primeiro = None
        self._ultimo = None
        self._numItens = 0
        self.item = None