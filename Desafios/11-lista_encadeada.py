"""
Lista Estática Ordenada Encadeada. Utiliza um vetor com a quantidade máxima de
posições/entradas ("casinhas") já alocada/definida para armazenar itens de dados.
Cada entrada do vetor acomoda um nó da lista. Cada nó acomoda um item de dado
e um campo de próximo que referencia o próximo nó/item da lista, na ordem do
encadeamento. Na lista ordenada de itens, os elementos são ordenados de acordo
com o campo chave, que aqui é o nome.

O encadeamento é estático, feito com índices do vetor e não com referências/
ponteiros de memória. Apontar para o próximo item da lista é manter o índice
do vetor onde ele se encontra.

O início da lista é controlado pelo atributo _inicio. As casinhas livres são
controladas pelo atributo _livres. No início, todas as casinhas estão livres.
Essas casinhas livres são organizadas como uma pilha estática encadeada, sendo
que um nó aponta para o outro e as casinhas são utilizadas sob demanda.

Uma casinha livre é retirada do topo da pilha de nós livres e utilizada para a
inserção de um novo item na lista, sendo encadeada na posição de inserção do
item na lista. O topo da pilha de nós livres é controlado pelo atríbuto _livres.
Na remoção de um elemento da lista, a casinha utilizada pelo item removido é
desconectada da lista de itens e empilhada novamente na pilha de casinhas livres.

Existe uma função de busca que retorna a posição (índice) do item anterior a
posição em que o item esteja inserido ou que deve ser inserido. Essa busca deve
ser usada nos métodos de inserção, de remoção, de atualização e de consulta.
"""

from copy import deepcopy
from dataclasses import dataclass

TERRA: int = -1


@dataclass
class tipoItem:
    nome: str | None = None


@dataclass
class tipoNo:
    item: tipoItem
    prox: int = TERRA


