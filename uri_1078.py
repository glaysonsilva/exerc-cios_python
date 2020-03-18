N = int(input())
cont = 1
while cont <= 10:
    if 2 < N < 1000:
        print(cont, 'x', N, '=', cont * N)
        cont += 1
