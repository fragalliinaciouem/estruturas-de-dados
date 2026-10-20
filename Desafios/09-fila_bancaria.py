import random
from copy import deepcopy
from dataclasses import dataclass


@dataclass
class Cliente:
    nome: str
    tempo: int


@dataclass
class TipoItem:
    valor: Cliente | None = None


class FilaEstaticaCircular:
    def __init__(self, tamMax: int):
        self._fila: list[TipoItem] = [TipoItem() for _ in range(tamMax)]
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
            return TipoItem()

        return deepcopy(self._fila[self._inicio])

    def mostrar(self) -> None:
        if self.estaVazia():
            print("Vazia")
            return

        pos = self._inicio

        for i in range(self._nItens):
            cliente = self._fila[pos].valor
            print(f"{cliente.nome}({cliente.tempo})", end="")

            if i < self._nItens - 1:
                print(" -> ", end="")

            pos = (pos + 1) % self._tamMax

        print()


@dataclass
class TipoNo:
    item: TipoItem
    prox: "TipoNo | None" = None


class FilaDinamica:
    def __init__(self, tamMax=None):
        self._primeiro: TipoNo | None = None
        self._ultimo: TipoNo | None = None
        self._nItens: int = 0
        self.item: TipoItem = TipoItem()

    def estaVazia(self) -> bool:
        return self._primeiro is None

    def estaCheia(self) -> bool:
        return False

    def enfileirar(self, item: TipoItem) -> bool:
        novo = TipoNo(deepcopy(item))

        if self.estaVazia():
            self._primeiro = novo
        else:
            self._ultimo.prox = novo

        self._ultimo = novo
        self._nItens += 1
        return True

    def desenfileirar(self) -> bool:
        if self.estaVazia():
            self.item = TipoItem()
            return False

        self.item = deepcopy(self._primeiro.item)
        self._primeiro = self._primeiro.prox
        self._nItens -= 1

        if self._primeiro is None:
            self._ultimo = None

        return True

    def primeiroItem(self) -> TipoItem:
        if self.estaVazia():
            return TipoItem()

        return deepcopy(self._primeiro.item)

    def mostrar(self) -> None:
        if self.estaVazia():
            print("Vazia")
            return

        atual = self._primeiro

        while atual is not None:
            cliente = atual.item.valor
            print(f"{cliente.nome}({cliente.tempo})", end="")

            atual = atual.prox

            if atual is not None:
                print(" -> ", end="")

        print()

def criarCliente(tempoMaximo: int) -> Cliente:
    return Cliente(
        nome=chr(random.randint(ord("A"), ord("Z"))),
        tempo=random.randint(1, tempoMaximo)
    )


def simular(
    Fila,
    ciclos: int,
    tamanhoMaximo: int,
    probabilidadeEntrada: int,
    tempoMaximo: int
):
    fila = Fila(tamanhoMaximo)
    caixa = None
    quantidadeFila = 0

    for ciclo in range(1, ciclos + 1):
        if (
            random.randint(1, 100) <= probabilidadeEntrada
            and quantidadeFila < tamanhoMaximo
            and not fila.estaCheia()
        ):
            if fila.enfileirar(TipoItem(criarCliente(tempoMaximo))):
                quantidadeFila += 1

        if caixa is None and not fila.estaVazia():
            fila.desenfileirar()
            caixa = fila.item.valor
            quantidadeFila -= 1

        if caixa is not None:
            caixa.tempo -= 1

            if caixa.tempo == 0:
                caixa = None

        print(f"Ciclo: {ciclo}/{ciclos}")

        if caixa is None:
            print("Caixa: livre")
        else:
            print(f"Caixa: {caixa.nome} ({caixa.tempo})")

        print("\nFila:")
        fila.mostrar()

        if ciclo < ciclos:
            input("\nPressione Enter para o próximo ciclo...")


print("Tipo de fila:")
print("1 - Estática Circular")
print("2 - Dinâmica")

opcao = input("Escolha: ")

if opcao == "2":
    Fila = FilaDinamica
else:
    Fila = FilaEstaticaCircular

ciclos = int(input("Quantidade de ciclos: "))
tamanho = int(input("Tamanho máximo da fila: "))
probabilidade = int(input("Probabilidade de entrada (%): "))
tempoMaximo = int(input("Tempo máximo de atendimento: "))

simular(
    Fila,
    ciclos,
    tamanho,
    probabilidade,
    tempoMaximo
)