class listaEstOrdEnc:
    def __init__(self, maxTam: int):
        self._maxTam: int = maxTam
        self._inicio: int = TERRA
        self._livres: int = 0
        self._numItens: int = 0
        self.item: tipoItem | None = None
        self._vetor: list[tipoNo] = [
            tipoNo(item=tipoItem(), prox=i + 1 if i < maxTam - 1 else TERRA)
            for i in range(maxTam)
        ]

    def vazia(self) -> bool:
        return self._numItens == 0

    def cheia(self) -> bool:
        return self._numItens == self._maxTam

    def _retiraLivre(self) -> int:
        """
        Retira uma casinha do topo da pilha de nós livres (desempilha).
        """
        if self.cheia():
            return TERRA

        idx = self._livres
        self._livres = self._vetor[idx].prox
        self._vetor[idx].prox = TERRA
        return idx

    def _devolveLivre(self, idx: int) -> None:
        """
        Devolve a casinha para o topo da pilha de nós livres (empilha).
        """
        self._vetor[idx].item = tipoItem()
        self._vetor[idx].prox = self._livres
        self._livres = idx

    def _busca(self, nome: str) -> int:
        """
        Retorna o índice da casinha anterior (ant) à posição onde o item
        está inserido ou onde deve ser inserido na lista ordenada.
        Se deve ser inserido no início ou se a lista estiver vazia, retorna TERRA.
        """
        ant = TERRA
        atual = self._inicio

        while atual != TERRA and self._vetor[atual].item.nome < nome:
            ant = atual
            atual = self._vetor[atual].prox

        return ant

    busca = _busca

    def consultar(self, nome: str) -> tipoItem | None:
        if self.vazia() or nome is None:
            self.item = None
            return None

        ant = self._busca(nome)
        if ant == TERRA:
            alvo = self._inicio
        else:
            alvo = self._vetor[ant].prox

        if alvo == TERRA or self._vetor[alvo].item.nome != nome:
            self.item = None
            return None

        self.item = deepcopy(self._vetor[alvo].item)
        return deepcopy(self._vetor[alvo].item)

    def inserir(self, item: tipoItem) -> bool:
        if item.nome is None or item.nome == "":
            return False

        if self.cheia():
            return False

        ant = self._busca(item.nome)
        if ant == TERRA:
            alvo = self._inicio
        else:
            alvo = self._vetor[ant].prox

        if alvo != TERRA and self._vetor[alvo].item.nome == item.nome:
            return False

        novo = self._retiraLivre()
        if novo == TERRA:
            return False

        self._vetor[novo].item = deepcopy(item)

        if ant == TERRA:
            self._vetor[novo].prox = self._inicio
            self._inicio = novo
        else:
            self._vetor[novo].prox = self._vetor[ant].prox
            self._vetor[ant].prox = novo

        self._numItens += 1
        return True

    def remover(self, nome: str) -> bool:
        if self.vazia() or nome is None:
            self.item = None
            return False

        ant = self._busca(nome)
        if ant == TERRA:
            alvo = self._inicio
        else:
            alvo = self._vetor[ant].prox

        if alvo == TERRA or self._vetor[alvo].item.nome != nome:
            self.item = None
            return False

        self.item = deepcopy(self._vetor[alvo].item)

        if ant == TERRA:
            self._inicio = self._vetor[alvo].prox
        else:
            self._vetor[ant].prox = self._vetor[alvo].prox

        # Devolve a casinha para a pilha de livres
        self._devolveLivre(alvo)
        self._numItens -= 1
        return True

    def atualizar(self, nome: str, novoItem: tipoItem) -> bool:
        if self.vazia() or nome is None or novoItem.nome is None or novoItem.nome == "":
            self.item = None
            return False

        ant = self._busca(nome)
        if ant == TERRA:
            alvo = self._inicio
        else:
            alvo = self._vetor[ant].prox

        if alvo == TERRA or self._vetor[alvo].item.nome != nome:
            self.item = None
            return False

        if novoItem.nome != nome:
            ant_novo = self._busca(novoItem.nome)

            if ant_novo == TERRA:
                alvo_novo = self._inicio
            else:
                alvo_novo = self._vetor[ant_novo].prox

            if alvo_novo != TERRA and self._vetor[alvo_novo].item.nome == novoItem.nome:
                self.item = None
                return False

            self.remover(nome)

            if self.inserir(novoItem):
                self.item = deepcopy(novoItem)
                return True

            return False

    def mostra(self) -> None:
        if self.vazia():
            print("\nSituação da Lista: Vazia!")
            return

        print("\nSituação da Lista: ", end="")
        atual = self._inicio
        primeiro = True

        while atual != TERRA:
            if not primeiro:
                print(", ", end="")
            print(self._vetor[atual].item.nome, end="")
            primeiro = False
            atual = self._vetor[atual].prox

        print("")

    def esvazia(self) -> None:
        self._inicio = TERRA
        self._numItens = 0
        self.item = None
        self._livres = 0

        for i in range(self._maxTam):
            prox = i + 1 if i < self._maxTam - 1 else TERRA
            self._vetor[i].item = tipoItem()
            self._vetor[i].prox = prox


if __name__ == "__main__":
    lista = listaEstOrdEnc(5)

    print("--- Lista vazia ---")
    lista.mostra()

    print("--- Inserções fora de ordem ---")
    lista.inserir(tipoItem("Carlos"))
    lista.inserir(tipoItem("Ana"))
    lista.inserir(tipoItem("Bruno"))
    lista.mostra()

    print("--- Consultar ---")
    print("Ana:", lista.consultar("Ana"))
    print("Zeca:", lista.consultar("Zeca"))

    print("--- Remover Bruno ---")
    lista.remover("Bruno")
    lista.mostra()
    print("Item removido:", lista.item)

    print("--- Atualizar Ana (mesma chave) ---")
    lista.atualizar("Ana", tipoItem("Ana"))
    lista.mostra()

    print("--- Tentativa de atualizar Ana para Carlos (chave já existente) ---")
    print("Sucesso:", lista.atualizar("Ana", tipoItem("Carlos")))
    lista.mostra()

    print("--- Preencher até cheia ---")
    lista.inserir(tipoItem("Bruno"))
    lista.inserir(tipoItem("Diana"))
    lista.inserir(tipoItem("Edu"))
    lista.mostra()
    print("Cheia:", lista.cheia())
    print("Inserir extra:", lista.inserir(tipoItem("Fernanda")))
