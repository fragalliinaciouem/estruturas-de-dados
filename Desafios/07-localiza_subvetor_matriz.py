from random import randint

def gerarVetor(n: int) -> list[int]:
    return [randint(0, 10) for _ in range(n)]


def localizarVetor(vetorMaior: list[int], vetorMenor: list[int]) -> list[int]:
    indices: list[int] = []

    tamanho_menor: int = len(vetorMenor)
    tamanho_maior: int = len(vetorMaior)

    if tamanho_maior < tamanho_menor or tamanho_menor == 0:
        print('Vetores com tamanhos incompatíveis ou vazios.')
        return []

    for i in range(tamanho_maior - tamanho_menor + 1):
        corresponde: bool = True

        for j in range(tamanho_menor):
            if vetorMaior[i + j] != vetorMenor[j]:
                corresponde = False

        if corresponde:
            indices.append(i)

    return indices


def gerarMatriz(m: int, n: int) -> list[list[int]]:
    matriz: list[list[int]] = []

    for i in range(m):
        linha: list[int] = []

        for j in range(n):
            linha.append(randint(-10, 10))

        matriz.append(linha)

    return matriz


def mostraMatriz(Mx: list[list[int]], m: int, n: int) -> None:
    print(f'\nMatriz ({m}x{n}):')

    for i in range(m):
        for j in range(n):
            print(f'\t{Mx[i][j]}', end='')

        print()


def matrizParaVetor(matriz: list[list[int]], m: int, n: int) -> list[int]:
    vetor: list[int] = []

    for i in range(m):
        for j in range(n):
            vetor.append(matriz[i][j])

    return vetor


def indiceParaCoordenada(indice: int, n: int) -> tuple[int, int]:
    linha: int = indice // n
    coluna: int = indice % n

    return linha, coluna


if __name__ == '__main__':
    valido: bool = True

    padraoM: int = 5
    padraoN: int = 5
    padraoP: int = 3

    matriz: list[list[int]] = gerarMatriz(padraoM, padraoN)

    while valido:
        print(
            f'\n(1) configuração de m, n e p '
            f'(padrões: m={padraoM}, n={padraoN}, p={padraoP})\n'
            '(2) mostrar matriz\n'
            '(3) montar vetor e localizar\n'
            '(4) finalizar programa'
        )

        try:
            opcao: int = int(input('Digite uma opção: '))
            print()

        except ValueError:
            print('Erro: Por favor, digite um número inteiro válido.')
            continue

        if opcao == 1:
            try:
                novoM: int = int(input(
                    f'Digite o número de linhas m (padrão = {padraoM}): '
                ))

                novoN: int = int(input(
                    f'Digite o número de colunas n (padrão = {padraoN}): '
                ))

                novoP: int = int(input(
                    f'Digite o tamanho do vetor p (padrão = {padraoP}): '
                ))

                if novoM <= 0 or novoN <= 0 or novoP <= 0:
                    print('\nErro: As dimensões devem ser maiores que zero.')

                elif novoP <= novoM * novoN:
                    padraoM = novoM
                    padraoN = novoN
                    padraoP = novoP

                    matriz = gerarMatriz(padraoM, padraoN)

                    print('\nNova matriz gerada.')

                else:
                    print('\nErro: p deve ser menor ou igual a m*n.')

            except ValueError:
                print('\nErro: Entrada inválida. A configuração não foi alterada.')

        elif opcao == 2:
            mostraMatriz(matriz, padraoM, padraoN)

        elif opcao == 3:
            mostraMatriz(matriz, padraoM, padraoN)

            vetorProcurado: list[int] = []

            print(f'\nDigite os {padraoP} elementos do vetor:')

            entradaValida: bool = True

            for i in range(padraoP):
                if entradaValida:
                    try:
                        elemento: int = int(input(f'V[{i}]: '))
                        vetorProcurado.append(elemento)

                    except ValueError:
                        print('\nErro: Você deve digitar apenas números inteiros.')
                        entradaValida = False

            if entradaValida:
                vetorMatriz: list[int] = matrizParaVetor(
                    matriz,
                    padraoM,
                    padraoN
                )

                indices: list[int] = localizarVetor(
                    vetorMatriz,
                    vetorProcurado
                )

                if len(indices) == 0:
                    print('\nVetor não encontrado na matriz.')

                else:
                    print('\nCorrespondências encontradas:')

                    for indiceInicial in indices:
                        indiceFinal: int = indiceInicial + padraoP - 1

                        linhaInicial, colunaInicial = indiceParaCoordenada(
                            indiceInicial,
                            padraoN
                        )

                        linhaFinal, colunaFinal = indiceParaCoordenada(
                            indiceFinal,
                            padraoN
                        )

                        print(
                            f'Início: ({linhaInicial}, {colunaInicial}) '
                            f'-> Fim: ({linhaFinal}, {colunaFinal})'
                        )

        elif opcao == 4:
            valido = False
            print('Programa finalizado.')

        else:
            print('Opção inválida.')