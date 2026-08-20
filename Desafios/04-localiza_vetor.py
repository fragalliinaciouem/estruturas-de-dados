from random import randint

def gerarVetor(n: int) -> list[int]:
    return [ randint(0, 10) for _ in range(n) ]

def localizarVetor(vetorMaior: list[int], vetorMenor: list[int]) -> list[int]:
    indices: list[int] = []

    if len(vetorMaior) < len(vetorMenor):
        print('Vetores com tamanhos incompatíveis. Vetor gerado maior que vetor procurado.')
        return []

    for i in range(len(vetorMaior)):
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

            vetorMenor: list[int] = []

            for i in range(padraoM):
                valor: int = int(input(f'Valor {i + 1} do vetor menor: '))
                vetorMenor.append(valor)

            print(localizarVetor(vetorMaior, vetorMenor), '\n')

        elif opcao == 5:
            valido = False
            print('Programa finalizado')
