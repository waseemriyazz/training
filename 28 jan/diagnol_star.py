def diagnol_star(N):
    for i in range(1, N + 1):
        for j in range(N, 0, -1):
            if j != i:
                print(j, end='')
            else:
                print('*', end='')
        print("")
diagnol_star(5)