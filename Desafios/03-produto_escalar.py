from random import randint

def gerarVetor(n: int) -> list[int]:

    # vetor: list[int] = []
    # for i in range(n):
    #     vetor.append(randint(0, 11))

    # O código acima representa o que acontece em baixo

    return [randint(0, 11) for _ in range(n)]


def produtoEscalarFor(vetor1: list[int], vetor2: list[int]) -> int:
    soma: int = 0

    for i in range(len(vetor1)):
        soma += vetor1[i] * vetor2[i]

    return soma

def produtoEscalarWhile(vetor1: list[int], vetor2: list[int]) -> int:
    soma: int = 0

    i: int = 0
    while i < len(vetor1):
        soma += vetor1[i] * vetor2[i]

        i += 1

    return soma

def produtoEscalarRec(vetor1: list[int], vetor2: list[int]) -> int:
    soma: int = 0

    if len(vetor1) == 0:
        return soma

    else:
        soma += vetor1[0] * vetor2[0] + produtoEscalarRec(vetor1[1:], vetor2[1:])

    return soma

if __name__ == "__main__":
    valido = True

    while valido:
        n = int(input("Digite um número: "))
        print()

        vetor1 = gerarVetor(n)
        vetor2 = gerarVetor(n)

        print(f"Vetor 1: {vetor1}\nVetor 2: {vetor2}\n")

        print(f"Produto escalar com For = {produtoEscalarFor(vetor1, vetor2)}")
        print(f"Produto escalar com While = {produtoEscalarWhile(vetor1, vetor2)}")
        print(f"Produto escalar Recursivo = {produtoEscalarRec(vetor1, vetor2)}\n")

        escolha = input("Deseja continuar? (s/n) ")
        if escolha.lower() == "n":
            valido = False