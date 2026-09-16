from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy


TERRA: int = -1


@dataclass
class tipoItem:
    valor: int | float | str | None = None

class PilhaEstatica:
    def __init__(self, tamMax: int):
        self._pilha: list[tipoItem] = [
            tipoItem() for _ in range(tamMax)
        ]
        self._tamMax: int = tamMax
        self._topo: int = TERRA
        self.item: tipoItem | None = None

    def vazia(self) -> bool:
        return self._topo == TERRA

    def cheia(self) -> bool:
        return self._topo == self._tamMax - 1

    def empilha(self, item: tipoItem) -> bool:
        if self.cheia():
            return False

        self._topo += 1
        self._pilha[self._topo] = deepcopy(item)

        return True

    def desempilha(self) -> bool:
        if self.vazia():
            self.item = None
            return False

        self.item = deepcopy(self._pilha[self._topo])
        self._topo -= 1

        return True

    def topo(self) -> tipoItem | None:
        if self.vazia():
            return None

        return deepcopy(self._pilha[self._topo])

    def mostra(self, texto: str) -> None:
        if self.vazia():
            print(f"\nSituação da Pilha {texto}: Vazia!")

        else:
            print(f"\nSituação da Pilha {texto}:")

            for i in range(self._topo, -1, -1):
                print(self._pilha[i].valor)

    def esvazia(self) -> None:
        self._topo = TERRA
        self.item = None

@dataclass
class _tipoNo:
    item: tipoItem | None = None
    _prox: _tipoNo | None = None


class PilhaDinamica:
    def __init__(self, maxTam: int | None = None):
        self._topo: _tipoNo | None = None
        self.item: tipoItem | None = None

    def vazia(self) -> bool:
        return self._topo is None

    def cheia(self) -> bool:
        return False

    def empilha(self, item: tipoItem) -> bool:
        novoNo = _tipoNo()

        novoNo.item = deepcopy(item)
        novoNo._prox = self._topo

        self._topo = novoNo

        return True

    def desempilha(self) -> bool:
        if self.vazia():
            self.item = None
            return False

        self.item = deepcopy(self._topo.item)

        aux = self._topo
        self._topo = self._topo._prox
        aux._prox = None

        return True

    def topo(self) -> tipoItem | None:
        if self.vazia():
            return None

        return deepcopy(self._topo.item)

    def mostra(self, texto: str) -> None:
        if self.vazia():
            print(f"\nSituação da Pilha {texto}: Vazia!")

        else:
            print(f"\nSituação da Pilha {texto}:")

            pos = self._topo

            while pos is not None:
                print(pos.item.valor)
                pos = pos._prox

    def esvazia(self) -> None:
        self.item = None
        self._topo = None


def ehValido(s: str, TipoPilha) -> bool:
    pilha = TipoPilha(len(s))

    for i in range(len(s)):
        caractere: str = s[i]

        if caractere == '(':
            pilha.empilha(tipoItem(caractere))

        elif caractere == ')':
            if pilha.vazia():
                print("Expressão incorreta: falta abre parêntese.")
                return False

            pilha.desempilha()

    if not pilha.vazia():
        print("Expressão incorreta: falta fecha parêntese.")
        return False

    print("Expressão correta.")
    return True


if __name__ == '__main__':
    expressao: str = input('Digite uma expressão matemática: ')
    tipoPilha: int = int(input('Escolha o tipo da pilha: \n1) Estática\n2) Dinâmica\n'))

    match tipoPilha:
        case 1:
            ehValido(expressao, PilhaEstatica)
        case 2:
            ehValido(expressao, PilhaDinamica)