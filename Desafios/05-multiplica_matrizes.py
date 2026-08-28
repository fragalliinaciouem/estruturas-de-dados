from random import randint

def gerarMatriz(m: int, n: int) -> list[list[int]]:
    matriz: list[list[int]] = []

    for i in range(m):
        linha: list[int] = []

        for j in range(n):
            linha.append(randint(-10, 10))

        matriz.append(linha)

    return matriz

def mostrarMatriz(matriz: list[list[int]]) -> None:
    for i in range(len(matriz)):
        print(matriz[i])

def multiplicarMatrizes(matrizA: list[list[int]], matrizB: list[list[int]]) -> list[list[int]]:
    if len(matrizA[0]) != len(matrizB):
        print("Dimensões incompatíveis")
        return [[]]

    matrizC: list[list[int]] = []

    for i in range(len(matrizA)):
        linha: list[int] = []
        for j in range(len(matrizB[0])):
            soma: int = 0
            for k in range(len(matrizB)):
                soma += matrizA[i][k] * matrizB[k][j]
            linha.append(soma)
        matrizC.append(linha)

    return matrizC

if __name__ == '__main__':
    matrizA: list[list[int]] = []
    matrizB: list[list[int]] = []

    valido: bool = True
    while valido: 
        print("\n(1) Gerar matrizes")
        print("(2) Mostrar matrizes")
        print("(3) Multiplicar matrizes")
        print("Digite -1 para sair\n")

        escolha: int = int(input("Digite sua escolha: "))

        if escolha == 1:
            mA: int = int(input("Digite o tamanho da linha da matriz A: "))
            nA: int = int(input("Digite o tamanho da coluna da matriz A: "))
            matrizA = gerarMatriz(mA, nA)

            mB: int = int(int(input("Digite o tamanho da linha da matriz B: ")))
            nB: int = int(int(input("Digite o tamanho da coluna da matriz B: ")))
            matrizB = gerarMatriz(mB, nB)

        elif escolha == 2:
            print("Matriz A:")
            mostrarMatriz(matrizA)

            print("Matriz B:")
            mostrarMatriz(matrizB)

        elif escolha == 3:
            matrizC = multiplicarMatrizes(matrizA, matrizB)
            print("Matriz C:")
            mostrarMatriz(matrizC)

        elif escolha == -1:
            valido = False