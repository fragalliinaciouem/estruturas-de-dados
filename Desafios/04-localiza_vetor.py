from random import randint

def gerarVetor(n: int) -> list[int]:
    return [ randint(0, 10) for _ in range(n) ]


def lerVetor(nome: str, tamanho: int) -> list[int]:
    vetor: list[int] = []

    for i in range(tamanho):
        valor: int = int(input(f'Valor {i + 1} do vetor {nome}: '))
        vetor.append(valor)

    return vetor


def localizarVetor(vetorMaior: list[int], vetorMenor: list[int]) -> list[int]:
    indices: list[int] = []

    if len(vetorMaior) < len(vetorMenor):
        print('Vetores com tamanhos incompatíveis. Vetor gerado maior que vetor procurado.')
        return []

    for i in range(len(vetorMaior) - len(vetorMenor) + 1):
        if vetorMaior[i] == vetorMenor[0]:
            contador: int = 1
            temp: int = i + 1
            indiceEntrado: int = i

            if len(vetorMenor) > 1:
                for j in range(1, len(vetorMenor)):
                    
                    if vetorMaior[temp] == vetorMenor[j]:
                        contador += 1
                        temp += 1

                    if contador == len(vetorMenor):
                        indices.append(indiceEntrado)
            else:
                indices.append(indiceEntrado)

    return indices

def removerVetor(vetorMaior: list[int], vetorMenor: list[int]) -> list[int]:
    m: int = len(vetorMenor)

    if m == 0:
        return vetorMaior

    i: int = 0

    while i <= len(vetorMaior) - m:
        casa: bool = True

        for j in range(m):
            if vetorMaior[i + j] != vetorMenor[j]:
                casa = False
                break

        if casa:
            for _ in range(m):
                for pos in range(i, len(vetorMaior) - 1):
                    vetorMaior[pos], vetorMaior[pos + 1] = vetorMaior[pos + 1], vetorMaior[pos]

            for _ in range(m):
                vetorMaior.pop()
        else:
            i += 1

    return vetorMaior


def substituirVetor(vetorMaior: list[int], vetorMenor: list[int], vetorSubstituto: list[int]) -> list[int]:
    m: int = len(vetorMenor)

    if m == 0:
        return vetorMaior

    if len(vetorMaior) < m:
        print('Vetores com tamanhos incompatíveis. Vetor gerado maior que vetor procurado.')
        return vetorMaior

    resultado: list[int] = []
    i: int = 0

    while i < len(vetorMaior):
        if i <= len(vetorMaior) - m:
            casa: bool = True

            for j in range(m):
                if vetorMaior[i + j] != vetorMenor[j]:
                    casa = False
                    break

            if casa:
                for valor in vetorSubstituto:
                    resultado.append(valor)
                i += m
                continue

        resultado.append(vetorMaior[i])
        i += 1

    return resultado


if __name__ == '__main__':
    valido: bool = True

    padraoN: int = 25
    padraoM: int = 2

    while valido:
        print(f'(1) configuração de n e m (padrões: {padraoN}, {padraoM})\n' + \
                '(2) localizar todas as ocorrências do vetor menor\n' + \
                '(3) remover todas as ocorrências do vetor menor\n' + \
                '(4) substituir todas as ocorrências do vetor menor\n' + \
                '(5) finalizar programa\n')

        opcao: int = int(input('Digite uma opção: '))
        print()

        if opcao == 1:
            novoN: int = int(input(f'Digite o valor de n (padrão = {padraoN}): '))
            novoM: int = int(input(f'Digite o valor de m (padrão = {padraoM}): '))
            print()

            padraoN = novoN
            padraoM = novoM

        elif opcao == 2:
            vetorMaior: list[int] = gerarVetor(padraoN)
            print(f'Vetor maior: {vetorMaior}')

            vetorMenor: list[int] = lerVetor('menor', padraoM)

            print(localizarVetor(vetorMaior, vetorMenor), '\n')

        elif opcao == 3:
            vetorMaior: list[int] = gerarVetor(padraoN)
            print(f'Vetor maior: {vetorMaior}')

            vetorMenor: list[int] = lerVetor('menor', padraoM)

            print(removerVetor(vetorMaior, vetorMenor), '\n')

        elif opcao == 4:
            vetorMaior: list[int] = gerarVetor(padraoN)
            print(f'Vetor maior: {vetorMaior}')

            vetorMenor: list[int] = lerVetor('menor', padraoM)

            tamanhoSubstituto: int = int(input('Quantos elementos tem o vetor substituto? '))
            vetorSubstituto: list[int] = lerVetor('substituto', tamanhoSubstituto)

            print(substituirVetor(vetorMaior, vetorMenor, vetorSubstituto), '\n')

        elif opcao == 5:
            valido = False
            print('Programa finalizado')
