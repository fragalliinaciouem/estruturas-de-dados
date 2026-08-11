n: int = int(input("Digite um número: "))
soma: int = 0

j = 0
k = 1

for i in range(n-1):

    if i == 0:
        print(0)

    print(k)
    soma += k
    t = k
    k = j + k
    j = t

print("soma: " + str(soma))