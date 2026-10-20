"""
Módulo que implementa um TAD de Fila Estática Circular. Nesse caso, a fila é
implementada em um vetor estático (lista de tamanho máximo de posições, sendo
as entradas já criadas na inicialização da estrutura.

Em uma fila podemos enfileirar e desenfileira itens de dados, usando métodos
específicos definidos para essa finalidade. Não podemos manipular os dados
se não for por meio desses métodos. Sempre que precisar enfileirar um novo
item na fila, devemos inseri-lo no final da fila (após todos os demais que já
estão na fila) e sempre precisar desenfileirar um item, devemos remover o item que
está no início da fila.

Portanto, uma fila funciona segundo o modelo FIFO (First In First Out), ou seja,
o primeiro a entrar é o primeiro a sair. Ou LILO. 

Podemos também consultar o item que está no início da fila, que será o próximo
a sair. A consulta do item que está por último também pode ser implementada,
mas não é uma operação padrão, pois, em tese, para chegar a vez do último item,
todos os anteriores deveriam ser antes removidos. Não podemos acessar os itens
no meio da fila, intermediários.

A fila estática começa vazia e na medida em que os dados são enfileirados, o
marcador de final da fila vai caminhando rumo ao final do vetor. Da mesma forma,
na medida em que os elementos são desenfileirados, o marcador de início da fila
tambem vai se movendo rumo ao final do vetor. Entretanto, quando esses marcadores
de início ou de fim atingem a última posição do vetor, eles continuam a caminhar
na posição inicial do vetor. Ambos os marcadores caminham no mesmo sentido. Esse
tipo de caminhamento é conhecido como circular, por ficar circulando no vetor.

Como a estrutura é estática, ela comporta uma quantidade máxima de itens.
"""

from dataclasses import dataclass
from copy import deepcopy

@dataclass
class TipoItem:
    """
    Define o tipo do item da fila, ou seja, o tipo do dado que será enfileirado
    ou desenfileirado. No caso aqui, apenas um valor inteiro, mas poderia ser um
    conjunto de valores, tipo: nome, idade, CPF etc...
    """
    valor: str | int | float | None = None


class filaEstDin(): #nesse caso, Fila Estática Circular
    """
    Construtor da fila. Incializa os atributos que gerenciam o TAD.

    self._maxTam:      tamanho do vetor alocado; número máximo de itens
    self._fila:        vetor alocado. Vide Obs no TAD pilha
    self._posPrimeiro: marcador do primeiro elemento (início da fila)
    self._posUltimo:   marcador do último elemento (final da fila)
    self._numItens:    controla a quantidade de itens na fila
    self.item:         armazena uma cópia do item do ultimo desenfileiramento
    """

    def __init__(self, maxTam: int):
        self._maxTam:       int             = maxTam
        self._fila:         list            = [None for i in range(maxTam)]
        self._posPrimeiro:  int             = 0
        self._posUltimo:    int             = -1
        self._numItens:     int             = 0
        self.item:          TipoItem | None = None
    
    def vazia(self) -> bool:
        return self._numItens == 0
    
    def cheia(self) -> bool:
        return self._numItens == self._maxTam

    def enfileira(self, item: TipoItem) -> bool:
        """
        Caso haja espaço alocado na estrutura, insere um novo elemento no final
        da fila, após o último. Esse novo elemento passa a ser o novo último.
        Altera o marcador de final de fila. Aumenta a quantidade de elementos.
        Retorna o suscesso da operação.
        """
        if self.cheia():
            return False
        else:
            self._posUltimo = (self._posUltimo+1) % self._maxTam
            self._fila[self._posUltimo] = deepcopy(item)
            self._numItens = self._numItens+1
            return True

    def desenfileira(self) -> bool:
        """
        Caso a estrutura não esteja vazia, remove o elemento que está no início,
        da fila, fazendo com que o elemento depois deste seja o novo início. Altera
        o marcador de início de fila. Diminui a quantidade de elementos. Retorna
        uma cópia do elemento removido em self.item. Retorna o suscesso da operação.
        """
        if self.vazia():
            self.item=None
            return False
        else:
            item: TipoItem = self._fila[self._posPrimeiro]
            self._posPrimeiro = (self._posPrimeiro+1) % self._maxTam
            self._numItens=self._numItens-1
            self.item=deepcopy(item)
            return True
    
    def itemPrimeiro(self) -> TipoItem:
        """
        Caso a estrutura não esteja vazia, retorna uma cópia do elemento que
        está na primeira posição, sem precisar removê-lo. O marcador de início
        continua com o mesmo valor. Não altera a quantidade de elementos.
        """
        if self.vazia():
            return None
        else:
            item: TipoItem = self._fila[self._posPrimeiro]
            return deepcopy(item)
        
    def mostra(self) -> None:
        """
        Mostra os elementos enfileirados, do primeiro até o último. Este método não
        faz parte do TAD em si, mas existe aqui apenas para fins didáticos.
        """
        if self.vazia():
            print("\nSituação da Fila: Vazia!")
        else:
            print("\nSituação da Fila: ",end="")
            pos=self._posPrimeiro
            for i in range(self._numItens-1):
                print(self._fila[pos].valor,", ", sep="",end="")
                pos=(pos+1)%self._maxTam
            if (self._numItens>0):
                print(self._fila[pos].valor)
            print("")

    def esvazia(self) -> None:
        """
        Reinicia os controles da fila para o estado inicial
        """
        self._posPrimeiro   = 0
        self._posUltimo     = -1
        self._numItens      = 0
        self.item            = None

        

