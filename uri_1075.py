N = int(input('Digite um valor: '))
cont = 1
while cont <= 10000:
    if N < 10000:
        if cont % N == 2:
            print(cont)
        cont += 1
