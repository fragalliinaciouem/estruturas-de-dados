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

from dataclasses import dataclass
from copy import deepcopy

_TERRA = -1    #representa um fim-terminal para o encadeamento.

"""
A seguir, variáveis de controle do status de algumas operações. As operações de
inserção, remoção, consulta e atualização retornam True ou False quanto ao
sucesso da operação e, além disso, registram o status da operação no atributo
_opSt para retornar o motivo pelo qual o resultado False foi obtido.
"""
LISTAVAZIA      = 1
LISTACHEIA      = 2
ITEMEXISTENTE   = 3
ITEMINEXISTENTE = 4
    
@dataclass
class tipoItem:
    """
    Define os atributos da classe dos itens da lista. O atributo nome é a
    chave usada na ordenação dos itens da lista.
    """
    nome:  str | None = None
    CPF:   str | None = None
    idade: int | None = None

@dataclass
class _tipoNo:
    """
    Define a classe dos Nós da lista. O atributo _prox serve para apontar/referenciar
    o proximo Nó do encadeamento. O valor _TERRA será usado para indicar a posição final
    do encadeamento.
    """
    _item:  tipoItem | None = None
    _prox: int       | None = None   #índice que aponta/indexa o proximo
    

class listaEstDinEncadeada():
    """
    Implementa uma Lista Estática Ordenada Encadeada.
    Define a estrutura, atributos e os métodos disponíveis.
    """

    def __init__(self, maxTam: int):
        """
        Construtor de inicialização: cria uma lista vazia com o numero de
        posições definido pelo usuário. O numero de itens é igual a zero.
        No início, todas as posições estão livres e encadeadas em uma pilha
        e o início da lista de itens é setada com _TERRA.
        """
        self._maxTam:   int  = maxTam
        self._lista:    list = [_tipoNo() for i in range(maxTam)]
        self._numItens: int  = 0
        self._inicio:   int  = _TERRA
        self._livres:   int  = 0
        self._opSt:     int  = LISTAVAZIA
        for pos in range(maxTam-1):
            self._lista[pos]._prox=pos+1
        self._lista[maxTam-1]._prox=_TERRA
        self.item: tipoItem | None = None

    def vazia(self) -> bool:
        """
        Método que retorna True se a lista esta vazia, caso contrário False.
        """
        return self._inicio==_TERRA #ou self._numItens==0

    def cheia(self) -> bool:
        """
        Retorna True se a lista esta cheia, caso contrário False.
        """
        return self._livres==_TERRA #ou self._numItens==self._maxTam

    def opStatus(self) -> bool:
        """
        Retorna o status da operação que registrou o motivo pelo retorno False
        durante as operações insere, remove, consulta e atualiza. Os possiveis
        status são:
        LISTAVAZIA
        LISTACHEIA
        ITEMEXISTENTE
        ITEMINEXISTENTE
        """
        return self._opSt

    def totalItens(self) -> int:
        """
        Retorna o numero de itens da lista.
        """
        return self._numItens

    def _buscaItem(self, nome: str)->int:
        """
        Busca por um item, de acordo com a chave de busca (CPF). Pode ser usado para
        buscar um item existente ou a posição de inserção de um item novo. Retorna a
        posição do elemento anterior: 1) à posição do elemento existente ou 2) à posição
        de inserção do elemento inexistente,na ordem do endadeamento. Se a posição de
        inserção/localização for a primeira da lista, então retorna _TERRA. Retorna
        o status da operação: ITEMINEXISTENTE ou ITEMEXISTENTE.
        """
        if self.vazia():
            self._opSt=ITEMINEXISTENTE
            return _TERRA
        else:
            posAnt=_TERRA
            posAtual=self._inicio
            achou=False
            fimCurso=False
            while not achou and not fimCurso:
                achou=nome<=self._lista[posAtual]._item.nome
                if not achou:
                    posAnt=posAtual
                    posAtual=self._lista[posAtual]._prox
                    fimCurso=posAtual==_TERRA
            if not achou:
                self._opSt=ITEMINEXISTENTE
            elif nome<self._lista[posAtual]._item.nome:
                self._opSt=ITEMINEXISTENTE
            else:
                self._opSt=ITEMEXISTENTE
            return posAnt
        
    def insere(self, item: tipoItem) -> bool:
        """
        Insere o elemento em ordem, de acordo com o nome (chave de busca), e
        retorna o sucesso da operação (True ou False). A inserção é feita a
        frente da posição retornada no _buscaItem. Para retorno False, o
        status da operação pode ser: LISTACHEIA ou ITEMEXISTENTE. Elementos
        repetidos pela chave de busca (já existentes na lista) não são
        inseridos. Incrrementa o número de elementos.
        """   
        if self.cheia():
            self._opSt=LISTACHEIA
            return False
        else:
            pos=self._buscaItem(item.nome)
            if self._opSt==ITEMEXISTENTE:
                return False
            else:    
                posLivre=self._livres
                self._livres=self._lista[self._livres]._prox
                self._lista[posLivre]._item=deepcopy(item)
                if pos==_TERRA:
                    self._lista[posLivre]._prox=self._inicio
                    self._inicio=posLivre
                else:
                    self._lista[posLivre]._prox=self._lista[pos]._prox
                    self._lista[pos]._prox=posLivre
                self._numItens=self._numItens+1
                return True
    
    def remove(self, nome: str) -> bool:
        """
        Remove o elemento da lista, de acordo com o nome (chave de busca),
        retorna uma cópia dele no atributo rem e retorna o sucesso da operação
        (True ou False). A remoção é feita a frente da posição retornada no
        _buscaItem. Para retorno False, o status da operação pode ser: LISTAVAZIA
        ou ITEMINEXISTENTE. Desconecta o elemento removido do encadeamento da
        lista e empilha a casinha por ele ocupada na pilha de livres. Reduz o
        número de elementos da lista. 
        """
        pos=self._buscaItem(nome)
        if self._opSt==ITEMINEXISTENTE:     #lista vazia ou não, não importa
            self.item=None
            return False
        elif pos==_TERRA:
            aux=self._inicio
            self._inicio=self._lista[aux]._prox
        else:
            aux=self._lista[pos]._prox 
            self._lista[pos]._prox=self._lista[aux]._prox
        self._numItens=self._numItens-1
        self._lista[aux]._prox=self._livres
        self._livres=aux
        self.item=deepcopy(self._lista[aux]._item)
        return True
    
    def mostra(self) -> None: 
        """
        Mostra no vídeo todos os elementos da lista.
        """
        if self.vazia():
            self._opSt=LISTAVAZIA
        else:
            pos=self._inicio
            for i in range(self._numItens):
                print(pos,":")
                print("Nome:",self._lista[pos]._item.nome)
                print("CPF:",self._lista[pos]._item.CPF)
                print("Idade:",self._lista[pos]._item.idade)
                pos=self._lista[pos]._prox

        
    #finalizar    
    def consulta(self, nome: str) -> bool:
        """
        Consulta o elemento e retorna o resultado lógico caso tenha sido encontrado
        ou não. Se ele existir, retorna uma copia do item no atributo rem.
        O código é similar ao da remoção, mas sem remover o item.
        """
        pos = self._buscaItem(nome)

        if self._opSt == ITEMINEXISTENTE:
            self.item = None
            return False

        if pos == _TERRA:
            aux = self._inicio
        else:
            aux = self._lista[pos]._prox

        self.item = deepcopy(self._lista[aux]._item)

        return True
        

    #finalizar
    def atualiza(self, item: tipoItem) -> bool:
        """
        Atualiza os componentes do elemento, exceto o nome, se ele existir.
        Retorna o status da operação: LISTAVAZIA ou ITEMINEXISTENTE. Utiliza
        o método _buscaItem().
        """
        pos = self._buscaItem(item.nome)

        if self._opSt == ITEMINEXISTENTE:
            return False

        if pos == _TERRA:
            aux = self._inicio
        else:
            aux = self._lista[pos]._prox

        self._lista[aux]._item.CPF = item.CPF
        self._lista[aux]._item.idade = item.idade

        return True

        
    #finalizar
    def reinicia(self) -> None:
        """
        Reinicia a lista: zera o numero de elementos, seta todas as posicoes
        como valores default, refaz o encadeamento de livres, reinicia os
        controle e retorna status LISTAVAZIA.
        """
        
        self._numItens: int  = 0
        self._inicio:   int  = _TERRA
        self._livres:   int  = 0
        self._opSt:     int  = LISTAVAZIA
        self.item = None

        for pos in range(self._maxTam):
            self._lista[pos]._item = None

        for pos in range(self._maxTam - 1):
            self._lista[pos]._prox = pos + 1

        self._lista[self._maxTam - 1]._prox = _TERRA

