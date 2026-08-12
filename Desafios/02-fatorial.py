def fatorialWhile(n: int) -> int:
    fatorial = 1
    i = 1

    while (i <= n):
        fatorial *= i

        i += 1

    return fatorial


def fatorialFor(n: int) -> int:
    fatorial = 1

    for i in range(1, n+1):
        fatorial *= i

    return fatorial

def fatorialReq(n: int) -> int:
    fatorial = 1

    if n == 1:
        return fatorial

    else:
        fatorial = n * fatorialReq(n-1)

    return fatorial

if __name__ == '__main__':
    valido = True

    while (valido):
        n: int = int(input("Digite um número: "))

        print(f"Fatorial While de {n} = {fatorialWhile(n)}")
        print(f"Fatorial For de {n} = {fatorialFor(n)}")
        print(f"Fatorial Recursivo de {n} = {fatorialReq(n)}")

        escolha: str = input("Deseja executar novamente? (s/n) ")

        if escolha == 'n':
            valido = False