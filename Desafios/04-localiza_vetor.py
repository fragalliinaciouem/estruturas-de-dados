from random import randint

def gerarVetor(n: int) -> list[int]:
    return [ randint(0,10) for _ in range(n) ]

def procurarVetor(vetorMaior: list[int], procurado: list[int]) -> int:
    indiceMenor: int = -1

    for i in range(len(vetorMaior)):

        if vetorMaior[i] == procurado[0]:
            contador: int = 0
            temp = i
            indiceEntrado = i

            for j in range(1, len(procurado)):
                if temp + 1 < len(vetorMaior):
                    if vetorMaior[temp+1] == procurado[j]:
                        contador += 1

            if contador == len(procurado) - 1:
                indiceMenor = indiceEntrado


    return indiceMenor


if __name__ == "__main__":
    n: int = int(input("Digite a quantidade de números: "))

    vetorMaior: list[int] = gerarVetor(n)
    print(vetorMaior)

    procurado: list[int] = []
    vetorMenor = input("Digite o vetor menor (entre espaços): ")

    for i in vetorMenor.split():
        procurado.append(int(i))

    print(procurarVetor(vetorMaior, procurado))

    